import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '18_dat.txt'

def main():
    data = readlines(FILENAME)
    running_sum = data[0]
    for i in range(1, len(data)):
        new = data[i]
        running_sum = snail_reduce_full('[' + running_sum + ',' + new + ']')
    # print(running_sum)
    # snail = snail_reduce_full('[11,1]')
    # print('final', snail)
    print(magnitude(running_sum))

def snail_reduce_full(snail):
    while True:
        # print('snail_reduce_full_iter', snail)
        snail, updated = snail_reduce(snail)
        if not updated:
            break
    return snail

def snail_reduce(snail):
    snail, updated = explode(snail)
    if updated:
        return snail, updated
    snail, updated = split(snail)
    if updated:
        return snail, updated
    return snail, False

def explode(snail):
    depth = 0
    for i, char in enumerate(snail):
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        if depth == 5:
            for j in range(i, len(snail)):
                if snail[j] == ']':
                    break
            exploded = snail[i:j+1]
            exploded_ints = [int(i) for i in exploded[1:-1].split(',')]
            exploded_left = exploded_ints[0]
            exploded_right = exploded_ints[1]
            # print(exploded_left, exploded_right)

            left_snail_end = None
            left_snail_start = None
            for left_snail_traveler in range(i-1, -1, -1):
                if is_number(snail[left_snail_traveler]):
                    if not left_snail_end:
                        left_snail_end = left_snail_traveler+1
                else:
                    if left_snail_end:
                        left_snail_start = left_snail_traveler+1
                        break
            if left_snail_start and left_snail_end:
                left_snail = snail[left_snail_start:left_snail_end]
                new_left_snail = snail[:left_snail_start] + str(int(left_snail) + exploded_left) + snail[left_snail_end:i]
                # print('left_snail', left_snail_start, left_snail_end, snail[left_snail_start:left_snail_end])
            else:
                new_left_snail = snail[:i]

            right_snail_start = None
            right_snail_end = None
            for right_snail_traveler in range(j+1, len(snail)):
                if is_number(snail[right_snail_traveler]):
                    if not right_snail_start:
                        right_snail_start = right_snail_traveler
                else:
                    if right_snail_start:
                        right_snail_end = right_snail_traveler
                        break
            if right_snail_start and right_snail_end:
                right_snail = snail[right_snail_start:right_snail_end]
                # print('a', right_snail_start, right_snail_end, right_snail)
                new_right_snail = snail[j+1:right_snail_start] + str(int(right_snail) + exploded_right) + snail[right_snail_end:]
            else:
                new_right_snail = snail[j+1:]

            new_snail = new_left_snail + '0' + new_right_snail

            return new_snail, True
    return snail, False

def is_number(chr):
    return chr != '[' and chr != ']' and chr != ','

def split(snail):
    snail_start = None
    snail_end = None
    for snail_traveler in range(len(snail)):
        if is_number(snail[snail_traveler]):
            if not snail_start:
                snail_start = snail_traveler
        else:
            if snail_start:
                snail_end = snail_traveler
                if int(snail[snail_start:snail_end]) < 10:
                    snail_start = None
                    snail_end = None
                    continue
                else:
                    break
    if snail_start and snail_end:
        splitter = int(snail[snail_start:snail_end])
        left = splitter // 2
        right = splitter - left
        return snail[:snail_start] + '[' + str(left) + ',' + str(right) + ']' + snail[snail_end:], True
        # print('a', int(snail[snail_start:snail_end]))
    return snail, False

def magnitude(snail):
    if snail[0] == '[' and snail[-1] == ']':
        depth = 0
        for i, char in enumerate(snail):
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            elif char == ',' and depth == 1:
                return 3 * magnitude(snail[1:i]) + 2 * magnitude(snail[i+1:-1])
    else:
        return int(snail)

# Time: 36:15 -- ok yea this is second time but no need for trees

def main2():
    data = readlines(FILENAME)
    max_mag = None
    for tree1 in data:
        for tree2 in data:
            mag = magnitude(snail_reduce_full('[' + tree1 + ',' + tree2 + ']'))
            if max_mag == None or mag > max_mag:
                max_mag = mag
    print(max_mag)
    return

# Time: 38:00 -- yea maybe we should have just done the string manipulation route instead of the full fledged trees.. lmao this is faster too!

if __name__ == '__main__':
    main()
    main2()
