import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '3_dat.txt'
mapper = {}

def find_max(seq, spaces_to_leave):
    tens = None
    tens_index = None
    for i in range(len(seq)-spaces_to_leave):
        cand = seq[i]
        if tens == None or tens < cand:
            tens = cand
            tens_index = i
    return tens, tens_index

def max_joltage(seq):
    tens, tens_index = find_max(seq, 1)
    remain = seq[tens_index+1:]
    ones, _ = find_max(remain, 0)
    return 10 * tens + ones

def main():
    data = readlines(FILENAME)
    data = [[int(x) for x in dat] for dat in data]
    # print_2d(data)
    tot = 0
    for i in data:
        # print(i, max_joltage(i))
        tot += max_joltage(i)
    print(tot)

def max_joltage_2(seq):
    incum = 0
    remain = seq
    for remains in range(11, -1, -1):
        dig, dig_index = find_max(remain, remains)
        remain = remain[dig_index+1:]
        incum += dig
        incum *= 10
    return incum // 10

def main2():
    data = readlines(FILENAME)
    data = [[int(x) for x in dat] for dat in data]
    # print_2d(data)
    tot = 0
    for i in data:
        # print(i, max_joltage_2(i))
        tot += max_joltage_2(i)
    print(tot)

if __name__ == '__main__':
    main()
    main2()
