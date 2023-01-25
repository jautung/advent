import sys 
sys.path.append('..')

import copy
import heapq
import math
import re
from collections import defaultdict
from helper import *

FILENAME = '19_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    starter = data[1][0]
    rules = [dat.split(' => ') for dat in data[0]]
    # print_2d(rules)
    # print(starter)
    
    all_possible = set()
    for rule in rules:
        all_possible = all_possible.union(apply_rule(starter, rule))
    print(len(all_possible))

def apply_rule(s, rule):
    res = set()
    idxs = [m.start() for m in re.finditer(rule[0], s)]
    for i in idxs:
        res.add(s[:i] + rule[1] + s[i+len(rule[0]):])
    return res
    # a = starter.find(rules[0][0])
    # print(a)

def main2():
    data = readlines_split_by_newlines(FILENAME)
    starter = data[1][0]
    rules = [dat.split(' => ') for dat in data[0]]
    # print_2d(rules)
    # print(starter)
    
    target_str = starter

    # A* search
    LEN_TARGET = len(target_str)
    MAX_LEN_TRANSFORM = max([len(rule[1]) for rule in rules])
    paths = [(math.ceil((LEN_TARGET - len('e')) / (MAX_LEN_TRANSFORM - 1)), 0, 'e')]
    heapq.heapify(paths)
    added_to_paths = set(['e'])
    while True:
        curr_f_cost, curr_g_cost, curr_str = heapq.heappop(paths)
        print(len(paths), curr_g_cost, curr_str)
        # print(curr_str, paths)
        if len(curr_str) > len(target_str): # quick trim
            continue
        all_possible = set()
        for rule in rules:
            all_possible = all_possible.union(apply_rule(curr_str, rule))
        # print(all_possible)
        for next_str in all_possible:
            if next_str == target_str:
                # print('FOUND IT!')
                print(curr_g_cost+1)
                return
            if next_str in added_to_paths:
                continue
            new_g_cost = curr_g_cost+1
            new_f_cost = new_g_cost + math.ceil((LEN_TARGET - len(next_str)) / (MAX_LEN_TRANSFORM - 1))
            heapq.heappush(paths, (new_f_cost, new_g_cost, next_str))
            # paths.append((curr_g_cost+1, next_str))
            added_to_paths.add(next_str)

    # data = readlines_split_by_newlines(FILENAME)
    # starter = data[1][0]
    # rules = [dat.split(' => ') for dat in data[0]]
    # # print_2d(rules)
    # # print(starter)
    
    # paths = [(0, 'e')]
    # heapq.heapify(paths)
    # target_str = starter
    # added_to_paths = set(['e'])
    # while True:
    #     curr_cost, curr_str = heapq.heappop(paths)
    #     # print(len(paths), curr_cost, curr_str)
    #     # print(curr_str, paths)
    #     if len(curr_str) > len(target_str): # quick trim
    #         continue
    #     all_possible = set()
    #     for rule in rules:
    #         all_possible = all_possible.union(apply_rule(curr_str, rule))
    #     # print(all_possible)
    #     for next_str in all_possible:
    #         if next_str == target_str:
    #             # print('FOUND IT!')
    #             print(curr_cost+1)
    #             return
    #         if next_str in added_to_paths:
    #             continue
    #         heapq.heappush(paths, (curr_cost+1, next_str))
    #         # paths.append((curr_cost+1, next_str))
    #         added_to_paths.add(next_str)

    # data = readlines_split_by_newlines(FILENAME)
    # starter = data[1][0]
    # rules = [dat.split(' => ') for dat in data[0]]
    # # print_2d(rules)
    # # print(starter)
    
    # target_str = starter

    # paths = [(0, target_str)]
    # heapq.heapify(paths)
    # added_to_paths = set([target_str])
    # while True:
    #     curr_cost, curr_str = heapq.heappop(paths)
    #     # print(len(paths), curr_cost, curr_str)
    #     # print(curr_str, paths)
    #     # if len(curr_str) > len(target_str): # quick trim
    #     #     continue
    #     all_possible = set()
    #     for rule in rules:
    #         all_possible = all_possible.union(apply_rule_2(curr_str, rule))
    #     # print(all_possible)
    #     for next_str in all_possible:
    #         if next_str == 'e':
    #             # print('FOUND IT!')
    #             print(curr_cost+1)
    #             return
    #         if next_str in added_to_paths:
    #             continue
    #         heapq.heappush(paths, (curr_cost+1, next_str))
    #         # paths.append((curr_cost+1, next_str))
    #         added_to_paths.add(next_str)

# def apply_rule_2(s, rule):
#     res = set()
#     idxs = [m.start() for m in re.finditer(rule[1], s)]
#     for i in idxs:
#         res.add(s[:i] + rule[0] + s[i+len(rule[1]):])
#     return res
#     # a = starter.find(rules[0][0])
#     # print(a)

if __name__ == '__main__':
    main()
    main2()
