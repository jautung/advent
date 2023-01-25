import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '21_dat.txt'
mapper = {}

def parse(dat):
    name = dat[0][:-1]
    rest = dat[1:]
    if len(rest) == 1:
        val = int(rest[0])
    else:
        # print(rest)
        assert(len(rest) == 3)
        val = rest
    return name, val

def main():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    mapping = dict()
    for name, val in data:
        mapping[name] = val

    print(find_val('root', mapping))

def find_val(name, mapping):
    val = mapping[name]
    if isinstance(val, int):
        return val
    else:
        assert(len(val) == 3)
        if val[1] == '+':
            return find_val(val[0], mapping) + find_val(val[2], mapping)
        elif val[1] == '-':
            return find_val(val[0], mapping) - find_val(val[2], mapping)
        elif val[1] == '*':
            return find_val(val[0], mapping) * find_val(val[2], mapping)
        elif val[1] == '/':
            return int(find_val(val[0], mapping) / find_val(val[2], mapping))

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    mapping = dict()
    for name, val in data:
        mapping[name] = val

    # print(mapping['root'])
    left = mapping['root'][0]
    right = mapping['root'][2]

    # print(left, right)
    try:
        # print('l', find_val_2(left, mapping))
        correct = find_val_2(left, mapping)
    except:
        bad = 'L'
        pass

    try:
        # print('r', find_val_2(right, mapping))
        correct = find_val_2(right, mapping)
    except:
        bad = 'R'
        pass

    # print(correct)
    # print(bad)
    if bad == 'L':
        print(find_humn_for_target(correct, left, mapping))
    else:
        print(find_humn_for_target(correct, right, mapping))

def find_val_2(name, mapping):
    # assert(False)
    # print(name, mapping[name])
    if name == 'humn':
        assert(False)
        # return 301
    val = mapping[name]
    if isinstance(val, int):
        return val
    else:
        assert(len(val) == 3)
        if val[1] == '+':
            return find_val_2(val[0], mapping) + find_val_2(val[2], mapping)
        elif val[1] == '-':
            return find_val_2(val[0], mapping) - find_val_2(val[2], mapping)
        elif val[1] == '*':
            return find_val_2(val[0], mapping) * find_val_2(val[2], mapping)
        elif val[1] == '/':
            return int(find_val_2(val[0], mapping) / find_val_2(val[2], mapping))

def find_humn_for_target(target, name, mapping):
    if name == 'humn':
        return target

    val = mapping[name]

    if isinstance(val, int):
        assert(False)
        return None

    else:
        assert(len(val) == 3)

        try:
            left_val = find_val_2(val[0], mapping)
        except:
            left_val = None
            pass

        try:
            right_val = find_val_2(val[2], mapping)
        except:
            right_val = None
            pass

        assert(left_val != None or right_val != None)

        if val[1] == '+':
            if left_val != None:
                return find_humn_for_target(target - left_val, val[2], mapping)
            elif right_val != None:
                return find_humn_for_target(target - right_val, val[0], mapping)
        elif val[1] == '-':
            if left_val != None:
                return find_humn_for_target(left_val - target, val[2], mapping)
            elif right_val != None:
                return find_humn_for_target(target + right_val, val[0], mapping)
        elif val[1] == '*':
            if left_val != None:
                return find_humn_for_target(int(target / left_val), val[2], mapping)
            elif right_val != None:
                return find_humn_for_target(int(target / right_val), val[0], mapping)
        elif val[1] == '/':
            if left_val != None:
                return find_humn_for_target(int(left_val / target), val[2], mapping)
            elif right_val != None:
                return find_humn_for_target(target * right_val, val[0], mapping)

if __name__ == '__main__':
    main()
    main2()
