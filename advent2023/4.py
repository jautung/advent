import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    tot = 0
    for dat in data:
        winning, you = proc(dat)
        # print(set(winning).intersection(set(you)))
        winners = set(winning).intersection(set(you))
        num = len(winners)
        if num > 0:
            s = 2 ** (num-1)
        else:
            s = 0
        # print(s)
        tot += s
    print(tot)
    
    # print(data)

def proc(dat):
    a = dat.split(':')
    b = a[1].split('|')
    winning = [int(x.strip()) for x in b[0].split()]
    you = [int(x.strip()) for x in b[1].split()]
    return winning, you

def main2():
    data = readlines(FILENAME)
    index = 1
    mapper = dict()
    for dat in data:
        winning, you = proc(dat)
        # print(set(winning).intersection(set(you)))
        winners = set(winning).intersection(set(you))
        num = len(winners)
        # if num > 0:
        #     s = 2 ** (num-1)
        # else:
        #     s = 0
        # print(s)
        mapper[index] = num
        # tot += s
        index += 1
    # print(mapper)
    num_of_each = dict()
    for i in range(len(data)):
        num_of_each[i+1] = 1
    # print(mapper)
    # print(num_of_each)
    for i in range(len(data)):
        card = i+1
        to_add_more_cards = mapper[card]
        num_current_card = num_of_each[card]
        for k in range(to_add_more_cards):
            num_of_each[card+k+1] += num_current_card
    # print(num_of_each)
    tot = 0
    for a in num_of_each:
        tot += num_of_each[a]
    print(tot)
    

if __name__ == '__main__':
    main()
    main2()
