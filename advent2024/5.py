from functools import cmp_to_key
import sys 
sys.path.append('..')

import copy
from collections import defaultdict, Counter
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)
    rules = data[0]
    updates = data[1]
    rules = [[int(x) for x in r.split('|')] for r in rules]
    # print(rules)
    updates = [[int(x) for x in r.split(',')] for r in updates]
    # print(updates)
    def is_correct(update, rules):
        for rule in rules:
            first = rule[0]
            sec = rule[1]
            if not first in update or not sec in update:
                continue
            f_index = update.index(first)
            s_index = update.index(sec)
            if f_index >= s_index:
                return False
        return True
    cot = 0
    for update in updates:
        # print(update, is_correct(update, rules))
        if not is_correct(update, rules):
            continue
        # print(update[len(update)//2])
        cot += update[len(update)//2]
    print(cot)



def main2():
    data = readlines_split_by_newlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)
    rules = data[0]
    updates = data[1]
    rules = [[int(x) for x in r.split('|')] for r in rules]
    # print(rules)
    updates = [[int(x) for x in r.split(',')] for r in updates]
    # print(updates)
    def is_correct(update, rules):
        for rule in rules:
            first = rule[0]
            sec = rule[1]
            if not first in update or not sec in update:
                continue
            f_index = update.index(first)
            s_index = update.index(sec)
            if f_index >= s_index:
                return False
        return True
    # def precomp(rules):
    #     counter_all = Counter()
    #     for rule in rules:
    #         first = rule[0]
    #         sec = rule[1]
    #         counter_all[first] += 1
    #         counter_all[sec] += 1
    #     num_of_pages = len(counter_all)
    #     for a in counter_all:
    #         # print(counter_all[a])
    #         assert counter_all[a] == num_of_pages - 1

    #     counter_1 = Counter()
    #     for rule in rules:
    #         first = rule[0]
    #         counter_1[first] += 1

    #     # print(counter_1)
    #     build_upwards_sorted = []
    #     for i in range(num_of_pages):
    #         for c in counter_1:
    #             if counter_1[c] == num_of_pages - i - 1:
    #                 build_upwards_sorted.append(c)
    #                 break
    #     # print(build_upwards_sorted)
    #     # return build_upwards_sorted
    #     # while len(build_upwards_sorted) < num_of_pages:
    #     #     find_earliest_page(rules)

    #     # # do the dumb selection sort
    #     counter_1 = Counter()
    #     counter_2 = Counter()
    #     counter_all = Counter()
        

    #     for rule in rules:
    #         first = rule[0]
    #         sec = rule[1]
    #         counter_1[first] += 1
    #         counter_2[sec] += 1
    #         counter_all[first] += 1
    #         counter_all[sec] += 1
    #     print(counter_1)
    #     print(counter_2)
    #     print(counter_all)
    #     print(len(counter_all))

    def fix(update, rules):
        def custom_comparator(p1, p2):
            for rule in rules:
                if rule[0] == p1 and rule[1] == p2:
                    return -1
                if rule[1] == p1 and rule[0] == p2:
                    return 1
            raise ValueError()
            return 0

        return sorted(update, key=cmp_to_key(custom_comparator))

    # precompute_rules = precomp(rules)
    cot = 0
    for update in updates:
        # print(update, is_correct(update, rules))
        if is_correct(update, rules):
            continue
        # print(update)
        # print(fix(update, rules))
        # print()
        x = fix(update, rules)
        cot += x[len(update)//2]
    print(cot)


if __name__ == '__main__':
    main()
    main2()
