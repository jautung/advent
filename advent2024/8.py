import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    emits = dict()
    HEIGHT = len(data)
    WIDTH = len(data[0])
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if data[r][c] != '.':
                if data[r][c] in emits:
                    emits[data[r][c]].append((r,c))
                else:
                    emits[data[r][c]] = [(r,c)]
    # print(emits)

    def get_antis(lst):
        res = set()
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                at_i = lst[i]
                at_j = lst[j]
                res.add((2 * at_i[0] - at_j[0], 2 * at_i[1] - at_j[1]))
                res.add((2 * at_j[0] - at_i[0], 2 * at_j[1] - at_i[1]))
        return res

    all_antis = set()
    for typ in emits:
        lst = emits[typ]
        # print(typ, lst)
        antis_for_lst = get_antis(lst)
        all_antis = all_antis.union(antis_for_lst)
    # print(all_antis)
    # print(len(all_antis))

    inside_antis = set()
    for x in all_antis:
        if x[0] >= 0 and x[1] >= 0 and x[0] < HEIGHT and x[1] < WIDTH:
            inside_antis.add(x)
    # print(inside_antis)
    print(len(inside_antis))


def main2():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    emits = dict()
    HEIGHT = len(data)
    WIDTH = len(data[0])
    initial_counter = set()
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if data[r][c] != '.':
                initial_counter.add((r,c))
                if data[r][c] in emits:
                    emits[data[r][c]].append((r,c))
                else:
                    emits[data[r][c]] = [(r,c)]
    # print(emits)

    def in_bounds(x):
        return x[0] >= 0 and x[1] >= 0 and x[0] < HEIGHT and x[1] < WIDTH

    def get_antis_in_bound(lst):
        res = set()
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                at_i = lst[i]
                at_j = lst[j]
                
                                # from i down
                step = (at_i[0] - at_j[0], at_i[1] - at_j[1])
                test = at_i
                while True:
                    test = add_tup(test, step)
                    # print(test)
                    if not in_bounds(test):
                        break
                    res.add(test)

                # from i down
                step = (at_j[0] - at_i[0], at_j[1] - at_i[1])
                test = at_j
                while True:
                    test = add_tup(test, step)
                    # print(test)
                    if not in_bounds(test):
                        break
                    res.add(test)

                # res.add((2 * at_i[0] - at_j[0], 2 * at_i[1] - at_j[1]))
                # res.add((2 * at_j[0] - at_i[0], 2 * at_j[1] - at_i[1]))
        return res

    all_antis = set()
    for typ in emits:
        lst = emits[typ]
        # print(typ, lst)
        antis_for_lst = get_antis_in_bound(lst)
        all_antis = all_antis.union(antis_for_lst)
    # print(all_antis)
    # print(len(all_antis))
    # print(len(all_antis) + initial_counter)
    print(len(all_antis.union(initial_counter)))

    # inside_antis = set()
    # for x in all_antis:
    #     if x[0] >= 0 and x[1] >= 0 and x[0] < HEIGHT and x[1] < WIDTH:
    #         inside_antis.add(x)
    # # print(inside_antis)
    # print(len(inside_antis))

if __name__ == '__main__':
    main()
    main2()
