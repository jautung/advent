import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '1_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)[0]
    data = [d.strip(',') for d in data]
    start = (0,0)
    direction = (0,1)
    for d in data:
        step = int(d[1:])
        # print(start, step, direction, direction*step)
        if d[0] == 'R':
            direction = rotate_r(direction)
            start = add_tup(start,scale_tup(direction,step))
        elif d[0] == 'L':
            direction = rotate_l(direction)
            start = add_tup(start,scale_tup(direction,step))
    # print(start)
    print(abs(start[0])+abs(start[1]))

def add_tup(a,b):
    return (a[0]+b[0],a[1]+b[1])

def scale_tup(x,s):
    return (x[0]*s,x[1]*s)

def rotate_r(d):
    if d == (0,1):
        return (1,0)
    elif d == (1,0):
        return (0,-1)
    elif d == (0,-1):
        return (-1,0)
    elif d == (-1,0):
        return (0,1)

def rotate_l(d):
    if d == (0,1):
        return (-1,0)
    elif d == (1,0):
        return (0,1)
    elif d == (0,-1):
        return (1,0)
    elif d == (-1,0):
        return (0,-1)

def main2():
    data = readlines_split_each_line(FILENAME)[0]
    data = [d.strip(',') for d in data]
    start = (0,0)
    direction = (0,1)
    visited = set()
    visited.add(start)
    for d in data:
        step = int(d[1:])
        # print(start, step, direction, direction*step)
        if d[0] == 'R':
            direction = rotate_r(direction)
            for _ in range(step):
                start = add_tup(start,direction)
                if start in visited:
                    # print(start)
                    print(abs(start[0])+abs(start[1]))
                    return
                visited.add(start)
        elif d[0] == 'L':
            direction = rotate_l(direction)
            for _ in range(step):
                start = add_tup(start,direction)
                if start in visited:
                    # print(start)
                    print(abs(start[0])+abs(start[1]))
                    return
                visited.add(start)






# FACTORS = ((0, 1),   # turning right, N
#            (1, 0),   # E
#            (0, -1),  # S
#            (-1, 0)   # W
#            )
# DIRF = {'R': lambda x: (x+1) % 4,
#         'L': lambda x: (x-1) % 4
#         }


# def main3():
#     current_dir = 0  # facing north
#     loc = (0, 0)
#     line = readlines(FILENAME)[0]
#     for turn in [x.strip() for x in line.split(',')]:
#         # print(turn)
#         d, c = turn[0], int(turn[1:])
#         current_dir = DIRF[d](current_dir)
#         loc = (loc[0] + FACTORS[current_dir][0] * c,
#                loc[1] + FACTORS[current_dir][1] * c)

#     print(loc)
#     print('DIST: %d' % (abs(loc[0]) + abs(loc[1])))





if __name__ == '__main__':
    main()
    # main3()
    main2()



