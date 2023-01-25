import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '13_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    folds = data[1]
    data = [[int(i) for i in dat.split(',')] for dat in data[0]]

    # print(data)

    real_folds = []
    for fold in folds:
        line = fold.split()[-1]
        real_folds.append(line.split('='))

    # print(folds[0], folds[1])

    min_i = min(transpose(data)[0])
    max_i = max(transpose(data)[0])
    min_j = min(transpose(data)[1])
    max_j = max(transpose(data)[1])
    # print(min_i, min_j, max_i, max_j)

    grid = [[False for i in range(0, max_i+1)] for j in range(0, max_j+1)]
    for dat in data:
        # print(dat[1], dat[0])
        grid[dat[1]][dat[0]] = True
    
    # for i in grid:
    #     print(i)

    # print(real_folds[0])

    new_grid = do_fold(grid, real_folds[0])
    # new_grid = do_fold(new_grid, real_folds[1])
    tot = 0
    for i in new_grid:
        tot += sum(i)
    # print(sum(flatten([list(i) for i in new_grid])))
    print(tot)

# Time: 25:30

def do_fold(grid, fold):
    # for i in grid:
    #     print(i)
    # print()
    if fold[0] == 'y':
        line = int(fold[1])
        new_grid = dupe_array_with_def_value(grid, False)
        new_grid = new_grid[:line]
        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                new_grid[i][j] = grid[i][j]
        for i in range(line+1, len(grid)):
            for j in range(len(new_grid[0])):
                if grid[i][j]:
                    new_grid[line-i][j] = True
        return new_grid
    elif fold[0] == 'x':
        grid = transpose(grid)
        grid = do_fold(grid, ['y', fold[1]])
        return transpose(grid)

def main2():
    data = readlines_split_by_newlines(FILENAME)
    folds = data[1]
    data = [[int(i) for i in dat.split(',')] for dat in data[0]]

    # print(data)

    real_folds = []
    for fold in folds:
        line = fold.split()[-1]
        real_folds.append(line.split('='))

    # print(folds[0], folds[1])

    min_i = min(transpose(data)[0])
    max_i = max(transpose(data)[0])
    min_j = min(transpose(data)[1])
    max_j = max(transpose(data)[1])
    # print(min_i, min_j, max_i, max_j)

    grid = [[False for i in range(0, max_i+1)] for j in range(0, max_j+1)]
    for dat in data:
        # print(dat[1], dat[0])
        grid[dat[1]][dat[0]] = True
    
    # for i in grid:
    #     print(i)

    # print(real_folds[0])

    for real_fold in real_folds:
        grid = do_fold(grid, real_fold)
    for i in grid:
        print(''.join(['X' if j else ' ' for j in i]))

# Time: 28:08

if __name__ == '__main__':
    main()
    main2()
