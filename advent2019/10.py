import math
import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '10_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    asters = set()
    for rIdx, row in enumerate(data):
        for cIdx, char in enumerate(row):
            if char == '#':
                asters.add((rIdx, cIdx))
    # print(asters)

    all_numbers = []
    for candidate_location in asters:
        all_relative_locs = [sub_tup(x, candidate_location) for x in asters if x != candidate_location]
        all_dirs = set([normalize(x) for x in all_relative_locs])
        all_numbers.append(len(all_dirs))
        # print(candidate_location, ':', len(all_dirs), '|||', all_dirs)
    print(max(all_numbers))

def normalize(tuppy):
    gc = math.gcd(tuppy[0], tuppy[1])
    return (tuppy[0] // gc, tuppy[1] // gc)

def main2():
    data = readlines(FILENAME)
    asters = set()
    for rIdx, row in enumerate(data):
        for cIdx, char in enumerate(row):
            if char == '#':
                asters.add((rIdx, cIdx))
    # print(asters)

    all_numbers = []
    for candidate_location in asters:
        all_relative_locs = [sub_tup(x, candidate_location) for x in asters if x != candidate_location]
        all_dirs = set([normalize(x) for x in all_relative_locs])
        all_numbers.append((len(all_dirs), candidate_location))
        # print(candidate_location, ':', len(all_dirs), '|||', all_dirs)
    all_numbers.sort(reverse=True)
    # print(all_numbers[0])

    starting_station = all_numbers[0][1]
    all_relatives_by_norm = dict()
    for other_aster in asters:
        if other_aster == starting_station:
            continue
        relative = sub_tup(other_aster, starting_station)
        key = normalize(relative)
        if key in all_relatives_by_norm:
            all_relatives_by_norm[key].append((relative, other_aster))
        else:
            all_relatives_by_norm[key] = [(relative, other_aster)]
        
    for key in all_relatives_by_norm:
        # sort by distance
        all_relatives_by_norm[key].sort(key=lambda item: item[0][0] ** 2 + item[0][1] ** 2)
    # print(all_relatives_by_norm)
    
    tops = [x for x in all_relatives_by_norm.keys() if x[0] < 0 and x[1] == 0]
    top_rights = [x for x in all_relatives_by_norm.keys() if x[0] < 0 and x[1] > 0]
    rights = [x for x in all_relatives_by_norm.keys() if x[0] == 0 and x[1] > 0]
    bot_rights = [x for x in all_relatives_by_norm.keys() if x[0] > 0 and x[1] > 0]
    bots = [x for x in all_relatives_by_norm.keys() if x[0] > 0 and x[1] == 0]
    bot_lefts = [x for x in all_relatives_by_norm.keys() if x[0] > 0 and x[1] < 0]
    lefts = [x for x in all_relatives_by_norm.keys() if x[0] == 0 and x[1] < 0]
    top_lefts = [x for x in all_relatives_by_norm.keys() if x[0] < 0 and x[1] < 0]

    assert len(tops) <= 1
    assert len(rights) <= 1
    assert len(bots) <= 1
    assert len(lefts) <= 1

    top_rights.sort(key=lambda x: x[0] / x[1])
    bot_rights.sort(key=lambda x: x[0] / x[1])
    bot_lefts.sort(key=lambda x: x[0] / x[1])
    top_lefts.sort(key=lambda x: x[0] / x[1])

    all_in_order = tops + top_rights + rights + bot_rights + bots + bot_lefts + lefts + top_lefts
    # print(all_in_order)

    idx_of_all_in_order = 0
    full_ordering = []
    while len(full_ordering) != len(asters) - 1:
        curr_norm = all_in_order[idx_of_all_in_order]
        assert curr_norm in all_relatives_by_norm
        curr_candidates = all_relatives_by_norm[curr_norm]
        if len(curr_candidates) > 0:
            full_ordering.append(all_relatives_by_norm[curr_norm].pop(0))
        idx_of_all_in_order = (idx_of_all_in_order + 1) % len(all_in_order)

    extraction = [x[1] for x in full_ordering]
    # print(extraction)

    # nice visualization :)
    # for rIdx, row in enumerate(data):
    #     for cIdx, char in enumerate(row):
    #         if char == '#':
    #             assert (rIdx, cIdx) in extraction or (rIdx, cIdx) == starting_station
    #             # print(char, end="")
    #             if (rIdx, cIdx) == starting_station:
    #                 print(f'{"M":>2} ', end="")
    #             else:
    #                 print(f"{extraction.index((rIdx, cIdx)) + 1:>2} ", end="")
    #         else:
    #             print(f"{char:>2} ", end="")
    #     print()

    ans = extraction[200-1]
    print(ans[0] + ans[1] * 100)

if __name__ == '__main__':
    main()
    main2()
