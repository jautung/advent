import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '10_dat.txt'
mapper = {}

def main():
    line = '1113222113'
    # print(line)
    for _ in range(40):
        line = iter(line)
        # print(line)
    print(len(line))

def iter(line):
    res = ''
    while len(line) > 0:
        n, c = max_start(line)
        # print('a', line, n, c)
        res += str(n) + c
        line = line[n:]
    return res

def max_start(line):
    for i in range(1, len(line)+1):
        # print('z', line[:i])
        if len(set(list(line[:i]))) > 1:
            return i-1, line[0]
    return len(line), line[0]

def main2():
    line = '1113222113'
    # print(line)
    for _ in range(50):
        line = iter(line)
        # print(line)
    print(len(line))

if __name__ == '__main__':
    main()
    main2()
