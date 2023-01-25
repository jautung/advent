import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[[int(j) for j in i.split('-')] for i in dat.split(',')] for dat in data]
    count = 0
    for dat in data:
        if fully_contains(dat[0], dat[1]) or fully_contains(dat[1], dat[0]):
            count += 1
    print(count)

def fully_contains(r1, r2):
    if r1[0] <= r2[0] and r1[1] >= r2[1]:
        return True
    return False

def main2():
    data = readlines(FILENAME)
    data = [[[int(j) for j in i.split('-')] for i in dat.split(',')] for dat in data]
    count = 0
    for dat in data:
        if overlap(dat[0], dat[1]):
            count += 1
    print(count)

def overlap(r1, r2):
    # print(r1, r2)
    if r1[0] <= r2[0] and r2[0] <= r1[1]:
        # print('t')
        return True
    if r2[0] <= r1[0] and r1[0] <= r2[1]:
        # print('t')
        return True
    # print('f')
    return False

if __name__ == '__main__':
    main()
    main2()
