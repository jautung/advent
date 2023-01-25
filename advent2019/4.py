import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def main():
    # data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

    R_START = 234208
    R_END = 765869
    count = 0
    for p in range(R_START,R_END+1):
        if is_valid(p):
            count += 1
    print(count)

def is_valid(p):
    return is_valid_1(p) and is_valid_2(p)

def is_valid_1(p):
    s = str(p)
    return sum([len(set(s[i:i+2])) == 1 for i in range(len(s)-1)]) > 0

def is_valid_2(p):
    s = str(p)
    l = [int(i) for i in s]
    for i in range(len(s)-1):
        if l[i+1] < l[i]:
            return False
    return True

def main2():
    # data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

    R_START = 234208
    R_END = 765869
    count = 0
    for p in range(R_START,R_END+1):
        if is_new_valid(p):
            count += 1
    print(count)

    # test_p = 111122
    # print(is_new_valid(test_p))

def is_new_valid(p):
    return is_new_valid_1(p) and is_new_valid_2(p)

def is_new_valid_1(p):
    s = str(p)
    return sum([len(set(s[i:i+2])) == 1 and (i+1 == len(s)-1 or len(set(s[i:i+3])) > 1) and (i == 0 or len(set(s[i-1:i+2])) > 1) for i in range(len(s)-1)]) > 0

def is_new_valid_2(p):
    s = str(p)
    l = [int(i) for i in s]
    for i in range(len(s)-1):
        if l[i+1] < l[i]:
            return False
    return True

if __name__ == '__main__':
    main()
    main2()
