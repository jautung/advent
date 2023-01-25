import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '1_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    data = [dat//3 - 2 for dat in data]
    print(sum(data))

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    data = [get_fuel(dat) for dat in data]
    print(sum(data))

def get_fuel(dat):
    total = 0
    curr = dat
    while True:
        curr = curr//3 - 2
        if curr <= 0:
            break
        total += curr
    return total

if __name__ == '__main__':
    main()
    main2()
