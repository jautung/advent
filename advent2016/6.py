import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    data = transpose(data)
    # print_2d(data)
    data = [most_common(a) for a in data]
    print(''.join(data))

def main2():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    data = transpose(data)
    # print_2d(data)
    data = [least_common(a) for a in data]
    print(''.join(data))

if __name__ == '__main__':
    main()
    main2()
