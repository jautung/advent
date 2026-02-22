import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '1_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    tot = 50
    count = 0
    for i in data:
        if i[0] == "L":
            tot -= int(i[1:])
        elif i[0] == "R":
            tot += int(i[1:])
        else:
            assert False
        # print(i, tot % 100)
        if tot % 100 == 0:
            count += 1
    # tot = tot % 100
    # print(tot)
    print(count)

def main2():
    data = readlines(FILENAME)
    tot = 50
    count = 0
    for i in data:
        start_was_zero = tot == 0
        if i[0] == "L":
            tot -= int(i[1:])
        elif i[0] == "R":
            tot += int(i[1:])
        else:
            assert False
        end_was_zero = tot % 100 == 0
        # count including ending, not for starting
        if tot > 0:
            incre = tot // 100
        elif tot < 0:
            if start_was_zero:
                incre = (-tot) // 100
            else:
                incre = (-tot) // 100 + 1
        else:
            if start_was_zero:
                incre = 0
            else:
                # from non-zero positive to end at 0
                incre = 1
        tot = tot % 100
        # print(i, tot, incre)
        count += incre
    print(count)

if __name__ == '__main__':
    main()
    main2()
