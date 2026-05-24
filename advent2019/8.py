import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
mapper = {}

WIDTH = 25
HEIGHT = 6
SIZE = WIDTH * HEIGHT

def main():
    data = readlines(FILENAME)
    assert len(data) == 1
    rawPixels = data[0]
    layers = [rawPixels[i * SIZE : (i+1) * SIZE] for i in range(len(rawPixels) // SIZE)]
    # print([len(l) for l in layers])

    counters = [(l.count("0"), l.count("1") * l.count("2")) for l in layers]
    counters.sort()
    print(counters[0][1])

def main2():
    data = readlines(FILENAME)
    assert len(data) == 1
    rawPixels = data[0]
    layers = [rawPixels[i * SIZE : (i+1) * SIZE] for i in range(len(rawPixels) // SIZE)]

    rendered = ['2' for _ in range(SIZE)]
    for l in layers:
        for idx in range(SIZE):
            if rendered[idx] != '2':
                continue
            rendered[idx] = l[idx]

    renderedLayer = [rendered[i * WIDTH : (i+1) * WIDTH] for i in range(len(rendered) // WIDTH)]
    # print_2d(renderedLayer)
    for r in renderedLayer:
        print(''.join(['x' if k == '1' else ' ' for k in r]))

if __name__ == '__main__':
    main()
    main2()
