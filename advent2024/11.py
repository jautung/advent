import sys 
sys.path.append('..')

import math
import copy
from collections import defaultdict
from helper import *

FILENAME = '11_dat.txt'
mapper = {}

def g_num_digits(n):
    return int(math.log10(abs(n))) + 1

def main():
    data = readlines_split_each_line(FILENAME)
    # print(data[0])
    data = [int(dat) for dat in data[0]]
    # print(data)
    stones = data

    cache = {}
    def each_evolve(stone):
        if stone in cache:
            return cache[stone]
        if stone == 0:
            cache[stone] = [1]
            return cache[stone]
        # strify = str(stone)
        num_digits = g_num_digits(stone)
        # print(num_digits)
        if num_digits % 2 == 0:
            first = stone // (10**(num_digits//2))
            second = stone - first * (10**(num_digits//2))
            cache[stone] = [first, second]
            return cache[stone]
            # return [int(strify[:num_digits//2]), int(strify[num_digits//2:])]
        cache[stone] = [stone * 2024]
        return cache[stone]

    def evolve(stones):
        ret = []
        for stone in stones:
            # print(stone)
            # print(each_evolve(stone))
            ret += each_evolve(stone)
        return ret

        # return flatten([])
    i = 0
    # for i in range (10):
    while True:
        stones = evolve(stones)
        # print(i+1, len(stones))
        if i+1 == 25:
            break
        i += 1
    print(len(stones))
    # print(stones)
    # print(evolve(stones))

def main2():
    data = readlines_split_each_line(FILENAME)
    # print(data[0])
    data = [int(dat) for dat in data[0]]
    # print(data)
    stones = data

    cache = {}
    def num_resultant_stones(initial, num_turns):
        # print(initial, num_turns)
        if num_turns == 0:
            cache[(initial, num_turns)] = 1
            return cache[(initial, num_turns)]
        if (initial, num_turns) in cache:
            return cache[(initial, num_turns)]
        if initial == 0:
            cache[(initial, num_turns)] = num_resultant_stones(1, num_turns-1)
            return cache[(initial, num_turns)]
        num_digits = g_num_digits(initial)
        if num_digits % 2 == 0:
            first = initial // (10**(num_digits//2))
            second = initial - first * (10**(num_digits//2))
            cache[(initial, num_turns)] = num_resultant_stones(first, num_turns-1) + num_resultant_stones(second, num_turns-1)
            return cache[(initial, num_turns)]
            # cache[initial] = [first, second]
            # return cache[initial]
            # return [int(strify[:num_digits//2]), int(strify[num_digits//2:])]
        # print('s', stone*2024)
        cache[(initial, num_turns)] = num_resultant_stones(initial*2024, num_turns-1)
        return cache[(initial, num_turns)]
    c = 0
    for stone in stones:
        c += num_resultant_stones(stone, 75)
    print(c)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    main()
    main2()
