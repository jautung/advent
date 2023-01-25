import sys 
sys.path.append('..')

import copy
import heapq
from collections import defaultdict
from helper import *

FILENAME = '12_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[ord(c) - ord('a') for c in list(dat)] for dat in data]

    s = find_pos(data, ord('S') - ord('a'))
    e = find_pos(data, ord('E') - ord('a'))
    data[s[0]][s[1]] = ord('a') - ord('a')
    data[e[0]][e[1]] = ord('z') - ord('a')
    # print_2d(data)
    # print(s, e)
    paths = [(0, s)]
    heapq.heapify(paths)
    added_to_heap = set([s])
    visited = set()
    while True:
        curr_steps, explore = heapq.heappop(paths)
        ns = valid_neighbors(explore, data)
        for n in ns:
            if n == e:
                # print('FOUND!')
                print(curr_steps + 1)
                return
            # if n in visited:
            #     continue
            if n in added_to_heap:
                continue
            heapq.heappush(paths, (curr_steps + 1, n))
            added_to_heap.add(n)
        # visited.add(explore)
        # print(len(visited))
        # if len(visited) % 100 == 0:
        #     print(len(visited))

def find_pos(data, num):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == num:
                return i, j
    assert(False)

def valid_neighbors(source, data):
    x, y = source
    res = []
    if x-1 >= 0 and data[x-1][y] <= data[x][y]+1:
        res.append((x-1, y))
    if x+1 < len(data) and data[x+1][y] <= data[x][y]+1:
        res.append((x+1, y))
    if y-1 >= 0 and data[x][y-1] <= data[x][y]+1:
        res.append((x, y-1))
    if y+1 < len(data[0]) and data[x][y+1] <= data[x][y]+1:
        res.append((x, y+1))
    return res

def main2():
    data = readlines(FILENAME)
    data = [[ord(c) - ord('a') for c in list(dat)] for dat in data]

    s = find_pos(data, ord('S') - ord('a'))
    e = find_pos(data, ord('E') - ord('a'))
    data[s[0]][s[1]] = ord('a') - ord('a')
    data[e[0]][e[1]] = ord('z') - ord('a')
    # print_2d(data)
    # print(s, e)

    min_so_far = None
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                test = find_min_length_from((i,j), data, e)
                # print(i, j, find_min_length_from((i,j), data, e))
                if test != None and (min_so_far == None or test < min_so_far):
                    min_so_far = test
    print(min_so_far)

def find_min_length_from(s, data, e):
    paths = [(0, s)]
    heapq.heapify(paths)
    added_to_heap = set([s])
    # visited = set()
    while True:
        try:
            curr_steps, explore = heapq.heappop(paths)
        except:
            return None
        ns = valid_neighbors(explore, data)
        for n in ns:
            if n == e:
                # print('FOUND!')
                # print(curr_steps + 1)
                return curr_steps + 1
            # if n in visited:
            #     continue
            if n in added_to_heap:
                continue
            heapq.heappush(paths, (curr_steps + 1, n))
            added_to_heap.add(n)
        # visited.add(explore)
        # print(len(visited))
        # if len(visited) % 100 == 0:
        #     print(len(visited))

if __name__ == '__main__':
    main()
    main2()
