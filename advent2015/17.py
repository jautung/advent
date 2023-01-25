import sys 
sys.path.append('..')

import copy
from itertools import chain, combinations
from collections import defaultdict
from helper import *

FILENAME = '17_dat.txt'
mapper = {}

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def main():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]

    TARGET = 150

    count = 0
    for i in powerset(data):
        if sum(i) == TARGET:
            count += 1
    print(count)

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]

    TARGET = 150

    min_count = None
    for i in powerset(data):
        if sum(i) == TARGET:
            if min_count == None or len(i) < min_count:
                min_count = len(i)
    # print(min_count)

    count = 0
    for i in powerset(data):
        if sum(i) == TARGET and len(i) == min_count:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
    main2()
