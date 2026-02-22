import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    s_pos = None
    splits = set()
    for row in range(len(data)):
        for col in range(len(data[0])):
            cell = data[row][col]
            if cell == 'S':
                assert s_pos is None
                s_pos = (row, col)
            elif cell == "^":
                splits.add((row, col))
    # print(s_pos)
    # print(splits)

    height = len(data)

    split_counter = 0
    tach_ends = set([s_pos])
    while len(tach_ends) > 0:
    # for i in range(25):
        new_tach_ends = set()
        for tach_end in tach_ends:
            new_pos = add_tup(tach_end, (1, 0))
            # print(new_pos)
            if new_pos[0] >= height:
                break
            if new_pos in splits:
                split_counter += 1
                new_tach_ends.add(add_tup(new_pos, (0, -1)))
                new_tach_ends.add(add_tup(new_pos, (0, 1)))
            else:
                new_tach_ends.add(new_pos)
        tach_ends = new_tach_ends
        # print(tach_ends)
        # exit(1)
    print(split_counter)

def main2():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    s_pos = None
    splits = set()
    for row in range(len(data)):
        for col in range(len(data[0])):
            cell = data[row][col]
            if cell == 'S':
                assert s_pos is None
                s_pos = (row, col)
            elif cell == "^":
                splits.add((row, col))
    # print(s_pos)
    # print(splits)

    height = len(data)

    tach_ends = [(s_pos, 1)]
    while len(tach_ends) > 0:
    # for i in range(25):
        t_dict = {}

        def add_to_dict(xcxc, count):
            if xcxc in t_dict:
                t_dict[xcxc] += count
            else:
                t_dict[xcxc] = count

        for tach_end_tup in tach_ends:
            tach_end, num_tachs = tach_end_tup
            new_pos = add_tup(tach_end, (1, 0))
            # print(new_pos)
            if new_pos[0] >= height:
                # print(tach_ends)
                final_tach_ends = tach_ends
                break
            if new_pos in splits:
                add_to_dict(add_tup(new_pos, (0, -1)), num_tachs)
                add_to_dict(add_tup(new_pos, (0, 1)), num_tachs)
            else:
                add_to_dict(new_pos, num_tachs)
        
        # print(list(t_dict.items()))
        tach_ends = list(t_dict.items())
        # print(tach_ends)
        # exit(1)
    # print(split_counter)
    # print(final_tach_ends)
    print(sum([x[1] for x in final_tach_ends]))

if __name__ == '__main__':
    main()
    main2()
