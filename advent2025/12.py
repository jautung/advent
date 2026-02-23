import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '12_dat.txt'
mapper = {}

def parse_shape(index, shape):
    assert shape[0] == f"{index}:"
    return [[c for c in x] for x in shape[1:]]

def parse_problem(line):
    a = line.split(':')
    size = [int(x) for x in a[0].strip().split('x')]
    numbers = [int(x.strip()) for x in a[1].strip().split(' ')]
    return ((size[0], size[1]), numbers)

def get_size(shape):
    counter = 0
    for r in shape:
        for c in r:
            if c == "#":
                counter += 1
    return counter

def evaluate(problem, shapes, shape_sizes):
    # print('eval', problem)
    grid_size = problem[0][0] * problem[0][1]
    total_size = 0
    for index, s in enumerate(problem[1]):
        total_size += s * shape_sizes[index]
    # print(total_size, grid_size)
    if total_size > grid_size:
        # might as well bail quickly
        return False
    # at least for all examples and given info
    # the shapes are all within a 3x3
    dumb_num_3x3s = (problem[0][0] // 3) * (problem[0][1] // 3)
    # print(dumb_num_3x3s, sum(problem[1]))
    if sum(problem[1]) <= dumb_num_3x3s:
        # just put one in each 3x3 lol
        return True
    # think about better things later
    # hmm this is apparently enough for the problem
    # I'm very surprised we don't need to do anything more than this
    # but not going to complain i guess...
    # why is the bound so loose....
    assert False

def main():
    data = readlines_split_by_newlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print_2d(data)
    shapes = [parse_shape(i, shape) for (i, shape) in enumerate(data[:-1])]
    problems = [parse_problem(p) for p in data[-1]]

    # for s in shapes:
    #     print_2d(s)
    # print_2d(problems)

    shape_sizes = [get_size(shape) for shape in shapes]
    # print(shape_sizes)

    final_out = [evaluate(problem, shapes, shape_sizes) for problem in problems]
    # print("final", final_out)
    print(sum([1 if f else 0 for f in final_out]))

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
