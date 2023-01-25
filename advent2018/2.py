import sys 
sys.path.append('..')

import copy
from collections import Counter
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [Counter(list(dat)).most_common() for dat in data]
    data = [(sum([c[1] == 2 for c in dat])>0,sum([c[1] == 3 for c in dat])>0) for dat in data]
    # print_2d(data)
    # print(transpose(data))
    print(sum(transpose(data)[0]) * sum(transpose(data)[1]))

def main2():
    data = readlines(FILENAME)
    for a in data:
        for b in data:
            if differ_by(a,b) == 1:
                # print(a,b)
                print(same_part(a,b))
                return

def differ_by(a,b):
    assert(len(a) == len(b))
    N = len(a)
    return sum([a[i] != b[i] for i in range(N)])

def same_part(a,b):
    assert(len(a) == len(b))
    N = len(a)
    return ''.join(list(filter(lambda x: x, [a[i] if a[i] == b[i] else None for i in range(N)])))

if __name__ == '__main__':
    main()
    main2()
