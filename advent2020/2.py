import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {}

def parse(dat):
    r = dat[0]
    sr = int(r.split('-')[0])
    er = int(r.split('-')[1])
    letter = dat[1][:-1]
    cand = dat[2]
    return ((sr,er),letter,cand)

def main():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    valids = 0
    for r, letter, cand in data:
        # print(cand, cand.count(letter))
        actual = cand.count(letter)
        if actual >= r[0] and actual <= r[1]:
            valids += 1
    print(valids)

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    valids = 0
    for r, letter, cand in data:
        ra, rb = r
        if cand[ra-1] == letter and cand[rb-1] != letter:
            valids += 1
        elif cand[ra-1] != letter and cand[rb-1] == letter:
            valids += 1

    print(valids)

if __name__ == '__main__':
    main()
    main2()
