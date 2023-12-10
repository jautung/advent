import time
from itertools import groupby 
import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '10_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print(data)
    N_ROW = len(data)
    N_COL = len(data[0])
    # for r in data:
    #     print(r)
    row, col = find_s(data, N_ROW, N_COL)
    # print(row, col)
    # print("xxx")
    # print(follow_from(data, N_ROW, N_COL, (row+1, col), 'TOP'))
    # print("xxx")
    # print(follow_from(data, N_ROW, N_COL, (row-1, col), 'BOTTOM'))
    # print("xxx")
    # print(follow_from(data, N_ROW, N_COL, (row, col+1), 'LEFT'))
    # print("xxx")
    # print(follow_from(data, N_ROW, N_COL, (row, col-1), 'RIGHT'))
    lst = [
        follow_from(data, N_ROW, N_COL, (row+1, col), 'TOP'),
        follow_from(data, N_ROW, N_COL, (row-1, col), 'BOTTOM'),
        follow_from(data, N_ROW, N_COL, (row, col+1), 'LEFT'),
        follow_from(data, N_ROW, N_COL, (row, col-1), 'RIGHT'),
    ]
    routes = [a for a in lst if a != None]
    # print(routes)
    assert(len(routes) == 2)
    assert(len(routes[0]) == len(routes[1]))
    print(len(routes[0])//2)
    # print(3//2)
    
def follow_from(data, N_ROW, N_COL, coord, entry_dir):
    return follow_from_trace([], data, N_ROW, N_COL, coord, entry_dir)

def follow_from_trace(acc, data, N_ROW, N_COL, coord, entry_dir):
    # print(coord, entry_dir)
    acc.append(coord)
    r, c = coord
    if r >= N_ROW or r < 0 or c >= N_COL or c < 0:
        return None
    val = data[r][c]
    if val == 'S':
        # print("FOUND!")
        return acc
    if entry_dir == 'TOP':
        if val == '|':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r+1, c), 'TOP')
        elif val == 'L':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r, c+1), 'LEFT')
        elif val == 'J':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r, c-1), 'RIGHT')
    elif entry_dir == 'BOTTOM':
        if val == '|':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r-1, c), 'BOTTOM')
        elif val == 'F':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r, c+1), 'LEFT')
        elif val == '7':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r, c-1), 'RIGHT')
    elif entry_dir == 'LEFT':
        if val == '-':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r, c+1), 'LEFT')
        elif val == 'J':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r-1, c), 'BOTTOM')
        elif val == '7':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r+1, c), 'TOP')
    elif entry_dir == 'RIGHT':
        if val == '-':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r, c-1), 'RIGHT')
        elif val == 'L':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r-1, c), 'BOTTOM')
        elif val == 'F':
            return follow_from_trace(acc, data, N_ROW, N_COL, (r+1, c), 'TOP')

def find_s(data, N_ROW, N_COL):
    for r in range(N_ROW):
        for c in range(N_COL):
            if data[r][c] == 'S':
                return r, c

def main2():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print(data)
    N_ROW = len(data)
    N_COL = len(data[0])
    # for r in data:
    #     print(r)
    row, col = find_s(data, N_ROW, N_COL)
    # print(row, col)
    # print("xxx")
    # print(follow_from(data, N_ROW, N_COL, (row+1, col), 'TOP'))
    # print("xxx")
    # print(follow_from(data, N_ROW, N_COL, (row-1, col), 'BOTTOM'))
    # print("xxx")
    # print(follow_from(data, N_ROW, N_COL, (row, col+1), 'LEFT'))
    # print("xxx")
    # print(follow_from(data, N_ROW, N_COL, (row, col-1), 'RIGHT'))
    lst = [
        follow_from(data, N_ROW, N_COL, (row+1, col), 'TOP'),
        follow_from(data, N_ROW, N_COL, (row-1, col), 'BOTTOM'),
        follow_from(data, N_ROW, N_COL, (row, col+1), 'LEFT'),
        follow_from(data, N_ROW, N_COL, (row, col-1), 'RIGHT'),
    ]
    # print(lst)
    routes = [a for a in lst if a != None]
    # print(routes)
    assert(len(routes) == 2)
    assert(len(routes[0]) == len(routes[1]))
    s_piece = get_s_piece([a != None for a in lst])
    data[row][col] = s_piece
    # print(len(routes[0])//2)
    # print(3//2)
    path = routes[0]
    # print(path)
    print(interior(path, data, N_ROW, N_COL))

def get_s_piece(lst):
    can_go_down = lst[0]
    can_go_up = lst[1]
    can_go_right = lst[2]
    can_go_left = lst[3]
    if can_go_down:
        if can_go_up:
            return '|'
        elif can_go_right:
            return 'F'
        elif can_go_left:
            return '7'
    elif can_go_up:
        if can_go_right:
            return 'L'
        elif can_go_left:
            return 'J'
    elif can_go_right:
        if can_go_left:
                return '-'
    assert(False)

def interior(path, data, N_ROW, N_COL):
    n_i = 0
    n_o = 0
    # print(N_ROW, N_COL)
    for r in range(N_ROW):
        for c in range(N_COL):
            # print('R', r, 'C', c)
            if (r, c) in path:
                continue
            row = [(r, iter_c) for iter_c in range(c, N_COL)]
            pieces = [data[r][c] if (r, c) in path else '.' for r, c in row]
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

# def n_truth_streaks(lst):
#     res = [i[0] for i in groupby(lst)]
#     return len([x for x in res if x])

if __name__ == '__main__':
    sys.setrecursionlimit(999999999)
    # s = time.time()
    main()
    # print(time.time()-s, 'seconds for first part')
    # s = time.time()
    main2()
    # print(time.time()-s, 'seconds for second part')
