import sys 
sys.path.append('..')

import copy
# import sys
from collections import defaultdict
from helper import *
from sympy import *

FILENAME = '13_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    earliest = int(data[0])
    entries = [int(a) if a != 'x' else 'x' for a in data[1].split(',')]

    # print(earliest)
    # print(entries)

    best_found_time = None
    best_found_entry = None
    for item in entries:
        if item == 'x':
            continue
        next_time = math.ceil(earliest / item) * item
        # print(next_time)
        if best_found_time is None or next_time < best_found_time:
            best_found_time = next_time
            best_found_entry = item
    # print(best_found_time, best_found_entry)
    print((best_found_time - earliest) * best_found_entry)

def main2():
    # sys.setrecursionlimit(9999)

    data = readlines(FILENAME)
    entries = [int(a) if a != 'x' else 'x' for a in data[1].split(',')]

    for item in entries:
        if item == 'x':
            continue
        assert(isprime(item))

    assert(entries[0] != 'x')

    candidate = 0
    curr_multiplier = entries[0]
    for idx, item in enumerate(entries):
        # print(idx, item)
        if idx == 0:
            continue
        if item == 'x':
            continue
        # print(candidate, curr_multiplier)
        candidate = move_until_works(candidate, curr_multiplier, item, idx  % item)
        # print(candidate)
        curr_multiplier *= item

    # print('final:', candidate)
    print(candidate)

def move_until_works(candidate, curr_multiplier, item, idx):
    for _ in range(item+1):
        # print(_, candidate, item, idx)
        offset = (item - candidate % item) % item
        # offset = num_ahead(candidate, item)
        # print(offset)
        # print(idx)
        if offset == idx:
            curr_multiplier *= item
            return candidate
        candidate += curr_multiplier
    assert False

# def num_ahead(candidate, item):
#     next_time = math.ceil(candidate / item) * item
#     assert ((item - candidate % item) % item == next_time - candidate)
#         # print(item - candidate % item, next_time - candidate)
#     return next_time - candidate

if __name__ == '__main__':
    main()
    main2()
