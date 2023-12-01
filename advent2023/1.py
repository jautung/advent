import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '1_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [read(dat) for dat in data]
    # print(data)
    print(sum(data))

def read(dat):
    tot = []
    for c in dat:
        try:
            x = int(c)
            tot += [x]
        except:
            pass
    return 10 * tot[0] + tot[-1]
    

def main2():
    data = readlines(FILENAME)
    data = [read2(dat) for dat in data]
    # print(data)
    print(sum(data))

NUMS = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def read2(dat):
    idx_map = []
    for key in NUMS:
        x = dat.find(key)
        if x != -1:
            idx_map += [(NUMS[key], x,)]
    # print(idx_map)
    idx_map.sort(key=lambda x: x[1])
    # print(idx_map)
    # print(idx_map[0][0])
    
    idx_map2 = []
    for key in NUMS:
        x = dat.rfind(key)
        if x != -1:
            idx_map2 += [(NUMS[key], x,)]
    # print(idx_map2)
    idx_map2.sort(key=lambda x: x[1], reverse=True)
    # print(idx_map2)
    # print(idx_map2[0][0])
    
    c = 10 * idx_map[0][0] + idx_map2[0][0]
    # print(c)
    return c

if __name__ == '__main__':
    # main()
    main2()
