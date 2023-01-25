import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '16_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)

    info = dict()
    def parse(dat):
        new_map = dict()
        for i in range(2, len(dat), 2):
            new_map[dat[i][:-1]] = int(dat[i+1].strip(','))
        info[dat[1][:-1]] = new_map

    data = [parse(dat) for dat in data]
    # print(data)
    # for i in info:
    #     print(i, info[i])

    concrete = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    def matches(partial, concrete):
        for i in partial:
            if partial[i] != concrete[i]:
                return False
        return True

    for i in info:
        if matches(info[i], concrete):
            print('FOUND IT!')
            print(i)
        # print(i, info[i])

def main2():
    data = readlines_split_each_line(FILENAME)

    info = dict()
    def parse(dat):
        new_map = dict()
        for i in range(2, len(dat), 2):
            new_map[dat[i][:-1]] = int(dat[i+1].strip(','))
        info[dat[1][:-1]] = new_map

    data = [parse(dat) for dat in data]
    # print(data)
    # for i in info:
    #     print(i, info[i])

    concrete = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    def matches(partial, concrete):
        for i in partial:
            if i == 'cats' or i == 'trees':
                if partial[i] <= concrete[i]:
                    return False
            elif i == 'pomeranians' or i == 'goldfish':
                if partial[i] >= concrete[i]:
                    return False
            else:
                if partial[i] != concrete[i]:
                    return False
        return True

    for i in info:
        if matches(info[i], concrete):
            print('FOUND IT!')
            print(i)
        # print(i, info[i])

if __name__ == '__main__':
    main()
    main2()
