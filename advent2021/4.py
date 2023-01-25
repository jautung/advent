import sys 
sys.path.append('..')

import copy
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    order = data[0][0]
    order = [int(i) for i in order.split(',')]
    data = data[1:]
    data = [[[int(i) for i in dat.split()] for dat in data1] for data1 in data]
    for new in order:
        data = [update_dat(dat, new) for dat in data]
        wins = [is_winning(dat) for dat in data]
        try:
            winning = wins.index(True)
            break
        except:
            continue
    unmarked = flatten(data[winning])
    unmarked = list(filter(lambda x: x != -1, unmarked))
    print(sum(unmarked) * new)

def update_dat(dat, new):
    return [[i if i != new else -1 for i in j] for j in dat]

def is_winning(dat):
    for j in dat:
        if is_winning_row(j):
            return True
    for j in transpose(dat):
        if is_winning_row(j):
            return True
    return False

def is_winning_row(row):
    return len(list(filter(lambda x: x == -1, row))) == len(row)

def main2():
    data = readlines_split_by_newlines(FILENAME)
    order = data[0][0]
    order = [int(i) for i in order.split(',')]
    data = data[1:]
    data = [[[int(i) for i in dat.split()] for dat in data1] for data1 in data]
    losing = None
    for new in order:
        data = [update_dat(dat, new) for dat in data]
        wins = [is_winning(dat) for dat in data]
        if sum(wins) == len(wins) - 1:
            losing = wins.index(False)
        if losing and wins[losing]:
            break
    unmarked = flatten(data[losing])
    unmarked = list(filter(lambda x: x != -1, unmarked))
    print(sum(unmarked) * new)

if __name__ == '__main__':
    main()
    main2()
