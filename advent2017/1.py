import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '1_dat.txt'
mapper = {}

def main():
    data = [int(i) for i in readlines(FILENAME)[0]]
    # data = [int(dat) for dat in data]
    # print(data)
    count = 0
    for i in range(len(data)):
        t = data[i]
        n = data[(i+1)%len(data)]
        if t == n:
            count += t
    print(count)

def main2():
    data = [int(i) for i in readlines(FILENAME)[0]]
    # data = [int(dat) for dat in data]
    # print(data)
    count = 0
    for i in range(len(data)):
        t = data[i]
        n = data[(i+len(data)//2)%len(data)]
        if t == n:
            count += t
    print(count)

if __name__ == '__main__':
    main()
    main2()
