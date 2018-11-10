#!/usr/bin/env bash

# Download data
function download_dataset() {
    ./data/extract_txt.py
}

# Preprocess: Align the faces for the dataset: ./data/images/raw
function align_face() {
    ./utils/align-dlib.py --dlibFacePredictor ./dlib/shape_predictor_68_face_landmarks.dat \
    ./data/images/raw align outerEyesAndNose ./data/images/align --size 96 
}

# Generate representation for each dataset
function generate_rep() {

    for j in `seq 1 7`
    do 
        mkdir models/$j
        find models -name "cache*" | xargs rm
        for i in `seq 1 140`
        do
        
            mkdir models/$j/align-$i/
            cp -r ./data/images/dummy/* models/$j/align-$i/
            mkdir models/$j/features-$i/
            find ./data/images/align/$j/ -maxdepth 1 -type f | head -$i | xargs cp -t models/$j/align-$i/$j
            ./batch-represent/main.lua -model ./openface/nn4.small2.v1.t7 -outDir models/$j/features-$i/ -data models/$j/align-$i/
        done
    done
}

# Dump the trained model in form of pickles
function get_train_models() {
    for j in `seq 1 7`
    do
        for i in `seq 1 140`
        do
            ./classifier.py train ./models/$j/features-$i/
        done
    done
}

# 
function predict_stateful_images() {

    for j in `seq 1 7`
    do
        for i in `seq 1 140`
        do
            test_img=`ls ./test_images/$j/ | head -$(( i+1 )) | tail -1`
            dump="stateful"
            dump+="$j"
            ./classifier.py --resultDump=$dump infer ./models/$j/features-$i/*.pkl ./test_images/$j/$test_img
        done
    done
}

function predict_stateless_images() {
    for j in `seq 1 7`
    do
        for i in `seq 1 140`
        do
            test_img=`ls ./test_images/$j/ | head -$(( i+1 )) | tail -1`
            dump="stateless"
            dump+="$j"
            ./classifier.py infer --resultDump=$dump ./models/$j/features-20/*.pkl ./test_images/$j/$test_img
        done
    done
}

predict_stateful_images
# predict_stateless_images