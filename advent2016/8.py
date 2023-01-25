import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    # print_2d(data)

    parsed = []
    for dat in data:
        if dat.startswith('rect'):
            a = dat.split(' ')
            b = a[1].split('x')
            wide = int(b[0])
            tall = int(b[1])
            parsed.append(('L', wide, tall))
        else:
            a = dat.split(' ')
            assert(a[0] == 'rotate')
            if a[1] == 'row':
                coord = int(a[2].split('=')[1])
                dist = int(a[4])
                parsed.append(('R', coord, dist))
            elif a[1] == 'column':
                coord = int(a[2].split('=')[1])
                dist = int(a[4])
                parsed.append(('C', coord, dist))
            else:
                assert(False)
    # print_2d(parsed)

    WIDE = 50
    TALL = 6
    # WIDE = 7
    # TALL = 3
    screen = [[False for _ in range(WIDE)] for _ in range(TALL)]
    # print_screen(screen)

    for p in parsed:
        if p[0] == 'L':
            for i in range(p[1]):
                for j in range(p[2]):
                    screen[j][i] = True
        elif p[0] == 'R':
            old_row = screen[p[1]]
            new_row = [old_row[(i-p[2])%len(old_row)] for i in range(len(old_row))]
            screen[p[1]] = new_row
        elif p[0] == 'C':
            old_col = [screen[i][p[1]] for i in range(len(screen))]
            # print(old_col)
            new_col = [old_col[(i-p[2])%len(old_col)] for i in range(len(old_col))]
            # print(new_col)
            for i in range(len(screen)):
                screen[i][p[1]] = new_col[i]

    print_screen(screen)
    screen_lit_count(screen)

def print_screen(screen):
    for row in screen:
        for cell in row:
            if cell:
                print('#', end='')
            else:
                print('.', end='')
        print()

def screen_lit_count(screen):
    print(sum([sum(row) for row in screen]))

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
