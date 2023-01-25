import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '11_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(i) for i in list(dat)] for dat in data]
    total_flashes = 0
    for i in range(100):
        # print('step', i)
        # for i in data:
        #     print(i)
        data, flashes = step(data)
        total_flashes += flashes
    # print('final')
    # for i in data:
    #     print(i)
    print(total_flashes)

def step(data):
    data = [[i + 1 for i in dat] for dat in data]
    flashed = [[False] * len(data[0]) for i in range(len(data))]

    def in_bounds(i, j):
        return i >= 0 and j >= 0 and i < len(data) and j < len(data[0])

    def incr_if_in_bounds(i, j):
        if in_bounds(i, j):
            data[i][j] += 1

    def flash(i, j):
        if flashed[i][j]:
            return
        incr_if_in_bounds(i-1, j-1)
        incr_if_in_bounds(i, j-1)
        incr_if_in_bounds(i+1, j-1)
        incr_if_in_bounds(i-1, j)
        incr_if_in_bounds(i, j)
        incr_if_in_bounds(i+1, j)
        incr_if_in_bounds(i-1, j+1)
        incr_if_in_bounds(i, j+1)
        incr_if_in_bounds(i+1, j+1)
        flashed[i][j] = True

    while True:
        prev_flashed = copy.deepcopy(flashed)
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] > 9:
                    flash(i, j)
        if sum([sum(i) for i in prev_flashed]) == sum([sum(i) for i in flashed]):
            break

    data = [[i if i <= 9 else 0 for i in dat] for dat in data]

    return data, sum([sum(i) for i in flashed])

# Time: 20:47

def main2():
    data = readlines(FILENAME)
    data = [[int(i) for i in list(dat)] for dat in data]
    i = 0
    while True:
        i += 1
        # print('step', i)
        # for i in data:
        #     print(i)
        data, flashes = step(data)
        if flashes == len(data) * len(data[0]):
            break
    # print('final')
    # for i in data:
    #     print(i)
    print(i)

# Time: 22:35

if __name__ == '__main__':
    main()
    main2()
