import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '14_dat.txt'
mapper = {}

def parse(dat):
    return dat[0], int(dat[3]), int(dat[6]), int(dat[13])

def main():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]

    # print_2d(data)
    TIME = 2503
    # TIME = 1000
    res = [(dist_for_time(TIME, speed, fly_time, rest_time), name) for name, speed, fly_time, rest_time in data]
    # print_2d(res)
    print_2d(sorted(res))

def dist_for_time(t, speed, fly_time, rest_time):
    full_blocks = t // (fly_time + rest_time)
    last_block = t % (fly_time + rest_time)
    last_block_fly_time = min(fly_time, last_block)
    return full_blocks * fly_time * speed + last_block_fly_time * speed

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]

    # print_2d(data)
    TIME = 2503
    # TIME = 1000
    scores = def_dict(0)
    for t in range(1, TIME+1):
        res = [(dist_for_time(t, speed, fly_time, rest_time), name) for name, speed, fly_time, rest_time in data]
        best_dist = max([r[0] for r in res])
        for r in res:
            if r[0] == best_dist:
                scores[r[1]] += 1
    print(scores)

if __name__ == '__main__':
    main()
    main2()
