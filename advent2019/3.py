import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '3_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [dat.split(',') for dat in data]
    wire1 = data[0]
    wire2 = data[1]
    # print(data)
    set1 = get_set(wire1)
    set2 = get_set(wire2)
    inters = set1.intersection(set2) - set([(0,0)])
    distances = [manhattan(inter) for inter in inters]
    print(sorted(distances)[0])

def get_set(wire):
    res = set()

    start = (0,0)
    res.add(start)

    for instr in wire:
        if instr[0] == 'U':
            for _ in range(int(instr[1:])):
                start = add_tup(start, (0,1))
                res.add(start)
        elif instr[0] == 'D':
            for _ in range(int(instr[1:])):
                start = add_tup(start, (0,-1))
                res.add(start)
        elif instr[0] == 'L':
            for _ in range(int(instr[1:])):
                start = add_tup(start, (-1,0))
                res.add(start)
        elif instr[0] == 'R':
            for _ in range(int(instr[1:])):
                start = add_tup(start, (1,0))
                res.add(start)

    return res

def main2():
    data = readlines(FILENAME)
    data = [dat.split(',') for dat in data]
    wire1 = data[0]
    wire2 = data[1]
    # print(data)
    res1 = get_set_with_time(wire1)
    res2 = get_set_with_time(wire2)
    set1 = set(res1.keys())
    set2 = set(res2.keys())
    inters = set1.intersection(set2) - set([(0,0)])
    # print(inters)
    # print(res1[(6,5)])
    # print(res2[(6,5)])
    times = [res1[inter]+res2[inter] for inter in inters]
    print(sorted(times)[0])

def get_set_with_time(wire):
    res = dict()

    start = (0,0)
    res[start] = 0

    step_count = 1
    for instr in wire:
        if instr[0] == 'U':
            for _ in range(int(instr[1:])):
                start = add_tup(start, (0,1))
                if start not in res:
                    res[start] = step_count
                step_count += 1
        elif instr[0] == 'D':
            for _ in range(int(instr[1:])):
                start = add_tup(start, (0,-1))
                if start not in res:
                    res[start] = step_count
                step_count += 1
        elif instr[0] == 'L':
            for _ in range(int(instr[1:])):
                start = add_tup(start, (-1,0))
                if start not in res:
                    res[start] = step_count
                step_count += 1
        elif instr[0] == 'R':
            for _ in range(int(instr[1:])):
                start = add_tup(start, (1,0))
                if start not in res:
                    res[start] = step_count
                step_count += 1

    return res

if __name__ == '__main__':
    main()
    main2()
