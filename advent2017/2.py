import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)
    data = [[int(i) for i in dat] for dat in data]
    data = [max(dat)-min(dat) for dat in data]
    print(sum(data))

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [[int(i) for i in dat] for dat in data]
    data = [dividing(dat) for dat in data]
    # print_2d(data)
    print(sum(data))

def dividing(l):
    for i in l:
        for j in l:
            if i%j == 0 and i != j:
                return i//j

if __name__ == '__main__':
    main()
    main2()
