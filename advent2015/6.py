import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def parse(dat):
    if dat[0] == 'turn' and dat[1] == 'on':
        act = 'ON'
    elif dat[0] == 'turn' and dat[1] == 'off':
        act = 'OFF'
    elif dat[0] == 'toggle':
        act = 'TOGGLE'
    return act, parse_point(dat[-3]), parse_point(dat[-1])

def parse_point(point):
    l = [int(i) for i in point.split(',')]
    return l[0], l[1]

def main():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    LEN = 1000
    grid = [[False for _ in range(LEN)] for _ in range(LEN)]

    for dat in data:
        for i in range(dat[1][0], dat[2][0]+1):
            for j in range(dat[1][1], dat[2][1]+1):
                if dat[0] == 'ON':
                    grid[i][j] = True
                elif dat[0] == 'OFF':
                    grid[i][j] = False
                elif dat[0] == 'TOGGLE':
                    grid[i][j] = not grid[i][j]

    print(sum([sum(i) for i in grid]))

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    LEN = 1000
    grid = [[0 for _ in range(LEN)] for _ in range(LEN)]

    for dat in data:
        for i in range(dat[1][0], dat[2][0]+1):
            for j in range(dat[1][1], dat[2][1]+1):
                if dat[0] == 'ON':
                    grid[i][j] += 1
                elif dat[0] == 'OFF':
                    grid[i][j] = max(grid[i][j]-1, 0)
                elif dat[0] == 'TOGGLE':
                    grid[i][j] += 2

    print(sum([sum(i) for i in grid]))

if __name__ == '__main__':
    main()
    main2()
