import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[[int(i) for i in j.split(',')] for j in dat.split(' -> ')] for dat in data]
    res = def_dict(0)
    for dat in data:
        s = dat[0]
        e = dat[1]
        if s[0] == e[0]:
            for i in range(min(s[1], e[1]), max(s[1], e[1]) + 1):
                res[(s[0], i)] += 1
        elif s[1] == e[1]:
            for i in range(min(s[0], e[0]), max(s[0], e[0]) + 1):
                res[(i, s[1])] += 1

    count = 0
    for item in res.items():
        if item[1] > 1:
            count += 1
    print(count)    

def main2():
    data = readlines(FILENAME)
    data = [[[int(i) for i in j.split(',')] for j in dat.split(' -> ')] for dat in data]
    res = def_dict(0)
    for dat in data:
        s = dat[0]
        e = dat[1]
        if s[0] == e[0]:
            for i in range(min(s[1], e[1]), max(s[1], e[1]) + 1):
                res[(s[0], i)] += 1
        elif s[1] == e[1]:
            for i in range(min(s[0], e[0]), max(s[0], e[0]) + 1):
                res[(i, s[1])] += 1
        elif s[0]-e[0] == s[1]-e[1]:
            if s[0] > e[0]:
                sm_x = e[0]
                lg_x = s[0]
                sm_y = e[1]
                lg_y = s[1]
            else:
                sm_x = s[0]
                lg_x = e[0]
                sm_y = s[1]
                lg_y = e[1]
            for i in range(0, lg_x - sm_x + 1):
                res[(sm_x + i, sm_y + i)] += 1
        elif s[0]-e[0] == e[1]-s[1]:
            if s[0] > e[0]:
                sm_x = e[0]
                lg_x = s[0]
                sm_y = s[1]
                lg_y = e[1]
            else:
                sm_x = s[0]
                lg_x = e[0]
                sm_y = e[1]
                lg_y = s[1]
            for i in range(0, lg_x - sm_x + 1):
                res[(sm_x + i, lg_y - i)] += 1

    count = 0
    for item in res.items():
        if item[1] > 1:
            count += 1
    print(count)    

if __name__ == '__main__':
    main()
    main2()
