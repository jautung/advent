import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    curr_pos = 0
    i = 0
    while True:
        read = data[curr_pos]
        data[curr_pos] += 1
        curr_pos += read
        # print(curr_pos, read, data)
        if curr_pos < 0 or curr_pos >= len(data):
            print(i+1)
            return
        i += 1
    # print(data)

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    curr_pos = 0
    i = 0
    while True:
        read = data[curr_pos]
        if data[curr_pos] >= 3:
            data[curr_pos] -= 1
        else:
            data[curr_pos] += 1
        curr_pos += read
        # print(curr_pos, read, data)
        if curr_pos < 0 or curr_pos >= len(data):
            print(i+1)
            return
        i += 1
    # print(data)

if __name__ == '__main__':
    main()
    main2()
