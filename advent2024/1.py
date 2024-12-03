import sys 
sys.path.append('..')

import copy
from collections import defaultdict, Counter
from helper import *

FILENAME = '1_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(x) for x in dat.split()] for dat in data]
    data = transpose(data)
    l0 = sorted(data[0])
    l1 = sorted(data[1])
    print(sum([abs(l0[i] - l1[i]) for i in range(len(l0))]))

def main2():
    data = readlines(FILENAME)
    data = [[int(x) for x in dat.split()] for dat in data]
    data = transpose(data)
    c = Counter(data[1])
    print(sum([d * c[d] for d in data[0]]))

if __name__ == '__main__':
    main()
    main2()
