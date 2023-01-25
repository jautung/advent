import sys 
sys.path.append('..')

import copy
import functools
from collections import defaultdict
from helper import *

FILENAME = '13_dat.txt'
mapper = {}

class Node:
    def __init__(self, children=[]):
        self.children = children

def parse(line):
    # print(line)
    if line[0] == '[' and line[1] == ']':
        # print('y')
        return Node(children=[]), 1
    elif line[0] == '[':
        # print('x')
        children = []
        starting_index = 1
        while True:
            assert(starting_index < len(line))
            child, end_of_child = parse(line[starting_index:])
            if line[starting_index+end_of_child+1] == ']':
                children.append(child)
                # starting_index += end_of_child+2
                # print('completed')
                return Node(children=children), starting_index+end_of_child+1
                # break
            # print('s', line, end_of_child, line[end_of_child+1])
            assert(line[starting_index+end_of_child+1] == ',')
            children.append(child)
            starting_index += end_of_child+2
    else:
        until = 0
        while True:
            if until == len(line) or line[until] == ',' or line[until] == ']':
                break
            until += 1
        # until = line.index(',')
        # print(until)
        return int(line[:until]), until-1

def print_node(n, top_level=True):
    if isinstance(n, int):
        print(n, end='')
        # return
    else:
        assert(isinstance(n, Node))
        print('[', end='')
        for i, c in enumerate(n.children):
            print_node(c, top_level=False)
            if i != len(n.children) - 1:
                print(',', end='')
        print(']', end='')
    if top_level:
        print('\n', end='')

def main():
    data = readlines_split_by_newlines(FILENAME)

    pairs = []
    for dat in data:
        a, _ = parse(dat[0])
        b, _ = parse(dat[1])
        pairs.append((a,b))
        # print(dat[0])
        # print(dat[1])
        # print()
    # print(data)
    # n, _ = parse('[1,[2,[3,[4,[5,6,7]]]],8,9]')
    # print_node(n)
    res = 0
    for i, pair in enumerate(pairs):
        if in_right_order(pair[0], pair[1]):
            res += i+1
        # print(i+1, in_right_order(pair[0], pair[1]))
    print(res)

def in_right_order(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return True
        elif l > r:
            return False
        return None
    elif isinstance(l, Node) and isinstance(r, Node):
        to_check = min(len(l.children), len(r.children))
        for i in range(to_check):
            comp = in_right_order(l.children[i], r.children[i])
            if comp != None:
                return comp
        if len(l.children) < len(r.children):
            return True
        elif len(l.children) > len(r.children):
            return False
        else:
            return None
    elif isinstance(l, int) and isinstance(r, Node):
        return in_right_order(Node(children=[l]), r)
    elif isinstance(l, Node) and isinstance(r, int):
        return in_right_order(l, Node(children=[r]))

def cmp_func(l, r):
    o = in_right_order(l, r)
    if o == True:
        return 1
    elif o == False:
        return -1
    else:
        assert(o == None)
        return 0

def reverse_numeric(x, y):
    return y - x

def main2():
    data = readlines(FILENAME)
    data = list(filter(lambda x: x != '', data))
    data = [parse(dat)[0] for dat in data]
    dividers = [
        parse('[[2]]')[0],
        parse('[[6]]')[0],
    ]
    data = data + dividers

    sorted_data = sorted(data, key=functools.cmp_to_key(cmp_func), reverse=True)
    for i, n in enumerate(sorted_data):
        # print_node(i)
        if n == dividers[0]:
            # print(i+1)
            a = i+1
        elif n == dividers[1]:
            # print(i+1)
            b = i+1
    print(a*b)
    # print(sorted([5, 2, 4, 1, 3], key=functools.cmp_to_key(reverse_numeric)))
    # print_2d(sorted_data)
    # print(len(data))
    # print(data[0])

    # pairs = []
    # for dat in data:
    #     a, _ = parse(dat[0])
    #     b, _ = parse(dat[1])
    #     pairs.append((a,b))
    #     # print(dat[0])
    #     # print(dat[1])
    #     # print()
    # # print(data)
    # # n, _ = parse('[1,[2,[3,[4,[5,6,7]]]],8,9]')
    # # print_node(n)
    # res = 0
    # for i, pair in enumerate(pairs):
    #     if in_right_order(pair[0], pair[1]):
    #         res += i+1
    #     # print(i+1, in_right_order(pair[0], pair[1]))
    # print(res)

if __name__ == '__main__':
    main()
    main2()
