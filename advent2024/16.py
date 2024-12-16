import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '16_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]
    # print_2d(data)
    HEIGHT = len(data)
    WIDTH = len(data[0])
    walls = set()
    start = None
    end = None
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if data[row][col] == 'S':
                start = (row, col)
            elif data[row][col] == 'E':
                end = (row, col)
            elif data[row][col] == '#':
                walls.add((row, col))
            else:
                assert data[row][col] == '.'
    assert start is not None
    assert end is not None

    min_points_to_state = dict()
    bookkeep_previous_state = dict()
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if (row, col) in walls:
                continue
            for facing in ['N', 'S', 'E', 'W']:
                min_points_to_state[(row, col, facing)] = None
                bookkeep_previous_state[(row, col, facing)] = None
    min_points_to_state[(start[0], start[1], 'E')] = 0

    # print(min_points_to_state)
    # MAX_ITERS = HEIGHT * WIDTH
    while True:
        changed = False
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if (row, col) in walls:
                    continue
                for facing in ['N', 'S', 'E', 'W']:
                    steps_into_this = []

                    if facing == 'N':
                        neigh_turns = ['E', 'W']
                    elif facing == 'S':
                        neigh_turns = ['E', 'W']
                    elif facing == 'E':
                        neigh_turns = ['N', 'S']
                    elif facing == 'W':
                        neigh_turns = ['N', 'S']
                    for n in neigh_turns:
                        steps_into_this.append(((row, col, n), +1000))

                    if facing == 'N':
                        steps_into_this.append(((row+1, col, facing), +1))
                    elif facing == 'S':
                        steps_into_this.append(((row-1, col, facing), +1))
                    elif facing == 'E':
                        steps_into_this.append(((row, col-1, facing), +1))
                    elif facing == 'W':
                        steps_into_this.append(((row, col+1, facing), +1))

                    all_possible_new_considerations = []
                    for s_into in steps_into_this:
                        if s_into[0] in min_points_to_state and min_points_to_state[s_into[0]] is not None:
                            all_possible_new_considerations.append((s_into[0], min_points_to_state[s_into[0]] + s_into[1]))
                    if len(all_possible_new_considerations) == 0:
                        continue

                    min_all_possible_new_considerations = min(all_possible_new_considerations, key=lambda item: item[1])
                    if min_points_to_state[(row, col, facing)] == None:
                        min_points_to_state[(row, col, facing)] = min_all_possible_new_considerations[1]
                        assert bookkeep_previous_state[(row, col, facing)] is None
                        bookkeep_previous_state[(row, col, facing)] = set([m[0] for m in all_possible_new_considerations if m[1] == min_all_possible_new_considerations[1]])
                        changed = True
                    elif min_all_possible_new_considerations[1] == min_points_to_state[(row, col, facing)]:
                        bookkeep_previous_state[(row, col, facing)] = bookkeep_previous_state[(row, col, facing)].union(set([m[0] for m in all_possible_new_considerations if m[1] == min_all_possible_new_considerations[1]]))
                        # changed = True
                    elif min_all_possible_new_considerations[1] < min_points_to_state[(row, col, facing)]:
                        min_points_to_state[(row, col, facing)] = min_all_possible_new_considerations[1]
                        bookkeep_previous_state[(row, col, facing)] = set([m[0] for m in all_possible_new_considerations if m[1] == min_all_possible_new_considerations[1]])
                        changed = True
                    continue
        if not changed:
            break

    # print(min_points_to_state[(end[0], end[1], 'N')])
    # print(min_points_to_state[(end[0], end[1], 'S')])
    # print(min_points_to_state[(end[0], end[1], 'E')])
    # print(min_points_to_state[(end[0], end[1], 'W')])
    considerations = [
        min_points_to_state[(end[0], end[1], 'N')],
        min_points_to_state[(end[0], end[1], 'S')],
        min_points_to_state[(end[0], end[1], 'E')],
        min_points_to_state[(end[0], end[1], 'W')],
    ]
    x = min(considerations)
    print(x)

    def trace(ending_state):
        ret = set()
        queue = [ending_state]
        while len(queue) > 0:
            curr = queue.pop()
            # print(curr)
            ret.add((curr[0], curr[1]))
            maybe_prev = bookkeep_previous_state[curr]
            if maybe_prev is None:
                continue
            # print(maybe_prev)
            queue += maybe_prev
        return ret

    final_set = set()
    if x == min_points_to_state[(end[0], end[1], 'N')]:
        final_set = final_set.union(trace((end[0], end[1], 'N')))
    if x == min_points_to_state[(end[0], end[1], 'S')]:
        final_set = final_set.union(trace((end[0], end[1], 'S')))
    if x == min_points_to_state[(end[0], end[1], 'E')]:
        final_set = final_set.union(trace((end[0], end[1], 'E')))
    if x == min_points_to_state[(end[0], end[1], 'W')]:
        final_set = final_set.union(trace((end[0], end[1], 'W')))
    print(len(final_set))


def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    # main2()
