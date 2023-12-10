import math
import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
# mapper = {}

def main():
    data = readlines(FILENAME)
    lrs = [c for c in data[0]]
    map_edges = [parse(e) for e in data[2:]]
    # data = [int(dat) for dat in data]
    # print(lrs)
    # print(map_edges)
    mapper = dict()
    for m in map_edges:
        s, l, r = m
        mapper[s] = {'L': l, 'R': r}
    # print(mapper)
    steps = 0
    curr = 'AAA'
    while True:
        if curr == 'ZZZ':
            print(steps)
            return
        mov = lrs[steps % len(lrs)]
        curr = mapper[curr][mov]
        steps += 1

def parse(e):
    a = e.split('=')
    s = a[0].strip()
    choices = a[1].split(',')
    l = choices[0].strip().strip('(').strip(')')
    r = choices[1].strip().strip('(').strip(')')
    return s, l, r

def main2():
    data = readlines(FILENAME)
    lrs = [c for c in data[0]]
    map_edges = [parse(e) for e in data[2:]]
    # data = [int(dat) for dat in data]
    # print(lrs)
    # print(map_edges)
    mapper = dict()
    starts = []
    for m in map_edges:
        s, l, r = m
        if s.endswith('A'):
            starts.append(s)
        mapper[s] = {'L': l, 'R': r}
    # print(mapper)
    # print(starts)
    # steps = 0
    # # curr = 'AAA'
    # while True:
    #     # if steps % 10000 == 0:
    #     #     print(steps)
    #     if all([c.endswith('Z') for c in starts]):
    #         print(steps)
    #         return
    #     mov = lrs[steps % len(lrs)]
    #     starts = [mapper[s][mov] for s in starts]
    #     steps += 1
    mults = []
    # print(starts)
    for curr in starts:
        steps = 0
        while True:
            if curr.endswith('Z'):
                # print(steps)
                mults.append(steps)
                break
            mov = lrs[steps % len(lrs)]
            curr = mapper[curr][mov]
            steps += 1
    print(math.lcm(*mults))

if __name__ == '__main__':
    main()
    main2()
