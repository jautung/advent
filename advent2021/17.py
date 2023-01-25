import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '17_dat.txt'
mapper = {}

# TARGET_MIN_X = 20
# TARGET_MAX_X = 30
# TARGET_MIN_Y = -10
# TARGET_MAX_Y = -5

TARGET_MIN_X = 209
TARGET_MAX_X = 238
TARGET_MIN_Y = -86
TARGET_MAX_Y = -59

def main():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)
    
    # for test_y in range(0,200):
        # positions = simulate(0,test_y)
        # positions_within_y = list(filter(lambda a: a[2] >= TARGET_MIN_Y and a[2] <= TARGET_MAX_Y, positions))
        # print(test_y, len(positions_within_y))
        # for pos in positions_within_y:
        #     print(pos)
    positions = simulate(0,85)
    positions_within_y = list(filter(lambda a: a[2] >= TARGET_MIN_Y and a[2] <= TARGET_MAX_Y, positions))
    # for pos in positions:
    #     print(pos)

def simulate(vx, vy):
    positions = [(0,0,0,vx,vy)]
    step = 0
    while True:
        step += 1
        _,x,y,vx,vy = positions[-1]
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        positions.append((step,x,y,vx,vy))
        if y < TARGET_MIN_Y:
            break
    return positions

# Time: 17:48

def main2():
    works = []
    for test_y in range(-150,100):
        positions = simulate(0,test_y)
        positions_within_y = list(filter(lambda a: a[2] >= TARGET_MIN_Y and a[2] <= TARGET_MAX_Y, positions))
        # print(test_y, len(positions_within_y))
        # for pos in positions_within_y:
        #     print(pos)
        if len(positions_within_y) > 0:
            for test_x in range(0,1000):
                positions = simulate(test_x,test_y)
                positions_within = list(filter(lambda a: a[2] >= TARGET_MIN_Y and a[2] <= TARGET_MAX_Y and a[1] >= TARGET_MIN_X and a[1] <= TARGET_MAX_X, positions))
                if len(positions_within) > 0:
                    # print(test_x, test_y)
                    works.append((test_x, test_y))
    print(len(works))

    # positions = simulate(0,85)
    # positions_within_y = list(filter(lambda a: a[2] >= TARGET_MIN_Y and a[2] <= TARGET_MAX_Y, positions))
    # for pos in positions:
    #     print(pos)

# Time: 24:21

if __name__ == '__main__':
    main()
    main2()
