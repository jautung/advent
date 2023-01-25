import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '3_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = list(data[0])
    pos = (0,0)
    set_of_houses = set([pos])
    for dat in data:
        if dat == '>':
            pos = (pos[0]+1, pos[1])
        elif dat == '<':
            pos = (pos[0]-1, pos[1])
        elif dat == '^':
            pos = (pos[0], pos[1]-1)
        elif dat == 'v':
            pos = (pos[0], pos[1]+1)
        set_of_houses.add(pos)
    print(len(set_of_houses))

def main2():
    data = readlines(FILENAME)
    data = list(data[0])
    pos = (0,0)
    pos_alt = (0,0)
    set_of_houses = set([pos])
    robo_move = False
    for dat in data:
        if not robo_move:
            if dat == '>':
                pos = (pos[0]+1, pos[1])
            elif dat == '<':
                pos = (pos[0]-1, pos[1])
            elif dat == '^':
                pos = (pos[0], pos[1]-1)
            elif dat == 'v':
                pos = (pos[0], pos[1]+1)
            set_of_houses.add(pos)
        else:
            if dat == '>':
                pos_alt = (pos_alt[0]+1, pos_alt[1])
            elif dat == '<':
                pos_alt = (pos_alt[0]-1, pos_alt[1])
            elif dat == '^':
                pos_alt = (pos_alt[0], pos_alt[1]-1)
            elif dat == 'v':
                pos_alt = (pos_alt[0], pos_alt[1]+1)
            set_of_houses.add(pos_alt)
        robo_move = not robo_move
    print(len(set_of_houses))

if __name__ == '__main__':
    main()
    main2()
