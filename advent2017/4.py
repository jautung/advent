import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)
    print(sum([len(set(dat)) == len(dat) for dat in data]))
    # print(data)

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [[frozenset(d) for d in dat] for dat in data]
    print(sum([len(set(dat)) == len(dat) for dat in data]))
    # print(data)

if __name__ == '__main__':
    main()
    main2()
