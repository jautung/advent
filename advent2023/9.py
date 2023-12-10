import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '9_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(x) for x in dat.split()] for dat in data]
    s = 0
    for seq in data:
        # print()
        hist = proc(seq)
        # print(hist)
        extra(hist)
        # print(hist)
        # print(hist[0][-1])
        s += hist[0][-1]
    print(s)

def extra(hist):
    for k in range(len(hist)-1, -1, -1):
        r = hist[k]
        if k == len(hist)-1:
            r.append(0)
        else:
            r.append(r[-1] + hist[k+1][-1])

def proc(seq):
    hist = [seq]
    while True:
        seq = itera(seq)
        hist.append(seq)
        # print(seq)
        if all([a == 0 for a in seq]):
            return hist
            break
        
def itera(seq):
    return [seq[i+1] - seq[i] for i in range(len(seq)-1)]

def main2():
    data = readlines(FILENAME)
    data = [[int(x) for x in dat.split()] for dat in data]
    s = 0
    for seq in data:
        # print()
        hist = proc(seq)
        # print(hist)
        intra(hist)
        # print(hist)
        # print(hist[0][-1])
        s += hist[0][0]
    print(s)

def intra(hist):
    for k in range(len(hist)-1, -1, -1):
        r = hist[k]
        if k == len(hist)-1:
            r.insert(0, 0)
        else:
            r.insert(0, r[0] - hist[k+1][0])    

if __name__ == '__main__':
    main()
    main2()
