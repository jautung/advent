import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    fresh = [[int(y) for y in x.split('-')] for x in data[0]]
    avail = [int(x) for x in data[1]]
    # print(fresh)
    # print(avail)

    def is_fresh(n):
        for f in fresh:
            if n >= f[0] and n <= f[1]:
                return True
        return False

    count = 0
    for a in avail:
        if is_fresh(a):
            count += 1
    print(count)

def maybe_merge(r_1, r_2):
    if r_1[0] <= r_2[0] and r_1[1] >= r_2[1]:
        return r_1
    if r_2[0] <= r_1[0] and r_2[1] >= r_1[1]:
        return r_2
    if r_1[1] >= r_2[0] and r_1[0] <= r_2[0]:
        return [r_1[0], r_2[1]]
    if r_2[1] >= r_1[0] and r_2[0] <= r_1[0]:
        return [r_2[0], r_1[1]]
    return None

def add_to_merged(new_range, all_ranges):
    for index, r in enumerate(all_ranges):
        merged = maybe_merge(new_range, r)
        if merged is not None:
            return add_to_merged(merged, all_ranges[:index] + all_ranges[index+1:])
    return all_ranges + [new_range]

def main2():
    data = readlines_split_by_newlines(FILENAME)
    fresh = [[int(y) for y in x.split('-')] for x in data[0]]

    merged = []
    for f in fresh:
        merged = add_to_merged(f, merged)
        # print(f, merged)
    c = 0
    for m in merged:
        c += m[1] - m[0] + 1
    print(c)

if __name__ == '__main__':
    main()
    main2()
