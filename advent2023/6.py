import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    x = [int(a) for a in data[0].split()[1:]]
    y = [int(a) for a in data[1].split()[1:]]
    races = []
    for i in range(len(x)):
        races.append((x[i], y[i]))
    # print(x, y)
    # print(races)
    x = 1
    for race in races:
        n_win = proc(race)
        x *= n_win
        # print(n_win)
    print(x)

def proc(race):
    t = race[0]
    d = race[1]
    count = 0
    for i in range(t + 1):
        if i * (t-i) > d:
            count += 1
    return count
        
def main2():
    data = readlines(FILENAME)
    x = int(data[0].split(':')[1].replace(" ", ""))
    y = int(data[1].split(':')[1].replace(" ", ""))
    # print(x)
    # print(y)
    # races = []
    # for i in range(len(x)):
    #     races.append((x[i], y[i]))
    # # print(x, y)
    # # print(races)
    # x = 1
    # for race in races:
    n_win = proc_binary((x, y))
    print(n_win)
    #     x *= n_win
    #     # print(n_win)
    # print(x)

def proc_binary(race):
    t = race[0]
    d = race[1]
    count = 0
    # 0, 1, 2, ... t/2 are possible cutoffs
    lower = 0
    upper = t//2 + 2
    # test_val = (lower + upper) // 2
    res = bin_search(t, d, lower, upper)
    return t - (res * 2) - 1

def bin_search(t, d, lower, upper):
    if upper - lower < 5:
        for i in range(lower, upper+1):
            if i * (t-i) > d:
                return i - 1
    test_val = (lower + upper) // 2
    if test_val * (t-test_val) > d:
        # lower returns false
        # upper returns true on this
        return bin_search(t, d, lower, test_val + 1)
    else:
        return bin_search(t, d, test_val - 1, upper)

if __name__ == '__main__':
    main()
    main2()
