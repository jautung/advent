import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

def strip_bag(name, with_count):
    x = name.split(' bag')[0]
    if x == 'no other':
        return None
    if not with_count:
        return x
    first_space = x.index(' ')
    return x[:first_space], x[first_space+1:]
    # return name

def parse_line(dat):
    x = dat.split(' contain ')
    assert(len(x) == 2)
    first = strip_bag(x[0], False)
    # print(x[0])
    # print(x[1].split(', '))
    rest = [strip_bag(t, True) for t in x[1].split(', ')]
    if x[1] == 'no other bags.':
        rest = None
    if rest:
        assert(first not in [r[1] for r in rest])
    return first, rest

def gen_is_contain(container, target):
    if container == target:
        return True
    if mapper[container] == None:
        return False
    for a in mapper[container]:
        if gen_is_contain(a[1], target):
            return True
    return False

TARGET = 'shiny gold'

def main():
    data = readlines(FILENAME)
    data = [parse_line(dat) for dat in data]
    # print(data)
    # for d in data:
    #     print(d)
    # print([d[0] for d in data])
    assert(len([d[0] for d in data]) == len(set([d[0] for d in data])))
    for d in data:
        mapper[d[0]] = d[1]
    # print(mapper)
    count = 0
    for i in mapper:
        if i == TARGET:
            continue
        x = gen_is_contain(i, TARGET)
        # print(i, x)
        if x:
            count += 1
    print(count)

def counter(start):
    if mapper[start] == None:
        return 1
    total = 1
    for a in mapper[start]:
        total += int(a[0]) * counter(a[1])
    return total

def main2():
    data = readlines(FILENAME)
    data = [parse_line(dat) for dat in data]
    # print(data)
    # for d in data:
    #     print(d)
    # print([d[0] for d in data])
    assert(len([d[0] for d in data]) == len(set([d[0] for d in data])))
    for d in data:
        mapper[d[0]] = d[1]
    # print(mapper)
    print(counter(TARGET) - 1)

if __name__ == '__main__':
    main()
    main2()
