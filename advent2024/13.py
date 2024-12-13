import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '13_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    def parse(grp):
        assert len(grp) == 3
        a_thing = grp[0]
        a_sides = a_thing.split(':')[1].strip().split(',')
        a_x = int(a_sides[0].split('+')[1].strip())
        a_y = int(a_sides[1].split('+')[1].strip())
        b_thing = grp[1]
        b_sides = b_thing.split(':')[1].strip().split(',')
        b_x = int(b_sides[0].split('+')[1].strip())
        b_y = int(b_sides[1].split('+')[1].strip())
        prizes_thing = grp[2]
        prizes_sides = prizes_thing.split(':')[1].strip().split(',')
        prizes_x = int(prizes_sides[0].split('=')[1].strip())
        prizes_y = int(prizes_sides[1].split('=')[1].strip())
        return ((a_x, a_y), (b_x, b_y), (prizes_x, prizes_y))
    data = [parse(dat) for dat in data]
    # print(data)
    LIMIT = 100
    def combinations(a, b, p):
        res = []
        for maybe_a_count in range(LIMIT+1):
            already_x = a[0] * maybe_a_count
            already_y = a[1] * maybe_a_count
            remaining_x = p[0] - already_x
            remaining_y = p[1] - already_y
            if remaining_x % b[0] != 0:
                continue
            if remaining_y % b[1] != 0:
                continue
            maybe_b_1 = remaining_x // b[0]
            maybe_b_2 = remaining_y // b[1]
            if maybe_b_1 != maybe_b_2:
                continue
            res.append((maybe_a_count, maybe_b_1, 3*maybe_a_count + maybe_b_1))
        return res
    whee = 0
    for config in data:
        # print(config, combinations(config[0], config[1], config[2]))
        cs = combinations(config[0], config[1], config[2])
        if len(cs) == 0:
            continue
        whee += min([a[2] for a in cs])
    print(whee)
    

def main2():
    data = readlines_split_by_newlines(FILENAME)
    def parse(grp):
        assert len(grp) == 3
        a_thing = grp[0]
        a_sides = a_thing.split(':')[1].strip().split(',')
        a_x = int(a_sides[0].split('+')[1].strip())
        a_y = int(a_sides[1].split('+')[1].strip())
        b_thing = grp[1]
        b_sides = b_thing.split(':')[1].strip().split(',')
        b_x = int(b_sides[0].split('+')[1].strip())
        b_y = int(b_sides[1].split('+')[1].strip())
        prizes_thing = grp[2]
        prizes_sides = prizes_thing.split(':')[1].strip().split(',')
        prizes_x = int(prizes_sides[0].split('=')[1].strip())
        prizes_y = int(prizes_sides[1].split('=')[1].strip())
        return ((a_x, a_y), (b_x, b_y), (prizes_x+10000000000000, prizes_y+10000000000000))
    data = [parse(dat) for dat in data]
    # print(data)
    # LIMIT = 100
    """
    A * x_a y_a
    B * x_b y_b
    ==
    x_p, y_p

    need A * x_a + B * x_b == x_p
    need A * y_a + B * y_b == y_p

    solve for A and B (and they need to be both nonnegative integers at the end)

    need A * x_a * y_a + B * x_b * y_a == x_p * y_a
    need A * x_a * y_a + B * x_a * y_b == x_a * y_p
    B = (x_p * y_a - x_a * y_p) // (x_b * y_a - x_a * y_b)
    """
    def combinations(a, b, p):
        x_a = a[0]
        y_a = a[1]
        x_b = b[0]
        y_b = b[1]
        x_p = p[0]
        y_p = p[1]
        if (x_p * y_a - x_a * y_p) % (x_b * y_a - x_a * y_b) != 0:
            return []
        if (x_p * y_b - x_b * y_p) % (x_a * y_b - x_b * y_a) != 0:
            return []
        maybe_a_count = (x_p * y_b - x_b * y_p) // (x_a * y_b - x_b * y_a)
        maybe_b_count = (x_p * y_a - x_a * y_p) // (x_b * y_a - x_a * y_b)
        return [(maybe_a_count, maybe_b_count, 3*maybe_a_count + maybe_b_count)]
    whee = 0
    for config in data:
        # print(config, combinations(config[0], config[1], config[2]))
        cs = combinations(config[0], config[1], config[2])
        if len(cs) == 0:
            continue
        whee += min([a[2] for a in cs])
    print(whee)

if __name__ == '__main__':
    main()
    main2()
