import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

CARDINALS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print_2d(data)

    def get_at(x, y):
        if x < 0 or y < 0 or y >= len(data) or x >= len(data[0]):
            return False
        return data[y][x] == "@"

    # print(get_at(2,0))
    count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if not get_at(x,y):
                continue
            num_neighs = 0
            for c in CARDINALS:
                neighbor = add_tup((x,y), c)
                n_x, n_y = neighbor
                num_neighs += 1 if get_at(n_x, n_y) else 0
            if num_neighs < 4:
                # print((x,y))
                count += 1
    print(count)

def iter_remove(data):
    def get_at(x, y):
        if x < 0 or y < 0 or y >= len(data) or x >= len(data[0]):
            return False
        return data[y][x] == "@"

    # print(get_at(2,0))
    for y in range(len(data)):
        for x in range(len(data[0])):
            if not get_at(x,y):
                continue
            num_neighs = 0
            for c in CARDINALS:
                neighbor = add_tup((x,y), c)
                n_x, n_y = neighbor
                num_neighs += 1 if get_at(n_x, n_y) else 0
            if num_neighs < 4:
                # print((x,y))
                # count += 1
                data[y][x] = "."
    # print(count)

def num_bales(data):
    count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "@":
                count += 1
    return count

def main2():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    init_num = num_bales(data)
    prev_num = None
    while True:
        iter_remove(data)
        new_num = num_bales(data)
        # print(new_num)
        if new_num == prev_num:
            break
        prev_num = new_num
    print(init_num - new_num)

if __name__ == '__main__':
    main()
    main2()
