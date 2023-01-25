import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '9_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(i) for i in list(dat)] for dat in data]

    def get(i, j):
        if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
            return None
        else:
            return data[i][j]
    
    count = 0
    risk = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            neighbors = [get(i-1, j), get(i+1, j), get(i, j-1), get(i, j+1)]
            neighbors = list(filter(lambda x: x != None, neighbors))
            if data[i][j] < min(neighbors):
                count += 1
                risk += (data[i][j] + 1)
    print(risk)

# Time: 6:02

def main2():
    data = readlines(FILENAME)
    data = [[int(i) for i in list(dat)] for dat in data]

    def get(i, j):
        if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
            return None
        else:
            return data[i][j]
    
    basin_roots = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            neighbors = [get(i-1, j), get(i+1, j), get(i, j-1), get(i, j+1)]
            neighbors = list(filter(lambda x: x != None, neighbors))
            if data[i][j] < min(neighbors):
                basin_roots.append((i, j))

    def grow_basin(basin):
        new_basin = set()
        for i, j in basin:
            if ((i-1, j) not in basin) and get(i-1, j) != None and get(i-1, j) != 9:
                new_basin.add((i-1, j))
            if ((i+1, j) not in basin) and get(i+1, j) != None and get(i+1, j) != 9:
                new_basin.add((i+1, j))
            if ((i, j-1) not in basin) and get(i, j-1) != None and get(i, j-1) != 9:
                new_basin.add((i, j-1))
            if ((i, j+1) not in basin) and get(i, j+1) != None and get(i, j+1) != 9:
                new_basin.add((i, j+1))
        return new_basin.union(basin)

    def max_basin(basin_root):
        basin = set([basin_root])
        while True:
            new_basin = grow_basin(basin)
            if new_basin == basin:
                return basin
            basin = new_basin

    basins = [max_basin(basin_root) for basin_root in basin_roots]
    sizes = [len(i) for i in basins]
    sizes = sorted(sizes)
    print(sizes[-1] * sizes[-2] * sizes[-3])

# Time: 19:58

if __name__ == '__main__':
    main()
    main2()
