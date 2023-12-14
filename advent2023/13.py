import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '13_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    # data = [[c for c in] for dat in data]
    inp = [proc(map) for map in data]
    final = 0
    for i in inp:
        # print()
        x = find_row_refl(i)
        # print(x)
        y = find_col_refl(i)
        assert(x != None or y != None)
        if x:
            final += 100 * x
        if y:
            final += y
        # print(y)
    print(final)

def find_col_refl(map):
    return find_row_refl(transpose(map))

def find_row_refl(map):
    for row_i in range(1, len(map)):
        # check if refl line is BEFORE row_i, i.e. between row_i and row_i-1
        is_refl = True
        dist_away = 0
        while True:
            if row_i-1-dist_away < 0:
                break
            if row_i+dist_away >= len(map):
                break
            top = map[row_i-1-dist_away]
            bottom = map[row_i+dist_away]
            if ''.join(top) != ''.join(bottom):
                is_refl = False
                break
            dist_away += 1
        if is_refl:
            return row_i
    return None

def proc(map):
    return [[c for c in x] for x in map]

def main2():
    data = readlines_split_by_newlines(FILENAME)
    # data = [[c for c in] for dat in data]
    inp = [proc(map) for map in data]
    final = 0
    for i in inp:
        # print()
        x = find_row_refl_ob1(i)
        # print(x)
        y = find_col_refl_ob1(i)
        assert(x != None or y != None)
        if x:
            final += 100 * x
        if y:
            final += y
        # print(y)
    print(final)

def find_col_refl_ob1(map):
    return find_row_refl_ob1(transpose(map))

def find_row_refl_ob1(map):
    for row_i in range(1, len(map)):
        # check if refl line is BEFORE row_i, i.e. between row_i and row_i-1
        is_refl = True
        smudge_added = False
        dist_away = 0
        while True:
            if row_i-1-dist_away < 0:
                break
            if row_i+dist_away >= len(map):
                break
            top = map[row_i-1-dist_away]
            bottom = map[row_i+dist_away]
            diff = len([1 for i in range(len(top)) if top[i] != bottom[i]])
            if diff > 1:
                is_refl = False
                break
            if diff == 1:
                if not smudge_added:
                    smudge_added = True
                else:
                    is_refl = False
                    break
            dist_away += 1
        if smudge_added and is_refl:
            return row_i
    return None

if __name__ == '__main__':
    main()
    main2()
