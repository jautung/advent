import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def count_group(dat):
    x = [set(d) for d in dat]
    y = set()
    for i in x:
        y = y.union(i)
    return len(y)

def main():
    data = readlines_split_by_newlines(FILENAME)
    data = [count_group(dat) for dat in data]
    # print(data)
    print(sum(data))

def count_group2(dat):
    x = [set(d) for d in dat]
    y = x[0]
    # print(x)
    for i in x:
        y = y.intersection(i)
    return len(y)

def main2():
    data = readlines_split_by_newlines(FILENAME)
    data = [count_group2(dat) for dat in data]
    # print(data)
    print(sum(data))

if __name__ == '__main__':
    main()
    main2()
