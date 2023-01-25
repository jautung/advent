import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def fb_convert(l):
    return [1 if i == 'B' else 0 for i in l]

def lr_convert(l):
    return [1 if i == 'R' else 0 for i in l]

def bin_convert(l):
    return bin_to_int(''.join([str(i) for i in l]))

def main():
    data = readlines(FILENAME)
    data = [(bin_convert(fb_convert(list(dat[:7]))),bin_convert(lr_convert(list(dat[7:])))) for dat in data]
    ids = [d[0]*8+d[1] for d in data]
    print(max(ids))

def main2():
    data = readlines(FILENAME)
    data = [(bin_convert(fb_convert(list(dat[:7]))),bin_convert(lr_convert(list(dat[7:])))) for dat in data]
    have_passes = set(data)
    for row in range(128):
        for col in range(8):
            if (row,col) in have_passes:
                continue
            if row == 0 or row == 127:
                continue
            if col > 0 and (row,col-1) not in have_passes:
                continue
            if col < 7 and (row,col+1) not in have_passes:
                continue
            this_id = row*8+col
            print(this_id)

if __name__ == '__main__':
    main()
    main2()
