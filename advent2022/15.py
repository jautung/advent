import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '15_dat.txt'
mapper = {}

# https://www.geeksforgeeks.org/merging-intervals/
def mergeIntervals(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
 
    # print("The Merged Intervals are :", end=" ")
    # for i in range(len(stack)):
    #     print(stack[i], end=" ")
    return stack

####

def parse(dat):
    # print(dat[2].split('=')[1][:-1])
    x = int(dat[2].split('=')[1][:-1])
    y = int(dat[3].split('=')[1][:-1])
    cx = int(dat[8].split('=')[1][:-1])
    cy = int(dat[9].split('=')[1])
    return ((x,y),(cx,cy),manhat((x,y),(cx,cy)))

def manhat(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def main():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]

    max_left = None
    max_right = None
    for reading in data:
        cand_left = reading[0][0]-reading[2]
        cand_right = reading[0][0]+reading[2]
        if max_left == None or cand_left < max_left:
            max_left = cand_left
        if max_right == None or cand_right > max_right:
            max_right = cand_right
    # print(max_left, max_right)

    LINE_AT = 2000000
    RANGE_START = max_left - 1
    RANGE_END = max_right + 1

    count = 0
    for x in range(RANGE_START, RANGE_END+1):
        candidate = (x, LINE_AT)
        found_something = False
        for reading in data:
            if candidate == reading[1]:
                # print(x, 'B')
                found_something = True
                break
            dist_to_sensor = manhat(reading[0], candidate)
            if dist_to_sensor <= reading[2]:
                # print(x, 'Cannot exist')
                count += 1
                found_something = True
                break
        if not found_something:
            pass
            # print(x, 'Dunno much')
    print(count)
    # print_2d(data)

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]

    # max_left = None
    # max_right = None
    # for reading in data:
    #     cand_left = reading[0][0]-reading[2]
    #     cand_right = reading[0][0]+reading[2]
    #     if max_left == None or cand_left < max_left:
    #         max_left = cand_left
    #     if max_right == None or cand_right > max_right:
    #         max_right = cand_right
    # # print(max_left, max_right)

    # LINE_AT = 2000000
    # RANGE_START = max_left - 1
    # RANGE_END = max_right + 1

    interval_funcs = [convert_to_intervals(r) for r in data]
    beacon_per_y = defaultdict(lambda: set())
    for r in data:
        beacon_per_y[r[1][1]].add(r[1][0])

    # print(beacon_per_y)
    # test = interval_funcs[0]
    # for y in range(-3, 19):
    #     print(y, test(y))

    RANGE = 4000000
    for y in range(0, RANGE+1):
        # if y % 10000 == 0:
        #     print(y)
        all_intervals_orig = [interval_func(y) for interval_func in interval_funcs]
        all_intervals_orig = list(filter(lambda x: x != None, all_intervals_orig))
        for i in beacon_per_y[y]:
            all_intervals_orig += [[i,i+1]] # right exclusive to merge
        all_intervals = mergeIntervals(all_intervals_orig)
        covered = False
        for i in all_intervals:
            if i[0] <= 0 and i[1] > RANGE:
                covered = True
                break
        if not covered:
            # print(y)
            # print(all_intervals_orig)
            # print(all_intervals)
            for i in all_intervals:
                if i[1] >= 0 and i[1] <= RANGE:
                    # print(i[1])
                    print(i[1]*4000000+y)
                    exit(1)
        # exit(1)

    # count = 0
    # for x in range(0, RANGE+1):
    #     for y in range(0, RANGE+1):
    #         candidate = (x, y)
    #         found_something = False
    #         for reading in data:
    #             if candidate == reading[1]:
    #                 # print(x, 'B')
    #                 found_something = True
    #                 break
    #             dist_to_sensor = manhat(reading[0], candidate)
    #             if dist_to_sensor <= reading[2]:
    #                 # print(x, 'Cannot exist')
    #                 # count += 1
    #                 found_something = True
    #                 break
    #         if not found_something:
    #             # print((x,y))
    #             print(x*4000000+y)
    #             # print(x, 'Dunno much')
    # print(count)
    # print_2d(data)

def convert_to_intervals(reading):
    def lower_upper_given_y(y):
        y_gap = abs(y-reading[0][1])
        if reading[2] < y_gap:
            return None
        return [reading[0][0]-reading[2]+y_gap, reading[0][0]+reading[2]-y_gap+1] # right exclusive to merge
    return lower_upper_given_y

if __name__ == '__main__':
    main()
    main2()
