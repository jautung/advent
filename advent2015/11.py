import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '11_dat.txt'
mapper = {}

def main():
    # s = 'hepxcrrq'
    s = incr('hepxxyzz')
    # s = 'ghijklmn'
    # s = 'xx'
    while True:
        # print(s)
        if satisfies(s):
            print('FOUND!', s)
            return
        # assert(s != 'abcdffaa')
        s = incr(s)
        # print(s)
        assert(len(s) == 8)
        # print(s)

    # test = 'abbcegjk'
    # print(satisfies_1(test))
    # print(satisfies_2(test))
    # print(satisfies_3(test))

def satisfies(s):
    return satisfies_2(s) and satisfies_1(s) and satisfies_3(s)

def satisfies_1(s):
    trips = [s[i:i+3] for i in range(len(s)-2)]
    for trip in trips:
        nums = [ord(c) for c in trip]
        # print(nums)
        if nums[1] == nums[0]+1 and nums[2] == nums[0]+2:
            return True
    return False

def satisfies_2(s):
    return 'i' not in s and 'o' not in s and 'l' not in s

def satisfies_3(s):
    pairs = [s[i:i+2] for i in range(len(s)-1)]
    goods = []
    [goods.append(i) if len(set(list(pair))) == 1 else None for i, pair in enumerate(pairs)]
    return len(goods) > 1 and max(goods) - min(goods) > 1

def incr(s):
    base_26_lst = [ord(c) - ord('a') for c in s]
    # print(base_26_lst)
    decimal = to_dec(base_26_lst, 26)
    # print('d', decimal)
    decimal += 1
    # print('d', decimal)
    new = to_base(decimal, 26)
    # print(new)
    return ''.join([chr(n + ord('a')) for n in new]).rjust(8, 'a')
    # list(s)
    # print(ord(s[0]))
    # print(ord(s[1]))

def to_dec(l, b):
    acc = 0
    while len(l) > 0:
        acc += l.pop(0)
        acc *= b
    return acc // b

def to_base(d, b):
    ls = []
    while d > 0:
        ls.append(d % b)
        d = d // b
    return list(reversed(ls))

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
