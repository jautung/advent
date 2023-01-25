import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(i) for i in list(dat)] for dat in data]

    def is_visible(i, j):
        return is_visible_1(i, j) or is_visible_2(i, j) or is_visible_3(i, j) or is_visible_4(i, j)

    def is_visible_1(i, j):
        for i_iter in range(i-1, -1, -1):
            if data[i_iter][j] >= data[i][j]:
                return False
        return True

    def is_visible_2(i, j):
        for i_iter in range(i+1, len(data), 1):
            if data[i_iter][j] >= data[i][j]:
                return False
        return True

    def is_visible_3(i, j):
        for j_iter in range(j-1, -1, -1):
            if data[i][j_iter] >= data[i][j]:
                return False
        return True

    def is_visible_4(i, j):
        for j_iter in range(j+1, len(data[0]), 1):
            if data[i][j_iter] >= data[i][j]:
                return False
        return True

    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            # print(i,j,is_visible(i,j))
            if is_visible(i, j):
                count += 1
    # print_2d(data)
    print(count)

def main2():
    data = readlines(FILENAME)
    data = [[int(i) for i in list(dat)] for dat in data]

    def is_visible(i, j):
        return is_visible_1(i, j) * is_visible_2(i, j) * is_visible_3(i, j) * is_visible_4(i, j)

    def is_visible_1(i, j):
        count = 0
        for i_iter in range(i-1, -1, -1):
            count += 1
            if data[i_iter][j] >= data[i][j]:
                return count
        return count

    def is_visible_2(i, j):
        count = 0
        for i_iter in range(i+1, len(data), 1):
            count += 1
            if data[i_iter][j] >= data[i][j]:
                return count
        return count

    def is_visible_3(i, j):
        count = 0
        for j_iter in range(j-1, -1, -1):
            count += 1
            if data[i][j_iter] >= data[i][j]:
                return count
        return count

    def is_visible_4(i, j):
        count = 0
        for j_iter in range(j+1, len(data[0]), 1):
            count += 1
            if data[i][j_iter] >= data[i][j]:
                return count
        return count

    res = None
    for i in range(len(data)):
        for j in range(len(data[0])):
            # print(i,j,is_visible(i,j))
            if res == None or is_visible(i,j) > res:
                res = is_visible(i,j)
    # print_2d(data)
    print(res)

if __name__ == '__main__':
    main()
    main2()
