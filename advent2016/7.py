import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

def parse(dat):
    assert(dat[0] != '[')
    a = dat.split('[')
    init_outside = a[0]
    rest= a[1:]
    inside = []
    outside = [init_outside]
    for i in rest:
        b = i.split(']')
        assert(len(b) == 2)
        inside.append(b[0])
        outside.append(b[1])
    return inside, outside

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    count = 0
    for i, o in data:
        # print(i, o, satisfies(i, o))
        if satisfies(i, o):
            count += 1

    # print_2d(data)
    print(count)

def satisfies(i,o):
    return sum([contains_abba(x) for x in i]) == 0 and sum([contains_abba(x) for x in o]) > 0

def contains_abba(s):
    return sum([is_abba(s[i:i+4]) for i in range(len(s))]) > 0

def is_abba(s):
    return len(s) == 4 and s[0] != s[1] and s[0] == s[3] and s[1] == s[2]

def main2():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    count = 0
    for i, o in data:
        # print(i, o, satisfies(i, o))
        if satisfies_ssl(i, o):
            count += 1

    # print_2d(data)
    print(count)

def satisfies_ssl(i,o):
    abas = []
    for x in i:
        abas += find_aba(x)
    for aba in abas:
        if sum([contains_bab(x, aba) for x in o]) > 0:
            return True
    return False

def find_aba(s):
    return list(filter(lambda x: x != None, [s[i:i+3] if is_aba(s[i:i+3]) else None for i in range(len(s))]))

def contains_bab(x, aba):
    target = aba[1] + aba[0] + aba[1]
    return target in x

def is_aba(s):
    return len(s) == 3 and s[0] != s[1] and s[0] == s[2]

if __name__ == '__main__':
    main()
    main2()
