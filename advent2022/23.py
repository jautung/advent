import sys 
sys.path.append('..')

import copy
from collections import Counter
from collections import defaultdict
from helper import *

FILENAME = '23_dat.txt'
mapper = {}

def printer(elves, grid_width, grid_height):
    for row in range(grid_height):
        for col in range(grid_width):
            if (col, row) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

def main():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    # print_2d(data)
    grid_width = len(data[0])
    grid_height = len(data)
    # print(grid_width, grid_height)

    elves = set()
    for row in range(grid_height):
        for col in range(grid_width):
            if data[row][col] == '#':
                elves.add((col, row))
    # print_2d(elves)

    propose_order = [(0,-1),(0,1),(-1,0),(1,0)]
    round_num = 0
    while True:
        # print(round_num)
        # printer(elves, grid_width, grid_height)

        proposals = make_proposals(elves, propose_order, grid_width, grid_height)
        # print(proposals)
        proposed_results = Counter(list(proposals.values()))
        # print(proposed_results)
        # print(proposed_results[(2,0)])
        new_elves = set()
        for elf in elves:
            if proposed_results[proposals[elf]] > 1:
                new_elves.add(elf)
            else:
                new_elves.add(proposals[elf])
        # print(new_elves)
        # exit()
        if elves == new_elves:
            break
        elves = new_elves
        propose_order = propose_order[1:] + propose_order[:1]
        round_num += 1
        # if round_num == 4:
        #     exit()
        if round_num == 10:
            print(find_min_bounding_area(elves) - len(elves))
            return

    # printer(elves, grid_width, grid_height)

def find_min_bounding_area(elves):
    min_x = min([e[0] for e in elves])
    max_x = max([e[0] for e in elves])
    min_y = min([e[1] for e in elves])
    max_y = max([e[1] for e in elves])
    return (max_x-min_x+1) * (max_y-min_y+1)

def make_proposals(elves, propose_order, grid_width, grid_height):
    res = dict()
    for elf in elves:
        res[elf] = make_proposal(elf, propose_order, grid_width, grid_height, elves)
    return res

def make_proposal(elf, propose_order, grid_width, grid_height, elves):
    neighbor_ds = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    n_neighbors = sum([add_tup(elf, n) in elves for n in neighbor_ds])
    if n_neighbors == 0:
        return None
    for p_test in propose_order:
        if not in_grid(add_tup(elf, p_test), grid_width, grid_height):
            continue
        if p_test[0] == 0:
            p_test_neighbors = [p_test, (-1, p_test[1]), (1, p_test[1])]
        elif p_test[1] == 0:
            p_test_neighbors = [p_test, (p_test[0], -1), (p_test[0], 1)]
        else:
            assert(False)
        if sum([add_tup(elf, n) in elves for n in p_test_neighbors]) == 0:
            return add_tup(elf, p_test)
    return None

def in_grid(pos, grid_width, grid_height):
    # return pos[0] >= 0 and pos[0] < grid_width and pos[1] >= 0 and pos[1] < grid_height
    return True

def main2():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    # print_2d(data)
    grid_width = len(data[0])
    grid_height = len(data)
    # print(grid_width, grid_height)

    elves = set()
    for row in range(grid_height):
        for col in range(grid_width):
            if data[row][col] == '#':
                elves.add((col, row))
    # print_2d(elves)

    propose_order = [(0,-1),(0,1),(-1,0),(1,0)]
    round_num = 0
    while True:
        # print(round_num)
        # printer(elves, grid_width, grid_height)

        proposals = make_proposals(elves, propose_order, grid_width, grid_height)
        # print(proposals)
        proposed_results = Counter(list(proposals.values()))
        # print(proposed_results)
        # print(proposed_results[(2,0)])
        new_elves = set()
        for elf in elves:
            if proposed_results[proposals[elf]] > 1:
                new_elves.add(elf)
            else:
                new_elves.add(proposals[elf])
        # print(new_elves)
        # exit()
        if elves == new_elves:
            break
        elves = new_elves
        propose_order = propose_order[1:] + propose_order[:1]
        round_num += 1
        # if round_num == 4:
        #     exit()
        # if round_num == 10:
        #     print(find_min_bounding_area(elves) - len(elves))
        #     return

    # printer(elves, grid_width, grid_height)
    print(round_num+1)

if __name__ == '__main__':
    main()
    main2()
