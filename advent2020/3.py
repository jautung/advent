import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '3_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]

    count = 0

    row = 0
    col = 0
    while row < len(data):
        if data[row][col] == '#':
            count += 1
        row += 1
        col = (col+3)%len(data[0])
    # print_2d(data)
    print(count)

def main2():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]

    def get_count(dr,dc):
        count = 0

        row = 0
        col = 0
        while row < len(data):
            if data[row][col] == '#':
                count += 1
            row += dr
            col = (col+dc)%len(data[0])
        # print_2d(data)
        return count

    tests = [
        get_count(1,1),
        get_count(1,3),
        get_count(1,5),
        get_count(1,7),
        get_count(2,1),
    ]
    # print(tests)
    print(product(tests))

if __name__ == '__main__':
    main()
    main2()
