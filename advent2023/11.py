import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '11_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    n_row = len(data)
    n_col = len(data[0])
    coords = []
    for r in range(n_row):
        for c in range(n_col):
            if data[r][c] == '#':
                coords.append((r,c))
    # print(n_row, n_col, coords)
    empty_row_indices = []
    for r in range(n_row):
        if all([data[r][c] == '.' for c in range(n_col)]):
            empty_row_indices.append(r)
    empty_col_indices = []
    for c in range(n_col):
        if all([data[r][c] == '.' for r in range(n_row)]):
            empty_col_indices.append(c)
    # print(empty_row_indices)
    # print(empty_col_indices)
    n_galaxies = len(coords)
    
    d_sum = 0
    for galaxy_i_1 in range(n_galaxies):
        for galaxy_i_2 in range(galaxy_i_1+1, n_galaxies):
            # print(galaxy_i_1, galaxy_i_2)
            # print(coords[galaxy_i_1], coords[galaxy_i_2])
            d = get_dist(coords[galaxy_i_1], coords[galaxy_i_2], empty_row_indices, empty_col_indices)
            d_sum += d
            # print(coords[galaxy_i_1], coords[galaxy_i_2], d)
    print(d_sum)

def get_dist(coord_1, coord_2, empty_row_indices, empty_col_indices, space_mult=2):
    r_1, c_1 = coord_1
    r_2, c_2 = coord_2
    base_distance = abs(r_1-r_2) + abs(c_1-c_2)
    r_max = max(r_1, r_2)
    r_min = min(r_1, r_2)
    c_max = max(c_1, c_2)
    c_min = min(c_1, c_2)
    empty_r_inside = len([a for a in empty_row_indices if a > r_min and a < r_max])
    empty_c_inside = len([a for a in empty_col_indices if a > c_min and a < c_max])
    return base_distance + (space_mult-1)*(empty_r_inside+empty_c_inside)

def main2():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    n_row = len(data)
    n_col = len(data[0])
    coords = []
    for r in range(n_row):
        for c in range(n_col):
            if data[r][c] == '#':
                coords.append((r,c))
    # print(n_row, n_col, coords)
    empty_row_indices = []
    for r in range(n_row):
        if all([data[r][c] == '.' for c in range(n_col)]):
            empty_row_indices.append(r)
    empty_col_indices = []
    for c in range(n_col):
        if all([data[r][c] == '.' for r in range(n_row)]):
            empty_col_indices.append(c)
    # print(empty_row_indices)
    # print(empty_col_indices)
    n_galaxies = len(coords)
    
    d_sum = 0
    for galaxy_i_1 in range(n_galaxies):
        for galaxy_i_2 in range(galaxy_i_1+1, n_galaxies):
            # print(galaxy_i_1, galaxy_i_2)
            # print(coords[galaxy_i_1], coords[galaxy_i_2])
            d = get_dist(coords[galaxy_i_1], coords[galaxy_i_2], empty_row_indices, empty_col_indices, space_mult=1000000)
            d_sum += d
            # print(coords[galaxy_i_1], coords[galaxy_i_2], d)
    print(d_sum)

if __name__ == '__main__':
    main()
    main2()
