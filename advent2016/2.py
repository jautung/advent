import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {
    (0,0): 5,
    (1,0): 6,
    (-1,0): 4,
    (0,1): 2,
    (1,1): 3,
    (-1,1): 1,
    (0,-1): 8,
    (1,-1): 9,
    (-1,-1): 7,
}

def main():
    data = readlines(FILENAME)
    start = (0,0)
    final = []
    for line in data:
        for c in list(line):
            if c == 'U':
                new_start = add_tup(start,(0,1))
                if new_start in mapper:
                    start = new_start
            elif c == 'D':
                new_start = add_tup(start,(0,-1))
                if new_start in mapper:
                    start = new_start
            elif c == 'L':
                new_start = add_tup(start,(-1,0))
                if new_start in mapper:
                    start = new_start
            elif c == 'R':
                new_start = add_tup(start,(1,0))
                if new_start in mapper:
                    start = new_start
        # print(mapper[start])
        final.append(mapper[start])
    # print(data)
    print(''.join([str(i) for i in final]))

def add_tup(a,b):
    return (a[0]+b[0],a[1]+b[1])

mapper_2 = {
    (0,0): '5',
    (1,0): '6',
    (2,0): '7',
    (3,0): '8',
    (4,0): '9',
    (1,1): '2',
    (2,1): '3',
    (3,1): '4',
    (2,2): '1',
    (1,-1): 'A',
    (2,-1): 'B',
    (3,-1): 'C',
    (2,-2): 'D',
}

def main2():
    data = readlines(FILENAME)
    start = (0,0)
    final = []
    for line in data:
        for c in list(line):
            if c == 'U':
                new_start = add_tup(start,(0,1))
                if new_start in mapper_2:
                    start = new_start
            elif c == 'D':
                new_start = add_tup(start,(0,-1))
                if new_start in mapper_2:
                    start = new_start
            elif c == 'L':
                new_start = add_tup(start,(-1,0))
                if new_start in mapper_2:
                    start = new_start
            elif c == 'R':
                new_start = add_tup(start,(1,0))
                if new_start in mapper_2:
                    start = new_start
        # print(mapper_2[start])
        final.append(mapper_2[start])
    # print(data)
    print(''.join([str(i) for i in final]))

if __name__ == '__main__':
    main()
    main2()
