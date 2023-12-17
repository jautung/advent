import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '15_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    line = data[0]
    assgns = line.split(',')
    # print(assgns)
    s = 0
    for a in assgns:
        c = apply_alg(a)
        # print(a, c)
        s += c
    print(s)
    # data = [int(dat) for dat in data]
    # print(inp)

def apply_alg(line):
    v = 0
    for c in line:
        v += ord(c)
        v *= 17
        v = v % 256
    return v

def main2():
    data = readlines(FILENAME)
    line = data[0]
    seq = line.split(',')
    data = dict()
    for s in seq:
        if '=' in s:
            x = s.split('=')
            label = x[0]
            focal_length = int(x[1])
            label_hashed = apply_alg(label)
            # print('putting in', label, focal_length, 'into', label_hashed)
            if label_hashed in data:
                contents = data[label_hashed]
                content_labels = [c[0] for c in contents]
                if label in content_labels:
                    # replacement
                    i = content_labels.index(label)
                    contents[i] = (label, focal_length)
                else:
                    # not in there
                    contents.append((label, focal_length))
            else:
                data[label_hashed] = [(label, focal_length)]
        else:
            assert('-' in s)
            assert(s[-1] == '-')
            label = s[:-1]
            label_hashed = apply_alg(label)
            # print('trying to remove', label, 'from', label_hashed)
            if label_hashed in data:
                contents = data[label_hashed]
                content_labels = [c[0] for c in contents]
                if label in content_labels:
                    # poof
                    i = content_labels.index(label)
                    contents.pop(i)
        # print(data)
    s = 0
    for key in data:
        for idx, item in enumerate(data[key]):
            label, focal_length = item
            s += ((key+1) * (idx+1) * focal_length)
    print(s)
    

if __name__ == '__main__':
    main()
    main2()
