import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = data[0]
    for i in range(4, len(data)):
        four = data[i-4:i]
        if len(set(four)) == 4:
            print(i)
            return
    # print(data)

def main2():
    data = readlines(FILENAME)
    data = data[0]
    for i in range(14, len(data)):
        four = data[i-14:i]
        if len(set(four)) == 14:
            print(i)
            return
    # print(data)

if __name__ == '__main__':
    main()
    main2()
    # data = readlines(FILENAME)
    # data = data[0]
    # n = 4
    # print([len(set(data[i-n:i])) for i in range(n, len(data))].index(n)+n)
