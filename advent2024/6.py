import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    HEIGHT = len(data)
    WIDTH = len(data[0])

    def get_all_pos_of_type(c, tab):
        r = []
        for row in range(len(tab)):
            for col in range(len(tab[0])):
                if tab[row][col] == c:
                    r.append((row, col))
        return r

    guard = get_all_pos_of_type("^", data)
    assert len(guard) == 1
    guard = guard[0]
    obs = get_all_pos_of_type("#", data)

    # print(guard)
    # print(obs)
    def move_the_dude(guard, obs, HEIGHT, WIDTH):
        dir_array = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def in_bounds(tup):
            return tup[0] >= 0 and tup[1] >= 0 and tup[0] < HEIGHT and tup[1] < WIDTH
        painted = set()
        curr_dir_index = 0
        curr_pos = guard
        while True:
            painted.add(curr_pos)
            curr_dir = dir_array[curr_dir_index % 4]
            # print(curr_pos, curr_dir)
            maybe_next_pos = add_tup(curr_pos, curr_dir)
            if not in_bounds(maybe_next_pos):
                return painted
            if maybe_next_pos in obs:
                curr_dir_index += 1
                continue
            curr_pos = maybe_next_pos
            continue

    res = move_the_dude(guard, obs, HEIGHT, WIDTH)
    # print(res)
    print(len(res))



def main2():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    HEIGHT = len(data)
    WIDTH = len(data[0])

    def get_all_pos_of_type(c, tab):
        r = []
        for row in range(len(tab)):
            for col in range(len(tab[0])):
                if tab[row][col] == c:
                    r.append((row, col))
        return r

    guard = get_all_pos_of_type("^", data)
    assert len(guard) == 1
    guard = guard[0]
    obs = get_all_pos_of_type("#", data)

    # print(guard)
    # print(obs)
    def move_the_dude(guard, obs, HEIGHT, WIDTH):
        dir_array = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def in_bounds(tup):
            return tup[0] >= 0 and tup[1] >= 0 and tup[0] < HEIGHT and tup[1] < WIDTH
        painted = set()
        curr_dir_index = 0
        curr_pos = guard
        while True:
            painted.add(curr_pos)
            curr_dir = dir_array[curr_dir_index % 4]
            # print(curr_pos, curr_dir)
            maybe_next_pos = add_tup(curr_pos, curr_dir)
            if not in_bounds(maybe_next_pos):
                return painted
            if maybe_next_pos in obs:
                curr_dir_index += 1
                continue
            curr_pos = maybe_next_pos
            continue

    paintings = move_the_dude(guard, obs, HEIGHT, WIDTH)
    # print(res)
    # print(len(res))


    # print(guard)
    # print(obs)
    def is_dude_infinite(guard, obs, HEIGHT, WIDTH):
        dir_array = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def in_bounds(tup):
            return tup[0] >= 0 and tup[1] >= 0 and tup[0] < HEIGHT and tup[1] < WIDTH
        painted = set()
        stasis = set()
        curr_dir_index = 0
        curr_pos = guard
        while True:
            painted.add(curr_pos)
            curr_dir = dir_array[curr_dir_index % 4]
            if (curr_pos, curr_dir) in stasis:
                return True
            stasis.add((curr_pos, curr_dir))
            # print(curr_pos, curr_dir)
            maybe_next_pos = add_tup(curr_pos, curr_dir)
            if not in_bounds(maybe_next_pos):
                return False
            if maybe_next_pos in obs:
                curr_dir_index += 1
                continue
            curr_pos = maybe_next_pos
            continue

    counter = 0
    for index, candidate in enumerate(paintings):
        # print(f"{index} of {len(paintings)}")
        if candidate in obs:
            continue # cannot add
        new_obs = obs + [candidate]
        res = is_dude_infinite(guard, new_obs, HEIGHT, WIDTH)
        if res:
            counter += 1
    print(counter)

    # res = is_dude_infinite(guard, obs + [(6, 3)], HEIGHT, WIDTH)
    # print(res)
    # print(len(res))


if __name__ == '__main__':
    main()
    main2()
