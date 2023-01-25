import sys 
sys.path.append('..')

import copy
import math
from collections import defaultdict
from helper import *

FILENAME = '20_dat.txt'
mapper = {}

def main():
    i = 1
    while True:
        ds = find_divisors(i)
        # print(i, ds)
        # print(i, 10*sum(ds))
        if 10*sum(ds) >= 36000000:
            print(i)
            return
        i += 1

def find_divisors(i):
    d = set()
    for a in range(1, math.ceil(math.sqrt(i))+1):
        if i % a == 0:
            d.add(a)
            d.add(i//a)
    return d

STOP_AT = 50

def main2():
    i = 1
    delivered = def_dict(0)
    tired = set()
    while True:
        ds = find_divisors_2(i, delivered, tired)
        # print(i, ds)
        # print(i, 11*sum(ds))
        if 11*sum(ds) >= 36000000:
            print(i)
            return
        # if i == 15:
        #     exit(1)
        i += 1

def find_divisors_2(i, delivered, tired):
    d = set()
    for a in range(1, math.ceil(math.sqrt(i))+1):
        if i % a == 0:
            if a not in tired:
                d.add(a)
            if i//a not in tired:
                d.add(i//a)
    for x in d:
        delivered[x] += 1
        if delivered[x] == STOP_AT:
            tired.add(x)
    return d

if __name__ == '__main__':
    main()
    main2()
