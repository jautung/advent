import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {}

def is_invalid_id(num):
    s = str(num)
    l = len(s)
    if l % 2 != 0:
        return False
    return s[:l//2] == s[l//2:]

def main():
    data = readlines(FILENAME)
    data = ''.join(data)
    ranges = [[int(a) for a in x.split('-')] for x in data.split(',')]
    # print(ranges)
    c = 0
    for r in ranges:
        s = r[0]
        e = r[1]
        for x in range(s, e+1):
            if is_invalid_id(x):
                c += x
                # print(x)
    print(c)

def is_invalid_id_divisor(num, div):
    s = str(num)
    l = len(s)
    if l % div != 0:
        return False
    substr_len = l//div
    matcher = s[:substr_len]
    for index in range(div):
        if s[index * substr_len:(index+1) * substr_len] != matcher:
            return False
    return True

def is_invalid_id_2(num):
    s = str(num)
    for div in range(2, len(s)+1):
        if is_invalid_id_divisor(num, div):
            # print(num, div)
            return True
    return False

def main2():
    data = readlines(FILENAME)
    data = ''.join(data)
    ranges = [[int(a) for a in x.split('-')] for x in data.split(',')]
    # print(ranges)
    c = 0
    for r in ranges:
        s = r[0]
        e = r[1]
        for x in range(s, e+1):
            if is_invalid_id_2(x):
                c += x
                # print(x)
    print(c)

if __name__ == '__main__':
    main()
    main2()
