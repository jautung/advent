import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '3_dat.txt'
mapper = {}

def parse(dat):
    index = int(dat[0][1:])
    a = dat[2].split(',')
    x = int(a[0])
    y = int(a[1][:-1])
    b = dat[3].split('x')
    w = int(b[0])
    h = int(b[1])
    return index, (x,y), (w,h)

def main():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    claims = defaultdict(lambda: [])
    for index, start, dimens in data:
        for i in range(dimens[0]):
            for j in range(dimens[1]):
                x = start[0]+i
                y = start[1]+j
                claims[(x,y)].append(index)

    count = 0
    for c in claims:
        if len(claims[c]) > 1:
            count += 1
    # print(claims)
    print(count)

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    claims = defaultdict(lambda: [])
    for index, start, dimens in data:
        for i in range(dimens[0]):
            for j in range(dimens[1]):
                x = start[0]+i
                y = start[1]+j
                claims[(x,y)].append(index)

    overlapping = set()
    all_indexes = set()
    for c in claims:
        all_indexes = all_indexes.union(claims[c])
        if len(claims[c]) > 1:
            overlapping = overlapping.union(set(claims[c]))
    # print(claims)
    # print(count)
    print(all_indexes - overlapping)

if __name__ == '__main__':
    main()
    main2()
