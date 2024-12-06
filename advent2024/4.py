import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print_2d(data)
    tot = 0

    def get_at(x,y):
        if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
            return None
        return data[y][x]

    def can_form_word(sx, sy, direc):
        dirx, diry = direc
        if get_at(sx, sy) != 'X':
            return False
        if get_at(sx + dirx, sy + diry) != 'M':
            return False
        if get_at(sx + 2 * dirx, sy + 2 * diry) != 'A':
            return False
        if get_at(sx + 3 * dirx, sy + 3 * diry) != 'S':
            return False
        return True

    for starting_y in range(len(data)):
        for starting_x in range(len(data[0])):
            if can_form_word(starting_y, starting_x, (0,1)):
                tot += 1
            if can_form_word(starting_y, starting_x, (0,-1)):
                tot += 1
            if can_form_word(starting_y, starting_x, (1,0)):
                tot += 1
            if can_form_word(starting_y, starting_x, (-1,0)):
                tot += 1
            if can_form_word(starting_y, starting_x, (1,1)):
                tot += 1
            if can_form_word(starting_y, starting_x, (-1,-1)):
                tot += 1
            if can_form_word(starting_y, starting_x, (-1,1)):
                tot += 1
            if can_form_word(starting_y, starting_x, (1,-1)):
                tot += 1
            # print(starting_y, starting_x)
    print(tot)


def main2():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print_2d(data)
    tot = 0

    def get_at(x,y):
        if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
            return None
        return data[y][x]

    def can_form_word(sx, sy, direc):
        dirx, diry = direc
        if get_at(sx, sy) != 'A':
            return False
        if get_at(sx + dirx, sy + diry) != 'S':
            return False
        if get_at(sx - dirx, sy - diry) != 'M':
            return False
        if get_at(sx - diry, sy + dirx) != 'S':
            return False
        if get_at(sx + diry, sy - dirx) != 'M':
            return False
        # print(sx, sy, direc)
        return True

    for starting_y in range(len(data)):
        for starting_x in range(len(data[0])):
            if can_form_word(starting_y, starting_x, (1,1)):
                tot += 1
            if can_form_word(starting_y, starting_x, (-1,-1)):
                tot += 1
            if can_form_word(starting_y, starting_x, (-1,1)):
                tot += 1
            if can_form_word(starting_y, starting_x, (1,-1)):
                tot += 1
            # print(starting_y, starting_x)
    print(tot)


if __name__ == '__main__':
    main()
    main2()
