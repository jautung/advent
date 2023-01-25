import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '18_dat.txt'
mapper = {}

def print_2d(array):
    for row in array:
        print(''.join(['#' if i else '.' for i in row]))
    print()

def main():
    data = readlines(FILENAME)
    data = [[i == '#' for i in list(dat)] for dat in data]

    # print_2d(data)
    for i in range(100):
        data = stepper(data)
        # print_2d(data)
    print(sum([sum(i) for i in data]))

def getter(data, i, j):
    if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
        return False
    else:
        return data[i][j]

def stepper(data):
    new_data = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data[i][j] = get_from_prev(data, i, j)
    return new_data

def get_from_prev(data, i, j):
    neighbors = [
        getter(data, i-1, j-1),
        getter(data, i-1, j),
        getter(data, i-1, j+1),
        getter(data, i, j-1),
        getter(data, i, j+1),
        getter(data, i+1, j-1),
        getter(data, i+1, j),
        getter(data, i+1, j+1),
    ]
    if getter(data, i, j):
        return sum(neighbors) == 2 or sum(neighbors) == 3
    else:
        return sum(neighbors) == 3

def main2():
    data = readlines(FILENAME)
    data = [[i == '#' for i in list(dat)] for dat in data]

    # print_2d(data)
    for i in range(100):
        data = stepper_2(data)
        # print_2d(data)
    print(sum([sum(i) for i in data]))

def stepper_2(data):
    new_data = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data[i][j] = get_from_prev_2(data, i, j)
    return new_data

def get_from_prev_2(data, i, j):
    if (i == 0 or i == len(data)-1) and (j == 0 or j == len(data[0])-1):
        return True
    neighbors = [
        getter(data, i-1, j-1),
        getter(data, i-1, j),
        getter(data, i-1, j+1),
        getter(data, i, j-1),
        getter(data, i, j+1),
        getter(data, i+1, j-1),
        getter(data, i+1, j),
        getter(data, i+1, j+1),
    ]
    if getter(data, i, j):
        return sum(neighbors) == 2 or sum(neighbors) == 3
    else:
        return sum(neighbors) == 3

if __name__ == '__main__':
    main()
    main2()
