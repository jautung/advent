import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

VOWELS = set(list('aeiou'))

def main():
    data = readlines(FILENAME)
    count = 0
    for dat in data:
        # print(dat, is_nice(dat))
        if is_nice(dat):
            count += 1
    print(count)

def is_nice(s):
    if sum([c in VOWELS for c in s]) < 3:
        return False
    if sum([len(set(list(s[i:i+2]))) == 1 for i in range(len(s)-1)]) < 1:
        return False
    if 'ab' in s:
        return False
    if 'cd' in s:
        return False
    if 'pq' in s:
        return False
    if 'xy' in s:
        return False
    return True

def main2():
    data = readlines(FILENAME)
    count = 0
    for dat in data:
        # print(dat, is_nice_2(dat))
        if is_nice_2(dat):
            count += 1
    print(count)

def is_nice_2(s):
    pairs = [s[i:i+2] for i in range(len(s)-1)]
    pairs_dict = defaultdict(lambda: [])
    [pairs_dict[pair].append(i) for i, pair in enumerate(pairs)]
    good_pair = False
    for pair, poses in pairs_dict.items():
        if max(poses) - min(poses) > 1:
            good_pair = True
            break
    if not good_pair:
        return False
    if sum([len(set([s[i],s[i+2]])) == 1 for i in range(len(s)-2)]) < 1:
        return False
    return True

if __name__ == '__main__':
    main()
    main2()
