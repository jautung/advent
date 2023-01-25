import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '25_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    # print('init')
    # print_dat(data)
    count = 0
    while True:
        count += 1
        prev_hash = hash_dat(data)
        data = step(data)
        if hash_dat(data) == prev_hash:
            print(count)
            break
        # print('after step', i)
        # print_dat(data)
    # data = step(data)

def hash_dat(data):
    return ''.join([''.join(row) for row in data])

def step(data):
    new = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '>':
                if data[i][(j+1) % len(data[0])] == '.':
                    new[i][(j+1) % len(data[0])] = '>'
                else:
                    new[i][j] = '>'
            elif data[i][j] == 'v':
                new[i][j] = 'v'
    new_2 = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
    for i in range(len(new)):
        for j in range(len(new[0])):
            if new[i][j] == 'v':
                if new[(i+1) % len(data)][j] == '.':
                    new_2[(i+1) % len(data)][j] = 'v'
                else:
                    new_2[i][j] = 'v'
            elif new[i][j] == '>':
                new_2[i][j] = '>'
    # print_dat(new_2)
    return new_2

def print_dat(data):
    for row in data:
        print(''.join(row))
    print()

# def getter(data, i, j):
#     i = i % len(data)
#     j = j % len(data[0])
#     return data[i][j]

# TIME: 19:08

def main2():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    # print('init')
    # print_dat(data)
    count = 0
    while True:
        count += 1
        prev_hash = hash_dat(data)
        data = step(data)
        if hash_dat(data) == prev_hash:
            print(count)
            break
        # print('after step', i)
        # print_dat(data)
    # data = step(data)

# TIME: NANI TF IS THIS CLIFFHANGER

if __name__ == '__main__':
    main()
    main2()
