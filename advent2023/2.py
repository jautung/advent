import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [proc(dat) for dat in data]
    game_i = 1
    ret = 0
    for game in data:
        map = {
            'blue': 0,
            'red': 0,
            'green': 0,
        }
        for round in game:
            for pair in round:
                map[pair[1]] = max(map[pair[1]], int(pair[0])) 
                # print(int(pair[0]), pair[1])
        if map['red'] <= 12 and map['green'] <= 13 and map['blue'] <= 14:
            ret += game_i
        # print(map, game_i)
        game_i += 1
    print(ret)

def proc(dat):
    x = dat.split()
    s = ' '.join(x[2:]).split(';')
    c = [[[z.strip() for z in k.split()] for k in c.split(',')] for c in s]
    return c
    # aa = []
    # for i in range((len(x)-2)//2):
    #     print(x[2+2*i], x[2+2*i+1])
    # for a in x[2:]
    # print(x[2:])

def main2():
    data = readlines(FILENAME)
    data = [proc(dat) for dat in data]
    game_i = 1
    ret = 0
    for game in data:
        map = {
            'blue': 0,
            'red': 0,
            'green': 0,
        }
        for round in game:
            for pair in round:
                map[pair[1]] = max(map[pair[1]], int(pair[0])) 
                # print(int(pair[0]), pair[1])
        # if map['red'] <= 12 and map['green'] <= 13 and map['blue'] <= 14:
        #     ret += game_i
        power = map['red'] * map['green'] * map['blue']
        # print(power, game_i)
        ret += power
        game_i += 1
    print(ret)

if __name__ == '__main__':
    main()
    main2()
