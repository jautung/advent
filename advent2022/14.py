import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '14_dat.txt'
IS_PART_2 = False

def main():
    data = readlines(FILENAME)
    data = [[[int(x) for x in i.split(',')] for i in dat.split(' -> ')] for dat in data]
    
    horz_segments = []
    vert_segments = []
    max_y = None
    for dat in data:
        for i in range(len(dat)-1):
            seg = dat[i:i+2]
            if max_y == None or max(seg[0][1], seg[1][1]) > max_y:
                max_y = max(seg[0][1], seg[1][1])
            if seg[0][0] == seg[1][0]:
                vert_segments.append(seg)
            elif seg[0][1] == seg[1][1]:
                horz_segments.append(seg)
            else:
                assert(False)
    # print(max_y)
    # print_2d(horz_segments)
    # print_2d(vert_segments)

    # for i in range(494, 504):
    #     for j in range(0, 10):
    #         # print(i,j,is_rock((i,j), horz_segments, vert_segments))
    #         if (i,j) == (500,0):
    #             print('+', end='')
    #         elif is_rock((i,j), horz_segments, vert_segments):
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print('\n', end='')
    # print()
    curr_sands = set()
    while True:
        # print(len(curr_sands))
        resting_place = find_rest(curr_sands, max_y, horz_segments, vert_segments)
        # print(resting_place)
        if resting_place == None:
            print(len(curr_sands))
            return
        curr_sands.add(resting_place)
        if resting_place == (500,0):
            print(len(curr_sands))
            return

def find_rest(curr_sands, max_y, horz_segments, vert_segments):
    sand_pos = (500,0)
    while True:
        new_sand_pos = simulate_step(sand_pos, curr_sands, max_y, horz_segments, vert_segments)
        # print(new_sand_pos)
        if new_sand_pos == sand_pos:
            return sand_pos
        if not IS_PART_2:
            if new_sand_pos[1] > max_y:
                return None # free fallin'
        else:
            if new_sand_pos[1] > max_y + 2:
                return None # free fallin'
        sand_pos = new_sand_pos

def simulate_step(sand_pos, curr_sands, max_y, horz_segments, vert_segments):
    next_poses = [
        (sand_pos[0],sand_pos[1]+1),
        (sand_pos[0]-1,sand_pos[1]+1),
        (sand_pos[0]+1,sand_pos[1]+1),
    ]
    for next_pos in next_poses:
        if not is_occupied(next_pos, curr_sands, max_y, horz_segments, vert_segments):
            return next_pos
    return sand_pos

def is_occupied(pos, curr_sands, max_y, horz_segments, vert_segments):
    return is_rock(pos, max_y, horz_segments, vert_segments) or pos in curr_sands

def is_rock(pos, max_y, horz_segments, vert_segments):
    if IS_PART_2 and pos[1] == max_y + 2:
        return True
    for horz_segment in horz_segments:
        if in_horz_segment(pos, horz_segment):
            return True
    for vert_segment in vert_segments:
        if in_vert_segment(pos, vert_segment):
            return True
    return False

def in_horz_segment(pos, seg):
    x, y = pos
    return y == seg[0][1] and min(seg[0][0],seg[1][0]) <= x and x <= max(seg[0][0],seg[1][0])

def in_vert_segment(pos, seg):
    x, y = pos
    return x == seg[0][0] and min(seg[0][1],seg[1][1]) <= y and y <= max(seg[0][1],seg[1][1])

def main2():
    data = readlines(FILENAME)
    data = [[[int(x) for x in i.split(',')] for i in dat.split(' -> ')] for dat in data]
    
    horz_segments = []
    vert_segments = []
    max_y = None
    for dat in data:
        for i in range(len(dat)-1):
            seg = dat[i:i+2]
            if max_y == None or max(seg[0][1], seg[1][1]) > max_y:
                max_y = max(seg[0][1], seg[1][1])
            if seg[0][0] == seg[1][0]:
                vert_segments.append(seg)
            elif seg[0][1] == seg[1][1]:
                horz_segments.append(seg)
            else:
                assert(False)

    count = 0
    mapper = dict()
    mapper[(500,0)] = 'o'
    count += 1
    for y in range(1,max_y+2):
        for x in range(500-y,500+y+1):
            if is_rock((x, y), max_y, horz_segments, vert_segments):
                mapper[(x, y)] = '#'
                continue
            top_three = [
                (x-1,y-1),
                (x,y-1),
                (x+1,y-1),
            ]
            can_reach = [mapper[pos] if pos in mapper else None for pos in top_three]
            if 'o' in can_reach:
                mapper[(x, y)] = 'o'
                count += 1
            else:
                mapper[(x, y)] = '.'
    print(count)

if __name__ == '__main__':
    main()
    main2()
