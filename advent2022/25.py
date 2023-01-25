import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '25_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    # for dat in data:
    #     print(dat, from_snafu(dat))
    target = sum([from_snafu(dat) for dat in data])
    # print(target)
    print(to_snafu(target))

def from_snafu(dat):
    accum = 0
    for c in list(dat):
        if c == '2':
            accum += 2
        elif c == '1':
            accum += 1
        elif c == '0':
            accum += 0
        elif c == '-':
            accum -= 1
        elif c == '=':
            accum -= 2
        else:
            assert(False)
        accum *= 5
    return int(accum / 5)

def to_snafu(num):
    accum = []
    while True:
        if num == 0:
            break
        last_place = num%5
        if last_place >= 3:
            last_place -= 5
        accum.append(last_place)
        num -= last_place
        num = int(num/5)
    return ''.join(reversed([str(c) if c >= 0 else '-' if c == -1 else '=' for c in accum]))

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
