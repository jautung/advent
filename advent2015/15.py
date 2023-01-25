import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '15_dat.txt'
mapper = {}


def main():
    data = readlines_split_each_line(FILENAME)

    lookup = dict()
    def parse(dat):
        lookup[dat[0][:-1]] = (int(dat[2][:-1]), int(dat[4][:-1]), int(dat[6][:-1]), int(dat[8][:-1]), int(dat[10]))
        return dat[0][:-1], int(dat[2][:-1]), int(dat[4][:-1]), int(dat[6][:-1]), int(dat[8][:-1]), int(dat[10])

    data = [parse(dat) for dat in data]
    # print(lookup)
    
    # for dat in data:
    #     name, capacity, durability, flavor, texture, calories = dat
    #     print(name, capacity, durability, flavor, texture, calories)
    # # print_2d(data)

    TEASPOONS_LEFT = 100

    mapping = dict()
    ingrs = [dat[0] for dat in data]
    global best_score
    best_score = None

    def fill_map(curr_mapping, ingrs_left, spoons_left):
        if len(ingrs_left) == 1:
            curr_mapping[ingrs_left[0]] = spoons_left
            # print(curr_mapping, score(curr_mapping), best_score)
            curr_score = score(curr_mapping)
            global best_score
            # print(best_score)
            if best_score == None or curr_score > best_score:
                best_score = curr_score
            return
        else:
            for i in range(0, spoons_left+1):
                curr_mapping[ingrs_left[0]] = i
                fill_map(curr_mapping, ingrs_left[1:], spoons_left - i)

    def score(mapping):
        qual_mult = 1
        for qual in range(4):
            qual_tot = 0
            for item in mapping:
                # print(lookup[item])
                qual_tot += mapping[item] * lookup[item][qual]
            # print(qual, qual_tot)
            qual_mult *= max(0, qual_tot)
        return qual_mult

    fill_map(mapping, ingrs, TEASPOONS_LEFT)

    print(best_score)

def main2():
    data = readlines_split_each_line(FILENAME)

    lookup = dict()
    def parse(dat):
        lookup[dat[0][:-1]] = (int(dat[2][:-1]), int(dat[4][:-1]), int(dat[6][:-1]), int(dat[8][:-1]), int(dat[10]))
        return dat[0][:-1], int(dat[2][:-1]), int(dat[4][:-1]), int(dat[6][:-1]), int(dat[8][:-1]), int(dat[10])

    data = [parse(dat) for dat in data]
    # print(lookup)
    
    # for dat in data:
    #     name, capacity, durability, flavor, texture, calories = dat
    #     print(name, capacity, durability, flavor, texture, calories)
    # # print_2d(data)

    TEASPOONS_LEFT = 100

    mapping = dict()
    ingrs = [dat[0] for dat in data]
    global best_score
    best_score = None

    def fill_map(curr_mapping, ingrs_left, spoons_left):
        if len(ingrs_left) == 1:
            curr_mapping[ingrs_left[0]] = spoons_left
            # print(curr_mapping, score(curr_mapping), best_score)
            curr_score = score(curr_mapping)
            global best_score
            # print(best_score)
            if best_score == None or curr_score > best_score:
                best_score = curr_score
            return
        else:
            for i in range(0, spoons_left+1):
                curr_mapping[ingrs_left[0]] = i
                fill_map(curr_mapping, ingrs_left[1:], spoons_left - i)

    def score(mapping):
        calorie_tot = 0
        for item in mapping:
            calorie_tot += mapping[item] * lookup[item][4]
        if calorie_tot != 500:
            return 0

        qual_mult = 1
        for qual in range(4):
            qual_tot = 0
            for item in mapping:
                # print(lookup[item])
                qual_tot += mapping[item] * lookup[item][qual]
            # print(qual, qual_tot)
            qual_mult *= max(0, qual_tot)
        return qual_mult

    fill_map(mapping, ingrs, TEASPOONS_LEFT)

    print(best_score)

if __name__ == '__main__':
    main()
    main2()
