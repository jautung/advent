import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[x for x in dat.split(' ') if x] for dat in data]
    dt = transpose(data)
    # print(dt)
    tot = 0
    for x in dt:
        if x[-1] == "+":
            arr = x[:-1]
            res = sum([int(x) for x in arr])
            tot += res
        elif x[-1] == "*":
            arr = x[:-1]
            res = product([int(x) for x in arr])
            tot += res
        else:
            # print(x)
            assert False
    print(tot)

def main2():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print(data)
    # print_2d(data)
    nums = data[:-1]
    ops = data[-1]
    nums_t = list(reversed([int(''.join(x)) if any([c != " " for c in x]) else None for x in transpose(nums)]))
    # print_2d(nums_t)
    sets = []
    builder = []
    for x in nums_t:
        if x is None:
            sets.append(builder)
            builder = []
        else:
            builder.append(x)
    if len(builder) > 0:
        sets.append(builder)
    # print(sets)
    ops_2 = ''.join(ops).split(' ')
    ops_3 = list(reversed([x for x in ops_2 if x != '']))
    # print(ops_3)
    assert(len(sets) == len(ops_3))

    tot = 0
    for k in range(len(sets)):
        if ops_3[k] == "+":
            arr = sets[k]
            res = sum([int(x) for x in arr])
            tot += res
        elif ops_3[k] == "*":
            arr = sets[k]
            res = product([int(x) for x in arr])
            tot += res
        else:
            # print(x)
            assert False
    print(tot)

if __name__ == '__main__':
    main()
    main2()
