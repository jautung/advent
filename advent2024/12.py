import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '12_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    HEIGHT = len(data)
    WIDTH = len(data[0])

    def in_bounds(pt):
        row, col = pt
        return row >= 0 and col >= 0 and row < HEIGHT and col < WIDTH

    def find_region(pt):
        TILE = data[pt[0]][pt[1]]
        n_dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = set()
        queue = [pt]
        while len(queue) > 0:
            curr = queue.pop()
            if curr in seen:
                continue
            seen.add(curr)
            neighbors = [add_tup(curr, n) for n in n_dirs]
            neighbors = [n for n in neighbors if in_bounds(n) and n not in seen and data[n[0]][n[1]] == TILE]
            [queue.append(n) for n in neighbors]
        return seen

    points_in_region = set()
    regions = set() # set of sets
    for row in range(HEIGHT):
        for col in range(WIDTH):
            pt = (row, col)
            if pt in points_in_region:
                continue
            curr_reg = find_region(pt)
            regions.add(frozenset(curr_reg))
            points_in_region = points_in_region.union(curr_reg)
    # print(regions)
    # print(points_in_region)
    assert len(points_in_region) == WIDTH * HEIGHT

    def boundary(reg):
        n_dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        outer_bound_count = 0
        for pt in reg:
            neighbors = [add_tup(pt, n) for n in n_dirs]
            # neighbors = [n for n in neighbors]
            neighbors_not_in_region = [n for n in neighbors if n not in reg]
            outer_bound_count += len(neighbors_not_in_region)
        return outer_bound_count

    tot = 0
    for r in regions:
        # print(r, boundary(r), len(r), boundary(r) * len(r))
        tot += boundary(r) * len(r)
    print(tot)

def main2():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    HEIGHT = len(data)
    WIDTH = len(data[0])

    def in_bounds(pt):
        row, col = pt
        return row >= 0 and col >= 0 and row < HEIGHT and col < WIDTH

    def find_region(pt):
        TILE = data[pt[0]][pt[1]]
        n_dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = set()
        queue = [pt]
        while len(queue) > 0:
            curr = queue.pop()
            if curr in seen:
                continue
            seen.add(curr)
            neighbors = [add_tup(curr, n) for n in n_dirs]
            neighbors = [n for n in neighbors if in_bounds(n) and n not in seen and data[n[0]][n[1]] == TILE]
            [queue.append(n) for n in neighbors]
        return seen

    points_in_region = set()
    regions = set() # set of sets
    for row in range(HEIGHT):
        for col in range(WIDTH):
            pt = (row, col)
            if pt in points_in_region:
                continue
            curr_reg = find_region(pt)
            regions.add(frozenset(curr_reg))
            points_in_region = points_in_region.union(curr_reg)
    # print(regions)
    # print(points_in_region)
    assert len(points_in_region) == WIDTH * HEIGHT

    def fence_cost(reg):
        n_dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        outer_bound_horz_set = dict() # map from (lower, higher) to (col)
        outer_bound_vert_set = dict() # map from (left, right) to (row)
        # print('b',outer_bound_vert_set[(2,3)])
        for pt in reg:
            neighbors = [add_tup(pt, n) for n in n_dirs]
            # neighbors = [n for n in neighbors]
            neighbors_not_in_region = [n for n in neighbors if n not in reg]
            for second in neighbors_not_in_region:
                if pt[0] == second[0]:
                    # left = min(pt[1], second[1])
                    # right = max(pt[1], second[1])
                    # if (left, right) == (2,3):
                        # print(pt, second)
                        # print('c',outer_bound_vert_set[(2,3)])
                    # print('x',outer_bound_vert_set[(2,3)], (left, right))
                    if (pt[1], second[1]) in outer_bound_vert_set:
                        outer_bound_vert_set[(pt[1], second[1])].add(pt[0])
                    else:
                        outer_bound_vert_set[(pt[1], second[1])] = set([pt[0]])
                    # print('a', outer_bound_vert_set[(2,3)], (left, right))
                elif pt[1] == second[1]:
                    # lower = min(pt[0], second[0])
                    # higher = max(pt[0], second[0])
                    if (pt[0], second[0]) in outer_bound_horz_set:
                        outer_bound_horz_set[(pt[0], second[0])].add(pt[1])
                    else:
                        outer_bound_horz_set[(pt[0], second[0])] = set([(pt[1])])
                else:
                    assert False
                # outer_bound_count += len(neighbors_not_in_region)

        def num_contiguous(lst):
            s = sorted(list(lst))
            # print(s)
            last = None
            counter = 0
            for i in s:
                if last is None or i != last + 1:
                    counter += 1
                last = i
            # print(s, counter)
            return counter
        # print(outer_bound_vert_set[(2,3)])

        ret = 0
        for k in outer_bound_horz_set:
            # print(k, 'horz')
            ret += num_contiguous(outer_bound_horz_set[k])
        # print()
        for k in outer_bound_vert_set:
            # print(k, 'vert')
            ret += num_contiguous(outer_bound_vert_set[k])
        return ret

# .......789
# ........FF0
# .........F1
# VV.....FFF2
# VV.....FFF3
# VVVV....F.4
# VVIV......
# VVIII.....
# MIIIII....
# MIIISIJ...
# MMMISSJ...


    # test = [(0, 8), (0, 9), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9), (4, 8)]
    # print(sorted(test))
    # print(fence_cost(test))
    # supposed to be 12
    # return

    tot = 0
    for r in regions:
        # print(r, fence_cost(r), len(r), fence_cost(r) * len(r))
        # print(r, fence_cost(r))
        tot += fence_cost(r) * len(r)
    print(tot)

if __name__ == '__main__':
    main()
    main2()

