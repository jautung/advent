import sys 
sys.path.append('..')

import copy
from collections import Counter
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def parse(dat):
    a = dat.split('[')
    checksum = a[1][:-1]
    rest = a[0]
    boo = rest.split('-')
    sector = int(boo[-1])
    name = boo[:-1]
    return sector, name, checksum

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    count = 0
    for sector, name, checksum in data:
        if verify(name, checksum):
            count += sector

    # print_2d(data)
    print(count)

def verify(name, checksum):
    joined = ''.join(name)
    c = Counter(list(joined))
    # correct_cs = ''
    # for i in range(5):
        # print(c.most_common(5))
        # correct_cs += c.most_common(i)
    base = c.most_common(len(set(list(joined))))
    boo = [(b[1], -ord(b[0]), b[0]) for b in base]
    # print(sorted(boo, reverse=True))
    boo = sorted(boo, reverse=True)
    correct_cs = ''.join([a[2] for a in boo[:5]])
    # print(joined, correct_cs, checksum)
    return correct_cs == checksum

def main2():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    for sector, name, checksum in data:
        if verify(name, checksum):
            print(sector, decrypt(name, sector))

    # print_2d(data)
    # print(count)

def decrypt(name, sector):
    name = ' '.join(name)
    return ''.join([transform(c, sector) for c in name])

def transform(c, sector):
    if c == ' ':
        return c
    test = ord(c) + (sector%26)
    if test >= ord('a') and test <= ord('z'):
        return chr(test)
    test = ord(c) - (26-sector%26)
    if test >= ord('a') and test <= ord('z'):
        return chr(test)
    print(c, sector%26)
    assert(False)

if __name__ == '__main__':
    main()
    main2()
