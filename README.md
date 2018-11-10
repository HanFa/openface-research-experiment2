
# Openface Experiment 2
This repo is an experiment with support of [Openface](http://cmusatyalab.github.io/openface/). For the [face classifaction application](http://cmusatyalab.github.io/openface/demo-3-classifier/#2-preprocess-the-raw-images), the relationship between training sample number vs. model size vs. model accuracy \& confidence is studied in this experiment.

## Experiment procedure
Please follow `./run_experiment.sh` for each step of the experiment. There are mainly 5 steps as listed below

* Download the dataset by extracting txts
* Prune the dataset to different size (to make models of different maturity)
* Preprocess: Align the faces for each dataset
* Generate representation for each dataset
* Train models for each dataset
* Predict with test images and get results

## Experiment results

1. Model size
To get results, run `./utils/plot_model_size.py`.

![model_size](./results/model_size.png)

2. Model confidence compare: stateful vs. stateless

![model_conf1](./results/model_conf_compare_1.png)
![model_conf2](./results/model_conf_compare_2.png)
![model_conf3](./results/model_conf_compare_3.png)
![model_conf4](./results/model_conf_compare_4.png)
![model_conf5](./results/model_conf_compare_5.png)
![model_conf6](./results/model_conf_compare_6.png)
![model_conf7](./results/model_conf_compare_7.png)


