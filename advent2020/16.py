import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '16_dat.txt'
mapper = {}

def parse_info(line):
    assert(': ' in line)
    splits = line.split(': ')
    assert(len(splits) == 2)
    name = splits[0]
    ranges = splits[1].split(' or ')
    assert(len(ranges) == 2)
    p_ranges = []
    for r in ranges:
        nums = r.split('-')
        assert(len(nums) == 2)
        p_ranges.append((int(nums[0]), int(nums[1])))
    return name, p_ranges

def parse_ticket(line):
    return [int(x) for x in line.split(',')]

def main():
    data = readlines_split_by_newlines(FILENAME)
    infos = [parse_info(i) for i in data[0]]
    yours = parse_ticket(data[1][1])
    nearby = [parse_ticket(x) for x in data[2][1:]]
    # data = [int(dat) for dat in data]
    # print(infos)
    # print(yours)
    # print(nearby)

    count = 0
    for t in nearby:
        # print(t, is_ticket_valid(t, infos))
        # v = is_ticket_valid(t, infos)
        for i in t:
            if not is_val_valid(i, infos):
                # print(i)
                count += i
    print(count)

def is_ticket_valid(tic, infos):
    for i in tic:
        if not is_val_valid(i, infos):
            return False
    return True

def is_val_valid(val, infos):
    for item in infos:
        if is_val_valid_for_info(val, item):
            return True
    return False

def is_val_valid_for_info(val, item):
    _, rangs = item
    for r in rangs:
        if in_range(val, r):
            return True
    return False

def in_range(val, r):
    return val >= r[0] and val <= r[1]

def main2():
    data = readlines_split_by_newlines(FILENAME)
    infos = [parse_info(i) for i in data[0]]
    yours = parse_ticket(data[1][1])
    nearby = [parse_ticket(x) for x in data[2][1:]]
    # data = [int(dat) for dat in data]
    # print(infos)
    # print(yours)
    # print(nearby)

    valid_ticks = []
    for t in nearby:
        v = is_ticket_valid(t, infos)
        if v:
            valid_ticks.append(t)
    # print(valid_ticks)

    # build a table of index vs. names
    # row index = name index (i.e. index in infos)
    # col index = tic value index (i.e. index of values in tic)
    # ultimate goal = one True in every row and col
    # every data point sets some None, or False. False not possible, None _can_ be possible
    # if only one None (non-False) in a row or col, set to True
    # - advanced: technically any 2x2 of Nones mean everything else row/col become False (sudoku logic)
    # if one True somewhere, False-out all the row and cols
    assert(len(infos) == len(yours))
    size = len(infos)
    tab = [[None for _ in range(size)] for _ in range(size)]
    for sample in valid_ticks:
        for row in range(size):
            for col in range(size):
                val = sample[col]
                info = infos[row]
                if not is_val_valid_for_info(val, info):
                    # print('setting false because', val, info, sample, row, col)
                    tab[row][col] = False

    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    # print_2d(tab)
    # iterate(tab)
    while num_trues(tab) != size:
        iterate(tab)
    # print_2d(tab)

    # cool, assume that it is intended standard deduction is enough without advanced sudoku logic

    coords_of_trues = []
    map_of_row_to_col = {}
    for row in range(size):
        for col in range(size):
            if tab[row][col] == True:
                coords_of_trues.append((row, col))
                map_of_row_to_col[row] = col

    tot = 1
    for idx, i in enumerate(infos):
        name, _ = i
        if not name.startswith('departure'):
            continue
        col_idx = map_of_row_to_col[idx]
        my_tick_val = yours[col_idx]
        tot *= my_tick_val
    print(tot)

def iterate(tab):
    iterate_rows(tab)
    iterate_cols(tab)

def iterate_rows(tab):
    for r_idx, r in enumerate(tab):
        if r.count(True) >= 1:
            continue
        if r.count(None) == 1:
            i = r.index(None)
            r[i] = True
            set_all_for_true(tab, r_idx, i)

def iterate_cols(tab):
    for c_idx in range(len(tab)):
        built = [tab[r][c_idx] for r in range(len(tab))]
        if built.count(True) >= 1:
            continue
        if built.count(None) == 1:
            i = built.index(None)
            tab[i][c_idx] = True
            set_all_for_true(tab, i, c_idx)

def set_all_for_true(tab, r, c):
    for r2 in range(len(tab)):
        if r2 == r:
            continue
        assert (tab[r2][c] != True)
        tab[r2][c] = False
    for c2 in range(len(tab)):
        if c2 == c:
            continue
        assert (tab[r][c2] != True)
        tab[r][c2] = False

def num_trues(tab):
    c = 0
    for i in tab:
        for j in i:
            if j:
                c += 1
    return c

if __name__ == '__main__':
    main()
    main2()
