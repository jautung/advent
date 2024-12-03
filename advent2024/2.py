import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(d) for d in dat.split()] for dat in data]
    # print_2d(data)
    c = 0
    for row in data:
        # print(is_safe(row))
        c += 1 if is_safe(row) else 0
    print(c)

def is_safe(lst):
    a = sorted(lst, reverse=True)
    b = sorted(lst)

    if lst != a and lst != b:
        # print("updown")
        return False

    a = None
    for i in lst:
        if a is None:
            a = i
            continue
        if abs(i-a) != 1 and abs(i-a) != 2 and abs(i-a) != 3:
            # print("BEG")
            return False
        a = i
    return True

def main2():
    data = readlines(FILENAME)
    data = [[int(d) for d in dat.split()] for dat in data]
    # print_2d(data)
    c = 0
    for row in data:
        # print(can_be_safe(row))
        c += 1 if can_be_safe(row) else 0
    print(c)

def can_be_safe(lst):
    if is_safe(lst):
        return True
    for i in range(len(lst)):
        if is_safe(lst[:i] + lst[i+1:]):
            return True
    return False

if __name__ == '__main__':
    main()
    main2()
