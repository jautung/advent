import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [int(i) for i in data[0].split(',')]
    for i in range(80):
        data = transform(data)
    print(len(data))

def transform(data):
    new_dat = []
    count = 0
    for i in data:
        if i == 0:
            new_dat.append(6)
            count += 1
        else:
            new_dat.append(i - 1)
    for i in range(count):
        new_dat.append(8)
    return new_dat

def main2():
    data = readlines(FILENAME)
    data = [int(i) for i in data[0].split(',')]
    counts = [0] * 9
    for i in data:
        counts[i] += 1
    for i in range(256):
        counts = transform_counts(counts)
    print(sum(counts))

def transform_counts(counts):
    new_counts = [0] * 9
    for i in range(8):
        new_counts[i] = counts[i+1]
    new_counts[6] += counts[0]
    new_counts[8] += counts[0]
    return new_counts

if __name__ == '__main__':
    main()
    main2()
