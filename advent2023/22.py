import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '22_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    bricks = [parse(dat) for dat in data]
    bricks.sort(key=lambda brick: min(brick[0][2], brick[1][2]))
    # sorting so that we can go bottom to top
    # print_2d(bricks)
    fixed_bricks, _ = fall_bricks(bricks)
    # print_2d(fixed_bricks)
    print('INITIAL FELL')
    did_not_fall_counter = 0
    actual_fall_counter = 0
    for index, test_poof_brick in enumerate(fixed_bricks):
        print(f"POOFING {index} of {len(fixed_bricks)}")
        poofed = copy.deepcopy([b for b in fixed_bricks if b != test_poof_brick])
        _, fall_counter = fall_bricks(poofed)
        # print(test_poof_brick, did_fall)
        actual_fall_counter += fall_counter
        did_fall = fall_counter > 0
        if not did_fall:
            did_not_fall_counter += 1
        # print_2d(poofed)
    print(did_not_fall_counter)
    print(actual_fall_counter)
        
def fall_bricks(bricks):
    fall_counter = 0
    fixed_bricks = []
    for brick in bricks:
        did_fall = fall_brick(brick, fixed_bricks)
        if did_fall:
            fall_counter += 1
    return fixed_bricks, fall_counter

def fall_brick(brick, fixed_bricks):
    # print(brick, fixed_bricks)
    # print()
    # updates fixed_bricks
    test_brick = copy.deepcopy(brick)
    counter = 0
    while True:
        if on_floor(test_brick):
            fixed_bricks.append(test_brick)
            return counter != 0
        translate_down(test_brick)
        counter += 1
        if any([collide(test_brick, fixed_brick) for fixed_brick in fixed_bricks]):
            translate_up(test_brick)
            counter -= 1
            fixed_bricks.append(test_brick)
            return counter != 0

def translate_down(brick):
    # can probably optimize this more to subtract more, maybe for part 2
    brick[0][2] -= 1
    brick[1][2] -= 1

def translate_up(brick):
    brick[0][2] += 1
    brick[1][2] += 1

def on_floor(brick):
    return brick[0][2] == 1 or brick[1][2] == 1

def collide(brick1, brick2):
    brick_dir_1 = brick_dir(brick1)
    brick_dir_2 = brick_dir(brick2)
    if brick_dir_1 == brick_dir_2:
        for other_brick_dir in [0,1,2]:
            if other_brick_dir == brick_dir_1:
                continue
            if brick1[0][other_brick_dir] != brick2[0][other_brick_dir]:
                return False
        range_1 = sorted([brick1[0][brick_dir_1], brick1[1][brick_dir_1]])
        range_2 = sorted([brick2[0][brick_dir_1], brick2[1][brick_dir_1]])
        if range_1[0] < range_2[0]:
            return range_1[1] >= range_2[0]
        elif range_2[0] < range_1[0]:
            return range_2[1] >= range_1[0]
        else:
            return True
    else:
        third_dir = [i for i in [0,1,2] if i != brick_dir_1 and i != brick_dir_2][0]
        if brick1[0][third_dir] != brick2[0][third_dir]:
            return False
        # potential_intersection is
        # follow brick 2 in brick_dir_1
        # follow brick 1 in brick_dir_2
        # they have to be the same in third_dir
        return in_range(brick2[0][brick_dir_1], sorted([brick1[0][brick_dir_1], brick1[1][brick_dir_1]])) \
            and in_range(brick1[0][brick_dir_2], sorted([brick2[0][brick_dir_2], brick2[1][brick_dir_2]]))

def in_range(a, s_and_e):
    s, e = s_and_e
    return s <= a and a <= e

def brick_dir(brick):
    s = brick[0]
    e = brick[1]
    if s[0] == e[0] and s[1] == e[1]:
        return 2
    elif s[0] == e[0] and s[2] == e[2]:
        return 1
    elif s[2] == e[2] and s[1] == e[1]:
        return 0
    else:
        assert(False)

def parse(line):
    ends = line.split('~')
    assert(len(ends) == 2)
    return [parse_end(end) for end in ends]

def parse_end(end):
    x = end.split(',')
    assert(len(x) == 3)
    return [int(a.strip()) for a in x]

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
