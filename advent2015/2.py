import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(i) for i in dat.split('x')] for dat in data]
    
    tot = 0
    for dat in data:
        a = dat[0]*dat[1]
        b = dat[0]*dat[2]
        c = dat[2]*dat[1]
        tot += 2 * (a + b + c) + min(a,b,c)
    print(tot)

def main2():
    data = readlines(FILENAME)
    data = [[int(i) for i in dat.split('x')] for dat in data]
    
    tot = 0
    for dat in data:
        a = dat[0]+dat[1]
        b = dat[0]+dat[2]
        c = dat[2]+dat[1]
        tot += 2 * min(a,b,c) + dat[0]*dat[1]*dat[2]
    print(tot)

if __name__ == '__main__':
    main()
    main2()
