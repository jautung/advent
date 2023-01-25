import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '1_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = list(data[0])
    floor = 0
    for char in data:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    print(floor)

def main2():
    data = readlines(FILENAME)
    data = list(data[0])
    floor = 0
    for i, char in enumerate(data):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
            if floor < 0:
                print(i+1)
                return

if __name__ == '__main__':
    main()
    main2()
