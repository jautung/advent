import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [int(i) for i in data[0].split(',')]
    least = None
    least_target = None
    for target in range(min(data), max(data)):
        curr = align_fuel(data, target)
        if least_target is None or curr < least:
            least = curr
            least_target = target
    print(least, least_target)

def align_fuel(lst, final):
    total = 0
    for i in lst:
        total += abs(i - final)
    return total

def main2():
    data = readlines(FILENAME)
    data = [int(i) for i in data[0].split(',')]
    least = None
    least_target = None
    for target in range(min(data), max(data)):
        curr = align_fuel2(data, target)
        if least_target is None or curr < least:
            least = curr
            least_target = target
    print(least, least_target)

def align_fuel2(lst, final):
    total = 0
    for i in lst:
        dist = abs(i - final)
        total += (dist * (dist+1) // 2)
    return total

if __name__ == '__main__':
    main()
    main2()
