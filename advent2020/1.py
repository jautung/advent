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
    for i in data:
        for j in data:
            if i + j == 2020:
                print(i*j)
                return
    # print(data)

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    print(i*j*k)
                    return
    # print(data)


if __name__ == '__main__':
    main()
    main2()
