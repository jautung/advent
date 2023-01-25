import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '18_dat.txt'
mapper = {}

def parse(dat):
    return tuple([int(i) for i in dat.split(',')])

DIRS = [
    (0,0,1),
    (0,0,-1),
    (0,1,0),
    (0,-1,0),
    (1,0,0),
    (-1,0,0),
]

def main():
    data = readlines(FILENAME)
    data = set([parse(dat) for dat in data])
    # print_2d(data)

    count = 0
    for i in data:
        neighbors = [add_coord(i,d) for d in DIRS]
        count += sum([n not in data for n in neighbors])
    print(count)

def add_coord(a,b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

def main2():
    data = readlines(FILENAME)
    data = set([parse(dat) for dat in data])
    # print_2d(data)

    # xys = set([(d[0],d[1]) for d in data])
    # yzs = set([(d[1],d[2]) for d in data])
    # zxs = set([(d[2],d[0]) for d in data])
    # print(2 * (len(xys) + len(yzs) + len(zxs)))

    min_x = min([d[0] for d in data])
    max_x = max([d[0] for d in data])
    min_y = min([d[1] for d in data])
    max_y = max([d[1] for d in data])
    min_z = min([d[2] for d in data])
    max_z = max([d[2] for d in data])
    # print(min_x)
    # print(max_x)
    # print(min_y)
    # print(max_y)
    # print(min_z)
    # print(max_z)

    outside_corner = (min_x,min_y,min_z)
    assert(outside_corner not in data) # just happens to be true

    def in_bounds(pos):
        x,y,z = pos
        return x >= min_x and y >= min_y and z >= min_z and x <= max_x and y <= max_y and z <= max_z

    exterior = set()
    exterior.add(outside_corner)
    to_explore = [outside_corner]

    while len(to_explore) > 0:
        exploring = to_explore.pop()
        neighbors = [add_coord(exploring,d) for d in DIRS]
        for n in neighbors:
            if in_bounds(n) and n not in exterior and n not in data:
                exterior.add(n)
                to_explore.append(n)
    # print_2d(sorted(exterior))

    count = 0
    for i in data:
        neighbors = [add_coord(i,d) for d in DIRS]
        count += sum([not in_bounds(n) or n in exterior for n in neighbors])
    print(count)

if __name__ == '__main__':
    main()
    main2()
