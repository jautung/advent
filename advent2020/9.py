import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '9_dat.txt'
mapper = {}

# PREAM_LEN = 5
PREAM_LEN = 25

def check(num, lst):
    for l in lst:
        if num - l in lst:
            # print('yes')
            return None
    # print('no')
    return num
    return False

def main():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    for idx, num in enumerate(data):
        if idx < PREAM_LEN:
            continue
        x = check(num, copy.deepcopy(data[idx-PREAM_LEN:idx]))
        if x != None:
            print(x)
            return
    # print(data)

def attempt_sum(idx, data, final):
    l = 2
    while True:
        if final == sum(data[idx:idx+l]):
            # print(data[idx:idx+l])
            return data[idx:idx+l]
        elif final < sum(data[idx:idx+l]):
            break
        l += 1
    return None

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    final = None
    for idx, num in enumerate(data):
        if idx < PREAM_LEN:
            continue
        x = check(num, copy.deepcopy(data[idx-PREAM_LEN:idx]))
        if x != None:
            final = x
            break
    # print(data)
    for idx, num in enumerate(data):
        k = attempt_sum(idx, data, final)
        if k != None:
            print(max(k) + min(k))

if __name__ == '__main__':
    main()
    main2()
