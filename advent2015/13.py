import sys 
sys.path.append('..')

import copy
import itertools
from collections import defaultdict
from helper import *

FILENAME = '13_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)

    knights = set()
    coeffs = dict()
    def parse(dat):
        knights.add(dat[0])
        knights.add(dat[10][:-1])        
        if dat[2] == 'gain':
            coeffs[(dat[0], dat[10][:-1])] = int(dat[3])
        elif dat[2] == 'lose':
            coeffs[(dat[0], dat[10][:-1])] = -int(dat[3])
        else:
            assert(False)
        # return dat[0], dat[2], int(dat[3]), dat[10][:-1]

    [parse(dat) for dat in data]

    knights = list(knights)
    # print(knights)
    # print(coeffs)

    def calc(l):
        happ = 0
        for i in range(len(l)):
            happ += coeffs[(l[i],l[(i-1)%len(l)])]
            happ += coeffs[(l[i],l[(i+1)%len(l)])]
        return happ

    max_happ = None
    for perm in itertools.permutations(knights[1:]):
        full_list = [knights[0]] + list(perm)
        points = calc(full_list)
        if max_happ == None or points > max_happ:
            max_happ = points
    print(max_happ)

def main2():
    data = readlines_split_each_line(FILENAME)

    knights = set()
    coeffs = dict()
    def parse(dat):
        knights.add(dat[0])
        knights.add(dat[10][:-1])        
        if dat[2] == 'gain':
            coeffs[(dat[0], dat[10][:-1])] = int(dat[3])
        elif dat[2] == 'lose':
            coeffs[(dat[0], dat[10][:-1])] = -int(dat[3])
        else:
            assert(False)
        # return dat[0], dat[2], int(dat[3]), dat[10][:-1]

    [parse(dat) for dat in data]

    knights = list(knights) + ['You']
    for k in knights:
        coeffs[('You', k)] = 0
        coeffs[(k, 'You')] = 0
    # print(knights)
    # print(coeffs)

    def calc(l):
        happ = 0
        for i in range(len(l)):
            happ += coeffs[(l[i],l[(i-1)%len(l)])]
            happ += coeffs[(l[i],l[(i+1)%len(l)])]
        return happ

    max_happ = None
    for perm in itertools.permutations(knights[1:]):
        full_list = [knights[0]] + list(perm)
        points = calc(full_list)
        if max_happ == None or points > max_happ:
            max_happ = points
    print(max_happ)

if __name__ == '__main__':
    main()
    main2()
