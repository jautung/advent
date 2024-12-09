import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)
    rows = []
    for d in data:
        rows.append([int(d[0][:-1]), [int(x) for x in d[1:]]])
    # print_2d(rows)

    def can_make(target, seq):
        possibilities_at_each_index = [set([seq[0]])]
        for i in range(1, len(seq)):
            prev_lst = possibilities_at_each_index[i-1]
            new_set = set()
            for p in prev_lst:
                new_set.add(p * seq[i])
                new_set.add(p + seq[i])
            possibilities_at_each_index.append(new_set)
        return target in possibilities_at_each_index[-1]

    res = 0
    for r in rows:
        target = r[0]
        seq = r[1]
        if can_make(target, seq):
            res += target
    print(res)


def main2():
    data = readlines_split_each_line(FILENAME)
    rows = []
    for d in data:
        rows.append([int(d[0][:-1]), [int(x) for x in d[1:]]])
    # print_2d(rows)

    def can_make(target, seq):
        possibilities_at_each_index = [set([seq[0]])]
        for i in range(1, len(seq)):
            prev_lst = possibilities_at_each_index[i-1]
            new_set = set()
            for p in prev_lst:
                new_set.add(p * seq[i])
                new_set.add(p + seq[i])
                new_set.add(int(f"{str(p)}{str(seq[i])}"))
            possibilities_at_each_index.append(new_set)
        return target in possibilities_at_each_index[-1]

    res = 0
    for r in rows:
        target = r[0]
        seq = r[1]
        if can_make(target, seq):
            res += target
    print(res)


if __name__ == '__main__':
    main()
    main2()
