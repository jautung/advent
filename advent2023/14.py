import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '14_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print('\n'.join([''.join(dat) for dat in data]))
    tilt_north(data)
    # print()
    # print('\n'.join([''.join(dat) for dat in data]))
    c = cost(data)
    print(c)

def cost(data):
    s = 0
    for r_index, row in enumerate(data):
        for c_index, item in enumerate(row):
            if item != "O":
                continue
            s += len(data) - r_index
    return s

def tilt_north(data): # mutating
    # from top downwards so we can assume everything on top is settled
    for r_index, row in enumerate(data):
        for c_index, item in enumerate(row):
            if item != "O":
                continue
            data[r_index][c_index] = "."
            new_r_index = r_index
            while new_r_index >= 0:
                # keep travelling until we hit something
                if data[new_r_index][c_index] != ".":
                    break
                new_r_index -= 1
            # now new_r_index is either -1 and out of bounds, or it is the location of something
            # either way, rock will rest at new_r_index + 1
            data[new_r_index+1][c_index] = "O"
    # arguably we could've done this per column in parallel, maybe we can do that later
    # done
    return data

def main2():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print('\n'.join([''.join(dat) for dat in data]))
    # print('initial')
    # print('\n'.join([''.join(dat) for dat in data]))
    spin_idx = 0
    # TARGET_SPIN = 100
    TARGET_SPIN = 1000000000
    key = '\n'.join([''.join(dat) for dat in data])
    cached_states = [key]
    while True:
        data = tilt_north(data)
        # print()
        # print('\n'.join([''.join(dat) for dat in data]))
        data = tilt_west(data)
        # print()
        # print('\n'.join([''.join(dat) for dat in data]))
        data = tilt_south(data)
        # print()
        # print('\n'.join([''.join(dat) for dat in data]))
        data = tilt_east(data)
        # print()
        # print(f'after spin {spin_idx + 1}')
        key = '\n'.join([''.join(dat) for dat in data])
        if key in cached_states:
            # print("REPEAT!!")
            first_idx = cached_states.index(key)
            # print(first_idx, len(cached_states) + 1)
            # first = 2
            # len = 5
            # [XXX, YYY, A, B, C], ... A, B, C, A, B, C
            relevant_array = cached_states[first_idx:]
            augmented_target = TARGET_SPIN - first_idx
            to_comp = relevant_array[augmented_target % len(relevant_array)]
            print(cost([[c for c in row] for row in to_comp.split('\n')]))
            # in_period_idx = TARGET_SPIN % (len(cached_states) - first_idx)
            break
        cached_states.append(key)
        # print(f"spint {spin_idx + 1}: {cost(data)}")
        # print('\n'.join([''.join(dat) for dat in data]))
        # if spin_idx + 1 == TARGET_SPIN:
        #     break
        spin_idx += 1
        # exit(1)
        # if spin_idx == 5:
        #     exit(1)
    # print()
    # print('\n'.join([''.join(dat) for dat in data]))
    # c = cost(data)
    # print(c)

def tilt_south(data):
    data.reverse()
    data = tilt_north(data)
    data.reverse()
    return data

def tilt_west(data):
    # print('???\n')
    # print('\n'.join([''.join(dat) for dat in data]))
    data = [[c for c in row] for row in transpose(data)]
    # print('????\n')
    # print('\n'.join([''.join(dat) for dat in data]))
    data = tilt_north(data)
    # print('?????\n')
    # print('\n'.join([''.join(dat) for dat in data]))
    return [[c for c in row] for row in transpose(data)]

def tilt_east(data):
    data = [[c for c in row] for row in transpose(data)]
    data.reverse()
    data = tilt_north(data)
    data.reverse()
    data = [[c for c in row] for row in transpose(data)]
    return data

if __name__ == '__main__':
    main()
    main2()
