import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '14_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    def parse(line):
        parts = line.split(' ')
        p = parts[0].split('=')[1].split(',')
        v = parts[1].split('=')[1].split(',')
        # this is x, y (so col, row)
        return ((int(p[0]), int(p[1])), (int(v[0]), int(v[1])))
    data = [parse(dat) for dat in data]
    WIDTH = 101
    HEIGHT = 103
    # WIDTH = 11
    # HEIGHT = 7
    # print_2d(data)
    def get_pos_at_t(t):
        def move_for_t(p, v):
            return ((p[0] + t * v[0]) % WIDTH, (p[1] + t * v[1]) % HEIGHT)
        final_poses = [move_for_t(a[0], a[1]) for a in data]
        return final_poses

    f = get_pos_at_t(100)
    # print_2d(f)

    quads = {0: [], 1: [], 2: [], 3: []}
    for p in f:
        i_middle_col = WIDTH // 2
        i_middle_row = HEIGHT // 2
        if p[0] < i_middle_col and p[1] < i_middle_row:
            quads[0].append(p)
        elif p[0] < i_middle_col and p[1] > i_middle_row:
            quads[1].append(p)
        elif p[0] > i_middle_col and p[1] < i_middle_row:
            quads[2].append(p)
        elif p[0] > i_middle_col and p[1] > i_middle_row:
            quads[3].append(p)
    # print(quads)
    # print(len(quads[0]))
    # print(len(quads[1]))
    # print(len(quads[2]))
    # print(len(quads[3]))
    print(len(quads[0])*len(quads[1])*len(quads[2])*len(quads[3]))



def main2():
    data = readlines(FILENAME)
    def parse(line):
        parts = line.split(' ')
        p = parts[0].split('=')[1].split(',')
        v = parts[1].split('=')[1].split(',')
        # this is x, y (so col, row)
        return ((int(p[0]), int(p[1])), (int(v[0]), int(v[1])))
    data = [parse(dat) for dat in data]
    WIDTH = 101
    HEIGHT = 103
    # WIDTH = 11
    # HEIGHT = 7
    # print_2d(data)
    def get_pos_at_t(t):
        def move_for_t(p, v):
            return ((p[0] + t * v[0]) % WIDTH, (p[1] + t * v[1]) % HEIGHT)
        final_poses = [move_for_t(a[0], a[1]) for a in data]
        return final_poses

    def print_pretty(points):
        board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        for p in points:
            board[p[1]][p[0]] += 1
        for rows in board:
            print(''.join(['O' if r > 0 else '.' for r in rows]))

    # 704 and 805 are both weird vertical patterns
    # t = 704 - 101
    # 53 horizontal pattern with 156
    # t = 0
    t = 53
    while True:
        # t += 101
        # t += 1
        t += 103
        print(t)
        f = get_pos_at_t(t)
        print_pretty(f)
        input()

if __name__ == '__main__':
    main()
    main2()
