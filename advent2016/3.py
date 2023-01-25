import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '3_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)
    data = [[int(i) for i in dat] for dat in data]
    
    # print_2d(data)
    print(sum([is_tri(t) for t in data]))

def is_tri(t):
    return t[0]+t[1] > t[2] and t[1]+t[2] > t[0] and t[2]+t[0] > t[1]

def main2():
    data = readlines_partitioned(FILENAME, 3)
    data = [transpose([[int(i) for i in line.strip('\n').split()] for line in big_dat]) for big_dat in data]
    data = flatten(data)
    # data = [[int(i) for i in dat] for dat in data]
    
    # print_2d(data)
    print(sum([is_tri(t) for t in data]))

if __name__ == '__main__':
    main()
    main2()
