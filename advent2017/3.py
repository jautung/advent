import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '3_dat.txt'

def main():
    # KEY = 1024
    # KEY = 12
    KEY = 361527
    mapper = dict()
    i = 1
    while True:
        if i%2 == 0:
            mapper[i*i] = ((-int(i/2))+1,int(i/2))
        else:
            mapper[i*i] = (int(i/2),-int(i/2))
        # print(i*i)
        if i*i > KEY:
            i -= 1
            break
        i += 1
    # print(i, i*i, mapper[i*i])
    # print(i*i)
    if i%2 == 0:
        mapper[i*i+1] = add_tup(mapper[i*i], (-1,0))
        for k in range(1,i+1):
            # print('a', i*i+1+k)
            mapper[i*i+1+k] = add_tup(mapper[i*i+k], (0,-1))
        for k in range(1,i+1):
            # print('b', i*i+1+i+k)
            mapper[i*i+1+i+k] = add_tup(mapper[i*i+i+k], (1,0))
    else:
        mapper[i*i+1] = add_tup(mapper[i*i], (1,0))
        for k in range(1,i+1):
            mapper[i*i+1+k] = add_tup(mapper[i*i+k], (0,1))
        for k in range(1,i+2):
            mapper[i*i+1+i+k] = add_tup(mapper[i*i+i+k], (-1,0))
    # print(mapper)
    res = mapper[KEY]
    # print(mapper[KEY])
    print(abs(res[0])+abs(res[1]))


def add_tup(a,b):
    return (a[0]+b[0],a[1]+b[1])

def main2():
    KEY = 361527

    mapper = dict()
    mapper[(0,0)] = 1
    twice_steps = 2
    it = 0
    curr = (0,0)
    while True:
        direction = [(1,0),(0,1),(-1,0),(0,-1)][it%4]
        steps = int(twice_steps/2)
        twice_steps += 1
        for _ in range(steps):
            curr = add_tup(curr,direction)
            assert(curr not in mapper)
            mapper[curr] = find_val(curr,mapper)
            if mapper[curr] > KEY:
                print(mapper[curr])
                return
        # print(steps, direction)
        it += 1
        # if it == 15:
        #     return

def find_val(curr,mapper):
    neighbors = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1),
    ]
    res = 0
    for n in neighbors:
        if add_tup(curr, n) in mapper:
            res += mapper[add_tup(curr, n)]
    return res

if __name__ == '__main__':
    main()
    main2()
