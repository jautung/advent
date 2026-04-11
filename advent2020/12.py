import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '12_dat.txt'
mapper = {}

def parse(l):
    return l[0], int(l[1:])

DIRS = 'NESW' # clockwise, i.e 'R''

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]

    curr = (0,0)
    curr_dir = 1 # index in DIRS
    # print(curr, curr_dir)
    for inst in data:
        curr, curr_dir = apply_inst(curr, curr_dir, inst)
        # print(curr, curr_dir)
    
    # print(curr)
    print(abs(curr[0])+abs(curr[1]))

def apply_inst(pos, dirr, inst):
    a, num = inst
    if a == 'N':
        return add_tup(pos, (0, num)), dirr
    elif a == 'S':
        return add_tup(pos, (0, -num)), dirr
    elif a == 'E':
        return add_tup(pos, (num, 0)), dirr
    elif a == 'W':
        return add_tup(pos, (-num, 0)), dirr
    elif a == 'L':
        assert num % 90 == 0
        move_by = num//90
        return pos, (dirr - move_by) % 4
    elif a == 'R':
        assert num % 90 == 0
        move_by = num//90
        # print(move_by)
        return pos, (dirr + move_by) % 4
    elif a == 'F':
        actual = DIRS[dirr]
        # print(actual)
        return apply_inst(pos, dirr, (actual, num))

def main2():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]

    curr = (0,0)
    waypt = (10,1)
    # print(curr, waypt)
    for inst in data:
        curr, waypt = apply_inst_v2(curr, waypt, inst)
        # print(curr, waypt)
    
    # print(curr)
    print(abs(curr[0])+abs(curr[1]))

def apply_inst_v2(pos, waypt, inst):
    a, num = inst
    if a == 'N':
        return pos, add_tup(waypt, (0, num))
    elif a == 'S':
        return pos, add_tup(waypt, (0, -num))
    elif a == 'E':
        return pos, add_tup(waypt, (num, 0))
    elif a == 'W':
        return pos, add_tup(waypt, (-num, 0))
    elif a == 'L':
        assert num % 90 == 0
        move_by = num//90
        return pos, rotate_by(waypt, move_by % 4)
    elif a == 'R':
        assert num % 90 == 0
        move_by = num//90
        return pos, rotate_by(waypt, (-move_by) % 4)
    elif a == 'F':
        return add_tup(pos, (num * waypt[0], num * waypt[1])), waypt

def rotate_by(pt, num_times):
    if num_times == 0:
        return pt
    elif num_times == 1:
        return (-pt[1], pt[0])
    elif num_times == 2:
        return (-pt[0], -pt[1])
    elif num_times == 3:
        return (pt[1], -pt[0])
    assert False

if __name__ == '__main__':
    main()
    main2()
