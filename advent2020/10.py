import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '10_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    data.sort()
    counters = dict()
    counters[1] = 0
    counters[2] = 0
    counters[3] = 0
    for i, d in enumerate(data):
        if i == 0:
            counters[data[i]-0] += 1
            continue
        counters[data[i]-data[i-1]] += 1
    counters[3] += 1
    print(counters[1]*counters[3])

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    data.sort()
    data = data + [data[-1]+3]
    use_up_to_this = dict()
    use_up_to_this[0] = 1
    for d in data:
        count_for_this = 0
        if d - 3 in data or d - 3 == 0:
            count_for_this += use_up_to_this[d - 3]
        if d - 2 in data or d - 2 == 0:
            count_for_this += use_up_to_this[d - 2]
        if d - 1 in data or d - 1 == 0:
            count_for_this += use_up_to_this[d - 1]
        use_up_to_this[d] = count_for_this
    print(use_up_to_this[data[-1]])

if __name__ == '__main__':
    main()
    main2()
