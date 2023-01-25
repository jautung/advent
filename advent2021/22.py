import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '22_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [parse(dat.split()) for dat in data]
    # print_2d(data)
    # on/off, x, y, z
    def get_final_on_state(x,y,z):
        for dat in reversed(data):
            if in_range(x,dat[1]) and in_range(y,dat[2]) and in_range(z,dat[3]):
                return dat[0]
        return 'off' # initial

    count = 0
    for i in range(-50, 51):
        for j in range(-50, 51):
            for k in range(-50, 51):
                if get_final_on_state(i,j,k) == 'on':
                    count += 1
    print(count)

def in_range(i, rge):
    return i >= rge[0] and i <= rge[1]

def parse(dat):
    # print(dat[0])
    # print([x[2:].split('..') for x in dat[1].split(',')])
    return [dat[0]] + [[int(i) for i in x[2:].split('..')] for x in dat[1].split(',')]

# TIME: 9:35

def main2():
    data = readlines(FILENAME)
    data = [parse(dat.split()) for dat in data]
    # print_2d(data)

    # def get_final_on_state(x,y,z):
    #     for dat in reversed(data):
    #         if in_range(x,dat[1]) and in_range(y,dat[2]) and in_range(z,dat[3]):
    #             return dat[0]
    #     return 'off' # initial

    # on_ranges = []
    # for dat in data:
    #     print('a')
    #     new_on_ranges = []
    #     for old_on_range in on_ranges:
    #         new_on_ranges += combine_range(dat[0], old_on_range, dat[1:])
    #         print_2d('new_on_ranges')
    #     on_ranges = new_on_ranges
    # print_2d(on_ranges)
    xs = set()
    ys = set()
    zs = set()
    for dat in data:
        # range STARTS
        xs.add(dat[1][0])
        # xs.add(dat[1][0]-1)
        # xs.add(dat[1][1])
        xs.add(dat[1][1]+1)
        ys.add(dat[2][0])
        # ys.add(dat[2][0]-1)
        # ys.add(dat[2][1])
        ys.add(dat[2][1]+1)
        zs.add(dat[3][0])
        # zs.add(dat[3][0]-1)
        # zs.add(dat[3][1])
        zs.add(dat[3][1]+1)
    # print(len(xs))
    # print(len(ys))
    # print(len(zs))
    x_ranges = get_ranges(xs)
    y_ranges = get_ranges(ys)
    z_ranges = get_ranges(zs)
    # count = 0
    # for idx, x_range in enumerate(x_ranges):
    #     print(idx, 'of', len(x_ranges))
    #     for y_range in y_ranges:
    #         for z_range in z_ranges:
    #             if get_final_on_state(x_range[0],y_range[0],z_range[0]) == 'on':
    #                 count += range_size(x_range) * range_size(y_range) * range_size(z_range)
    # print(count)

    results_to_find = len(x_ranges) * len(y_ranges) * len(z_ranges)
    # print('s', len(x_ranges), len(y_ranges), len(z_ranges))
    # result = [[[None for k in range(len(z_ranges))] for j in range(len(y_ranges))] for i in range(len(x_ranges))]
    results = set()
    step = 0
    count = 0
    # print('s')
    for dat in reversed(data):
        # print(step)
        x_range_s_index = get_start_range_index(dat[1][0], x_ranges)
        x_range_e_index = get_end_range_index(dat[1][1], x_ranges)
        y_range_s_index = get_start_range_index(dat[2][0], y_ranges)
        y_range_e_index = get_end_range_index(dat[2][1], y_ranges)
        z_range_s_index = get_start_range_index(dat[3][0], z_ranges)
        z_range_e_index = get_end_range_index(dat[3][1], z_ranges)
        # print(x_range_s_index, x_range_e_index, y_range_s_index, y_range_e_index, z_range_s_index, z_range_e_index)
        for i in range(x_range_s_index, x_range_e_index+1):
            for j in range(y_range_s_index, y_range_e_index+1):
                for k in range(z_range_s_index, z_range_e_index+1):
                    if (i,j,k) in results:
                        continue
                    results.add((i,j,k))
                    if dat[0] == 'on':
                        count += range_size(x_ranges[i]) * range_size(y_ranges[j]) * range_size(z_ranges[k])
        if len(results) == results_to_find:
            break
        step += 1
        # if in_range(x,dat[1]) and in_range(y,dat[2]) and in_range(z,dat[3]):
        #     return dat[0]
    print(count)

def get_ranges(lst):
    lst = sorted(list(lst))
    # print(lst)
    ugh = [lst[i:i+2] for i in range(0, len(lst)-2+1)]
    return [[i[0], i[1]-1] for i in ugh]

def range_size(tup):
    return tup[1]-tup[0]+1

def get_start_range_index(s, ranges, offset=0):
    # print(s, ranges)
    if len(ranges) == 0:
        assert(False)
    if len(ranges) == 1:
        assert(ranges[0][0] == s)
        return offset
    mid_index = len(ranges)//2
    # print(mid_index, len(ranges))
    if ranges[mid_index][0] == s:
        return offset + mid_index
    elif ranges[mid_index][0] > s:
        return get_start_range_index(s, ranges[:mid_index], offset=offset)
    elif ranges[mid_index][0] < s:
        return get_start_range_index(s, ranges[mid_index+1:], offset=offset+mid_index+1)

def get_end_range_index(e, ranges, offset=0):
    if len(ranges) == 0:
        assert(False)
    if len(ranges) == 1:
        assert(ranges[0][1] == e)
        return offset
    mid_index = len(ranges)//2
    if ranges[mid_index][1] == e:
        return offset + mid_index
    elif ranges[mid_index][1] > e:
        return get_end_range_index(e, ranges[:mid_index], offset=offset)
    elif ranges[mid_index][1] < e:
        return get_end_range_index(e, ranges[mid_index+1:], offset=offset+mid_index+1)

# def combine_range(on_off, old_on_range, new_range):
#     if on_off == 'on':
#         return [old_on_range, new_range]
#     else:
#         return [old_on_range, new_range]

# TIME: 1:25:48 -- this actually took like ~5 minutes to run but I can't be bothered to think of a better optimization

if __name__ == '__main__':
    main()
    main2()
