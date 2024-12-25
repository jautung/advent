import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '25_dat.txt'
mapper = {}

def parse_board(board):
    return [[k for k in a] for a in board]

def get_lock_repr(lock):
    l_t = transpose(lock)
    return [sum([1 for i in x if i == '#']) - 1 for x in l_t]

def get_key_repr(lock):
    l_t = transpose(lock)
    return [sum([1 for i in x if i == '#']) - 1 for x in l_t]

def main():
    data = readlines_split_by_newlines(FILENAME)
    data = [parse_board(dat) for dat in data]
    
    locks = []
    keys = []
    for board in data:
        # print_2d(board)
        if board[0] == ['#'] * len(board[0]) and board[-1] == ['.'] * len(board[-1]):
            locks.append(board)
        if board[0] == ['.'] * len(board[0]) and board[-1] == ['#'] * len(board[-1]):
            keys.append(board)
    
    # print('locks')
    lock_reprs = []
    for lock in locks:
        # print_2d(lock)
        lock_reprs.append(get_lock_repr(lock))

    # print('keys')
    key_reprs = []
    for key in keys:
        # print_2d(key)
        key_reprs.append(get_key_repr(key))

    # print('locks')
    # for r in lock_reprs:
    #     print(r)
    # print('keys')
    # for r in key_reprs:
    #     print(r)

    HEIGHT = len(locks[0]) - 2
    # print(HEIGHT)

    def non_overlap(l, k):
        return all([x + y <= HEIGHT for x, y in zip(l, k)])

    c = 0
    for l_r in lock_reprs:
        for k_r in key_reprs:
            if non_overlap(l_r, k_r):
                # print(l_r, k_r)
                c += 1
    print(c)


def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
