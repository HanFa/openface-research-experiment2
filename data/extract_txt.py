#!/usr/bin/env python3
import os
import argparse
import requests
from tqdm import tqdm

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Extract all images from the txt files")
    parser.add_argument('--txt-dir', default='txts', dest='txt_dir', help='Path to the folder containing txt files')
    parser.add_argument('--out-dir', default='images', dest='out_dir', help='Path to the output folder containing images')
    args = parser.parse_args()
    txt_files = os.listdir(args.txt_dir)
    txt_files = map(lambda x: (os.path.join(args.txt_dir, x), x.split('.')[0]), txt_files)

    for file_path, name in txt_files:
        with open(file_path, 'r') as o:
            print("*** Downloading {}".format(name))
            for line in tqdm(o.readlines()):
                index = line.split(' ')[0]
                url = line.split(' ')[1]
                if not os.path.exists(os.path.join(args.out_dir, name)):
                    os.makedirs(os.path.join(args.out_dir, name))
                if os.path.exists(os.path.join(args.out_dir, name, index + '.jpg')):
                    continue
                try:
                    r = requests.get(url)
                except IOError as e:
                    print(e)
                    continue

                if r.status_code == 200 and 'Content-Type' in r.headers and "image" in r.headers['Content-Type']:
                    with open(os.path.join(args.out_dir, name, index + '.jpg'), 'w') as i:
                        i.write(r.content)

