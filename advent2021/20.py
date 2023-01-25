import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '20_dat.txt'
PADDING = 1
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    alg = data[0][0]
    img = [list(dat) for dat in data[1:][0]]
    # data = [int(dat) for dat in data]
    assert(len(alg) == 512)
    # print(alg)
    # print_2d(img)
    once, outside = iter_image(img, alg, 0) # outside of initial image is 0
    # print_2d(once)
    twice, outside = iter_image(once, alg, outside)
    # print_2d(twice)

    print('final', count_img(twice))

def iter_image(img, alg, outside):
    new_img = [[None for j in range(len(img[0])+2*PADDING)] for i in range(len(img)+2*PADDING)]

    def get_old(i, j):
        old_i = i-PADDING
        old_j = j-PADDING
        if old_i < 0 or old_j < 0 or old_i >= len(img) or old_j >= len(img[0]):
            return outside
        else:
            return 0 if img[old_i][old_j] == '.' else 1

    for i in range(len(new_img)):
        for j in range(len(new_img[0])):
            neighbors = [
                get_old(i-1,j-1),
                get_old(i-1,j),
                get_old(i-1,j+1),
                get_old(i,j-1),
                get_old(i,j),
                get_old(i,j+1),
                get_old(i+1,j-1),
                get_old(i+1,j),
                get_old(i+1,j+1),
            ]
            code = bin_to_int(''.join([str(neighbor) for neighbor in neighbors]))
            # print(i, j, code)
            new_img[i][j] = alg[code]

    return new_img, 0 if (alg[0] if outside == 0 else alg[-1]) == '.' else 1

def count_img(img):
    return sum([c == '#' for c in flatten(img)])

# Time: 21:46

def main2():
    data = readlines_split_by_newlines(FILENAME)
    alg = data[0][0]
    img = [list(dat) for dat in data[1:][0]]
    # data = [int(dat) for dat in data]
    assert(len(alg) == 512)
    # print(alg)
    # print_2d(img)
    outside = 0
    for i in range(50):
        img, outside = iter_image(img, alg, outside)
    # print_2d(img)

    print('final', count_img(img))

# Time: 23:53

if __name__ == '__main__':
    main()
    main2()
