import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '11_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[x for x in dat] for dat in data]

    last_hashed = hashed(data)
    # for i in range(10):
    while True:
        # pprint(data)
        # print(i, hashed(data))
        data = iterate(data)
        new_h = hashed(data)
        # print(new_h)
        if new_h == last_hashed:
            print(num_seats(new_h))
            break
        last_hashed = new_h

ADJACS = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1),
]

def iterate(grid):
    def find_at(inp):
        row, col = inp
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return None
        return grid[row][col]

    def neighbors_of(row, col):
        ns = [find_at(add_tup((row, col), a)) for a in ADJACS]
        ns = [n for n in ns if n is not None]
        # print(row, col, ns)
        return ns

    new_grid = [[None for i in range(len(grid[0]))] for j in range(len(grid))]
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            n = neighbors_of(row_idx, col_idx)
            if grid[row_idx][col_idx] == 'L' and len([x for x in n if x == '#']) == 0:
                new_grid[row_idx][col_idx] = '#'
            elif grid[row_idx][col_idx] == '#' and len([x for x in n if x == '#']) >= 4:
                new_grid[row_idx][col_idx] = 'L'
            else:
                new_grid[row_idx][col_idx] = grid[row_idx][col_idx]
    return new_grid

def pprint(grid):
    print()
    for i in grid:
        print(''.join(i))
    print()

def hashed(grid):
    return ''.join([''.join(i) for i in grid])

def num_seats(h):
    return h.count('#')

def main2():
    data = readlines(FILENAME)
    data = [[x for x in dat] for dat in data]

    mapped = map_out_viz(data)
    # print(mapped)

    last_hashed = hashed(data)
    # for i in range(30):
    while True:
        # pprint(data)
        # print(i, hashed(data))
        data = iterate_with_viz(data, mapped)
        new_h = hashed(data)
        # # print(new_h)
        if new_h == last_hashed:
            print(num_seats(new_h))
            break
        last_hashed = new_h


def iterate_with_viz(grid, mapped):
    def find_at(inp):
        row, col = inp
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return None
        return grid[row][col]

    def neighbors_of(row, col):
        ns = [find_at(neigh) for neigh in mapped[(row, col)]]
        # ns = [n for n in ns if n is not None]
        assert(len([n for n in ns if n is None]) == 0)
        # print(row, col, ns)
        return ns

    new_grid = [[None for i in range(len(grid[0]))] for j in range(len(grid))]
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            n = neighbors_of(row_idx, col_idx)
            if grid[row_idx][col_idx] == 'L' and len([x for x in n if x == '#']) == 0:
                new_grid[row_idx][col_idx] = '#'
            elif grid[row_idx][col_idx] == '#' and len([x for x in n if x == '#']) >= 5:
                new_grid[row_idx][col_idx] = 'L'
            else:
                new_grid[row_idx][col_idx] = grid[row_idx][col_idx]
    return new_grid

def map_out_viz(grid):
    def find_at(inp):
        row, col = inp
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return None
        return grid[row][col]

    def neighbor_in_dir(start, a):
        curr = start
        while True:
            next_step = add_tup(curr, a)
            maybe_item = find_at(next_step)
            if maybe_item is None:
                return None
            if maybe_item == 'L' or maybe_item == '#':
                return next_step
            curr = next_step
        assert False

    def neighbors_of(row, col):
        ns = []
        for a in ADJACS:
            final_coords = neighbor_in_dir((row, col), a)
            if final_coords is not None:
                ns.append(final_coords)
        return ns

    res = {}
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            res[(row_idx, col_idx)] = neighbors_of(row_idx, col_idx)
    return res


if __name__ == '__main__':
    main()
    main2()
