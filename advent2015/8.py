import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [solve(dat) for dat in data]
    data_t = transpose(data)
    print(sum(data_t[0]) - sum(data_t[1]))

def solve(line):
    actual = line[1:-1]
    count = 0
    i = 0
    while i < len(actual):
        if actual[i] != '\\':
            count += 1
            i += 1
        else:
            if actual[i+1] == '\\':
                count += 1
                i += 2
            elif actual[i+1] == '\"':
                count += 1
                i += 2
            elif actual[i+1] == 'x':
                count += 1
                i += 4
            else:
                assert(False)
    return len(line), count

def main2():
    data = readlines(FILENAME)
    data = [solve_2(dat) for dat in data]
    # print_2d(data)
    data_t = transpose(data)
    print(sum(data_t[0]) - sum(data_t[1]))

def solve_2(line):
    incr = list(line).count('\\') + list(line).count('\"')
    return len(line) + incr + 2, len(line)

if __name__ == '__main__':
    main()
    main2()
