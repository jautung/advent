import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '18_dat.txt'
# mapper = {}

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    # print(data)
    edge_points = trace_edge(data)
    # print_2d(edge_points)
    min_row = min(a[0][0] for a in edge_points)
    max_row = max(a[0][0] for a in edge_points)
    min_col = min(a[0][1] for a in edge_points)
    max_col = max(a[0][1] for a in edge_points)
    path = set([e[0] for e in edge_points])
    mapper = dict()
    for e in edge_points:
        mapper[e[0]] = e[2]
    def data_get(r, c):
        if (r,c) in mapper:
            return mapper[(r,c)]
        return '.'
    n_i = interior(path, data_get, min_row, max_row, min_col, max_col)
    print(n_i + len(path))
    # for r in range(min_row, max_row+1):
    #     for c in range(min_col, max_col+1):
    #         print(data_get(r, c), end='')
    #     print()

    # edge_points_set = set(edge_points)

    # print(min_row)
    # print(max_row)
    # print(min_col)
    # print(max_col)
    # counter = 0
    # for row_i in range(min_row-1, max_row+2):
    #     on_edge = False
    #     inside = False
    #     for col_i in range(min_col-1, max_col+2):
    #         if not on_edge and (row_i, col_i) in edge_points_set:
    #             on_edge = True
    #         if on_edge and (row_i, col_i) not in edge_points_set:
    #             on_edge = False
    #             inside = not inside
    #         if (row_i, col_i) in edge_points_set or inside:
    #             print((row_i, col_i))
    #             counter += 1
    #         # else:
    #         #     print((row_i, col_i))
    # print(counter)
    # state = dict()
    # for row_i in range(min_row-1, max_row+2):
    #     for col_i in range(min_col-1, max_col+2):
    #         if col_i == 0:
    #             if (row_i, col_i) in edge_points_set:
    #                 state[(row_i, col_i)] = 'EDGE'
    #             else:
    #                 state[(row_i, col_i)] = 'OUTSIDE'
    #         else:
    #             if (row_i, col_i) in edge_points_set:
    #                 state[(row_i, col_i)] = 'EDGE'
    #             else:
    #                 if state[(row_i, col_i-1)] == 'EDGE':
    #                     # look further left and invert it
    #                 elif state[(row_i, col_i-1)] == 'INSIDE':
    #                 elif state[(row_i, col_i-1)] == 'OUTSIDE':

def interior(path, data_get, min_row, max_row, min_col, max_col):
    n_i = 0
    n_o = 0
    # print(N_ROW, N_COL)
    for r in range(min_row, max_row+1):
        for c in range(min_col, max_col+1):
            # print('R', r, 'C', c)
            if (r, c) in path:
                continue
            row = [(r, iter_c) for iter_c in range(c, max_col+1)]
            pieces = [data_get(r, c) if (r, c) in path else '.' for r, c in row]
            # print(''.join(pieces))
            # print(r, c, pieces)
            # row_inclusivity = [x in path for x in row]
            # k = groupby(pieces, key=lambda piece: piece != '.')
            # print([list(i[1]) for i in k])
            real_pieces = [p for p in pieces if p != '.' and p != '-']
            why_not_str = ''.join(real_pieces)
            # print('S',why_not_str)
            why_not_str = why_not_str.replace('F7', '')
            why_not_str = why_not_str.replace('FJ', '|')
            why_not_str = why_not_str.replace('L7', '|')
            why_not_str = why_not_str.replace('LJ', '')
            # print('E',why_not_str)
            assert(all([x == '|' for x in why_not_str]))
            if len(why_not_str) % 2 == 1:
                # print(r, c, "inside")
                n_i += 1
            else:
                # print(r, c, "outside")
                n_o += 1
                # print(list(i[1]))
            # exit(1)
            # # print(row_inclusivity, n_truth_streaks(row_inclusivity))
            # # print()
            # if n_truth_streaks(row_inclusivity) % 2 == 1:
            #     print(r, c, "inside", n_truth_streaks(row_inclusivity))
            #     n_i += 1
            # else:
            #     print(r, c, "outside", n_truth_streaks(row_inclusivity))
            #     n_o += 1
    # print(path)
    return n_i

                        
def trace_edge(data):
    ret = []
    curr = (0, 0)
    first_dir = data[0][0]
    prev_dir = None
    # ret.append((curr, None))
    for item in data:
        direction, number, _ = item
        if len(ret) > 0:
            ret[-1] = (ret[-1][0], combine(prev_dir, direction))
        for _ in range(number):
            curr = step(curr, direction)
            ret.append((curr, direction))
        prev_dir = direction
    assert(curr == (0, 0)) # close the loop
    ret[-1] = (ret[-1][0], combine(prev_dir, first_dir))
    return [(a[0], a[1], notate(a[1])) for a in ret]

def notate(dirr):
    if dirr == 'L' or dirr == 'R':
        return '-'
    elif dirr == 'U' or dirr == 'D':
        return '|'
    elif dirr == 'UR' or dirr == 'LD':
        return 'F'
    elif dirr == 'UL' or dirr == 'RD':
        return '7'
    elif dirr == 'RU' or dirr == 'DL':
        return 'J'
    elif dirr == 'LU' or dirr == 'DR':
        return 'L'
    assert(False)

def combine(dir_a, dir_b):
    return dir_a + dir_b

def step(coord, direction, number=1):
    if direction == 'L':
        return (coord[0], coord[1]-number)
    elif direction == 'R':
        return (coord[0], coord[1]+number)
    elif direction == 'U':
        return (coord[0]-number, coord[1])
    elif direction == 'D':
        return (coord[0]+number, coord[1])
    assert(False)
    

def parse(dat):
    x = dat.split(' ')
    direction = x[0]
    number = int(x[1])
    hash = x[2][2:-1]
    return (direction, number, hash)

def main2():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    data = [parse_2(dat[2]) for dat in data]
    # print_2d(data)
    lines = get_lines(data)
    # print_2d(lines)
    boundary_points = [l[0] for l in lines]
    # min_row = min(a[0] for a in boundary_points)
    # max_row = max(a[0] for a in boundary_points)
    # min_col = min(a[1] for a in boundary_points)
    # max_col = max(a[1] for a in boundary_points)
    # # print(min_row)
    # print(max_row)
    # print(min_col)
    # print(max_col)
    row_keyframes = sorted(list(set([a[0] for a in boundary_points])))
    col_keyframes = sorted(list(set([a[1] for a in boundary_points])))
    # print(row_keyframes)
    # print(col_keyframes)
    tot = 0
    # print_2d(lines)
    for i, key_row_index in enumerate(row_keyframes):
        # print(f'processing row range {i} of {len(row_keyframes)}')
        tot += n_interior_for_row(key_row_index, lines, col_keyframes)
        if i != len(row_keyframes)-1:
            # there is a range from `key_row_index` to `row_keyframes[i+1]` (exclusive both sides)
            # that will all have the same n_interior because there are no key frames in between
            multiplier = (row_keyframes[i+1] - key_row_index - 1)
            if multiplier > 0:
                tot += multiplier * n_interior_for_row(key_row_index+1, lines, col_keyframes)
    print(tot)

def n_interior_for_row(row_index, lines, col_keyframes):
    # print_2d(lines)
    tot = 0
    for i, key_col_index in enumerate(col_keyframes):
        if is_edge_or_interior(row_index, key_col_index, lines):
            tot += 1
        if i != len(col_keyframes)-1:
            # there is a range from `key_col_index` to `col_keyframes[i+1]` (exclusive both sides)
            # that will all have the same is_edge_or_interior because there are no key frames in between
            n_in_range = (col_keyframes[i+1] - key_col_index - 1)
            if n_in_range > 0 and is_edge_or_interior(row_index, key_col_index+1, lines):
                tot += n_in_range
    return tot

def is_edge_or_interior(row_index, col_index, lines):
    # print_2d(lines)
    if is_edge(row_index, col_index, lines):
        return True
    n_left_barriers = sum([1 for line in lines if counts_as_a_left_barrier(row_index, col_index, line)]) 
    return n_left_barriers % 2 != 0

def counts_as_a_left_barrier(row_index, col_index, line):
    start, start_conn, end, end_conn, pipe = line
    if pipe == '-':
        assert(start[0] == end[0])
        if start[0] == row_index and col_index > max(start[1], end[1]) and s_or_5(start_conn, end_conn):
            return True
        else:
            return False
    elif pipe == '|':
        assert(start[1] == end[1])
        if col_index > start[1] and row_index > min(start[0], end[0]) and row_index < max(start[0], end[0]):
            # intentionally strict since the two endpoints will be handled by the row side of things
            return True
        return False
    assert(False)

def s_or_5(start_conn, end_conn):
    if set([start_conn, end_conn]) == set(['F', 'J']):
        return True
    if set([start_conn, end_conn]) == set(['L', '7']):
        return True
    return False

def is_edge(row_index, col_index, lines):
    for line in lines:
        start, start_conn, end, end_conn, pipe = line
        if pipe == '-':
            assert(start[0] == end[0])
            if start[0] == row_index and col_index >= min(start[1], end[1]) and col_index <= max(start[1], end[1]):
                return True
        elif pipe == '|':
            assert(start[1] == end[1])
            if start[1] == col_index and row_index >= min(start[0], end[0]) and row_index <= max(start[0], end[0]):
                return True
    return False

def get_lines(data):
    ret = []
    curr = (0, 0)
    for index, item in enumerate(data):
        number, direction = item
        prev_dir = data[(index - 1) % len(data)][1]
        next_dir = data[(index + 1) % len(data)][1]
        # start
        # end
        # - or | direction
        # endpoints FL7J for each of start and end
        start = curr
        start_conn = notate(combine(prev_dir, direction))
        end_conn = notate(combine(direction, next_dir))
        curr = step(curr, direction, number)
        end = curr
        ret.append((start, start_conn, end, end_conn, '-' if direction == 'L' or direction == 'R' else '|'))
    assert(curr == (0, 0)) # close the loop
    return ret

def trace_edge_2(data):
    ret = []
    curr = (0, 0)
    first_dir = data[0][1]
    prev_dir = None
    # ret.append((curr, None))
    for item in data:
        number, direction = item
        if len(ret) > 0:
            ret[-1] = (ret[-1][0], combine(prev_dir, direction))
        for _ in range(number):
            curr = step(curr, direction)
            ret.append((curr, direction))
        prev_dir = direction
    assert(curr == (0, 0)) # close the loop
    ret[-1] = (ret[-1][0], combine(prev_dir, first_dir))
    return [(a[0], a[1], notate(a[1])) for a in ret]


def parse_2(hex):
    # hex[:-1]
    if hex[-1] == '0':
        direction = 'R'
    elif hex[-1] == '1':
        direction = 'D'
    elif hex[-1] == '2':
        direction = 'L'
    elif hex[-1] == '3':
        direction = 'U'
    else:
        assert(False)
    return int(hex[:-1], 16), direction
    

if __name__ == '__main__':
    main()
    main2()
