import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '3_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    isnum = [[isint(char) for char in row] for row in data]
    # print(data)
    # print(isnum)
    numlocs = []
    for ridx, row in enumerate(data):
        # print(ridx, row)
        cidx = 0
        while cidx < len(row):
            if not isnum[ridx][cidx]:
                cidx += 1
                continue
            end_cidx = find_longest(cidx, isnum[ridx])
            numlocs.append((ridx, cidx, end_cidx, int(''.join(row[cidx:end_cidx+1]))))
            cidx = end_cidx + 1
    # print(numlocs)
    stufflocs = []
    for ridx, row in enumerate(data):
        for cidx, char in enumerate(row):
            if not isint(char) and char != '.':
                stufflocs.append((ridx, cidx, char))
    # print(stufflocs)
    tot = 0
    for nl in numlocs:
        next_to_stuff = False
        for sl in stufflocs:
            if is_adj(nl[0], nl[1], nl[2], sl[0], sl[1]):
                next_to_stuff = True
                break
        if next_to_stuff:
            tot += nl[3]
    print(tot)

def is_adj(ridx_nl, cidx_nl, end_cidx_nl, ridx_sl, cidx_sl):
    if abs(ridx_nl - ridx_sl) > 1:
        return False
    if cidx_sl < cidx_nl - 1:
        return False
    if cidx_sl > end_cidx_nl + 1:
        return False
    return True

def find_longest(cidx, row):
    while row[cidx]:
        cidx += 1
        if cidx == len(row):
            break
    return cidx - 1

def isint(char):
    try:
        int(char)
        return True
    except:
        return False

def main2():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    isnum = [[isint(char) for char in row] for row in data]
    # print(data)
    # print(isnum)
    numlocs = []
    for ridx, row in enumerate(data):
        # print(ridx, row)
        cidx = 0
        while cidx < len(row):
            if not isnum[ridx][cidx]:
                cidx += 1
                continue
            end_cidx = find_longest(cidx, isnum[ridx])
            numlocs.append((ridx, cidx, end_cidx, int(''.join(row[cidx:end_cidx+1]))))
            cidx = end_cidx + 1
    # print(numlocs)
    stufflocs = []
    for ridx, row in enumerate(data):
        for cidx, char in enumerate(row):
            if not isint(char) and char != '.':
                stufflocs.append((ridx, cidx, char))
    # print(stufflocs)
    tot = 0
    for sl in stufflocs:
        if sl[2] != '*':
            continue
        next_to_numlocs = []
        for nl in numlocs:
            if is_adj(nl[0], nl[1], nl[2], sl[0], sl[1]):
                next_to_numlocs.append(nl)
        if len(next_to_numlocs) == 2:
            tot += (next_to_numlocs[0][3] * next_to_numlocs[1][3])
    print(tot)

if __name__ == '__main__':
    main()
    main2()
