import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '10_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)

    CYCLES_TO_COMPLETE = 2

    reg = 1
    pending = []
    time = 1

    # for dat in data + ['noop'] * 10:
    #     if dat[0] == 'noop':
    #         continue
    #     elif dat[0] == 'addx':
    #         arg = int(dat[1])
    #         pending.append((arg, CYCLES_TO_COMPLETE))
    #     pending = [(pend[0], pend[1]-1) for pend in pending]
    #     for i in pending:
    #         if i[1] == 0:
    #             reg += i[0]
    #     pending = list(filter(lambda x: x[1] != 0, pending))
    #     print('after', time, 'is', reg, pending)
    #     time += 1

    strengths = 0
    for dat in data:
        if dat[0] == 'noop':
            strengths += do_thing(time, reg)
            time += 1
        elif dat[0] == 'addx':
            arg = int(dat[1])
            for i in range(CYCLES_TO_COMPLETE):
                strengths += do_thing(time, reg)
                time += 1
            reg += arg
    strengths += do_thing(time, reg)
    print(strengths)

def do_thing(time, reg):
    # print('during', time, 'is', reg)
    strength = time * reg
    # print(strength)
    # if time % 40 == 20:
    #     print(time, strength)
    return strength if time % 40 == 20 else 0

def main2():
    data = readlines_split_each_line(FILENAME)

    CYCLES_TO_COMPLETE = 2

    reg = 1
    pending = []
    time = 1

    # for dat in data + ['noop'] * 10:
    #     if dat[0] == 'noop':
    #         continue
    #     elif dat[0] == 'addx':
    #         arg = int(dat[1])
    #         pending.append((arg, CYCLES_TO_COMPLETE))
    #     pending = [(pend[0], pend[1]-1) for pend in pending]
    #     for i in pending:
    #         if i[1] == 0:
    #             reg += i[0]
    #     pending = list(filter(lambda x: x[1] != 0, pending))
    #     print('after', time, 'is', reg, pending)
    #     time += 1

    crt = [[None for j in range(40)] for i in range(6)]
    # print_2d(crt)

    # strengths = 0
    for dat in data:
        if dat[0] == 'noop':
            do_thing_2(time, reg, crt)
            time += 1
        elif dat[0] == 'addx':
            arg = int(dat[1])
            for i in range(CYCLES_TO_COMPLETE):
                do_thing_2(time, reg, crt)
                time += 1
            reg += arg
    do_thing_2(time, reg, crt)
    # print(strengths)

def do_thing_2(time, reg, crt):
    col = (time - 1) % 40
    row = (time - 1) // 40
    is_lit = abs(reg - col) <= 1
    # print('during', time, 'is', reg, row, col, is_lit)
    if time == 241:
        new = [''.join(['#' if c else ' ' for c in x]) for x in crt]
        print_2d(new)
        exit(1)
    crt[row][col] = is_lit
    # strength = time * reg
    # print(strength)
    # if time % 40 == 20:
    #     print(time, strength)
    # return strength if time % 40 == 20 else 0

if __name__ == '__main__':
    main()
    main2()
