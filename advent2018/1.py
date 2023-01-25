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
    print(sum(data))

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    curr = 0
    seen = set()
    seen.add(curr)
    while True:
        for i in data:
            curr += i
            if curr in seen:
                print(curr)
                return
            seen.add(curr)

if __name__ == '__main__':
    main()
    main2()
