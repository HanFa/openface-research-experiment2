#!/usr/bin/env python3
import os, sys
from matplotlib import pyplot as plt


def handle_ans_file(path, stateless=False, stateless_model_train_num=20):
    file_idxs = []
    confs = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            file_idx = int(line.split('\t')[0].split('/')[-1].split('_')[0])
            conf = float(line.split('\t')[-1])
            if stateless and file_idx <= stateless_model_train_num: continue
            file_idxs.append(file_idx)
            confs.append(conf)

    return file_idxs, confs


if __name__ == '__main__':
    stateful = os.path.join(os.getcwd(), sys.argv[1])
    stateless = sys.argv[2]
    person_idx = sys.argv[3]
    print("stateful:" + stateful)

    file_idxs, confs = handle_ans_file(stateful)
    plt.scatter(file_idxs, confs, label="stateful")
    file_idxs, confs = handle_ans_file(stateless, True)
    plt.scatter(file_idxs, confs, label="stateless")
    plt.legend()
    plt.xlabel("train frame num")
    plt.ylabel("model confidence")
    plt.title("Results for person {}".format(person_idx))
    plt.xlim(0, 150)
    plt.ylim(0, 1)
    plt.savefig("model_conf_compare_{}".format(person_idx))
