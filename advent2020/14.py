import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '14_dat.txt'
mapper = {}

def parse_mask(raw):
    assert(len(raw) == 36)
    res = {}
    for i in range(36):
        if raw[i] == 'X':
            continue
        elif raw[i] == '0':
            res[35-i] = 0
        elif raw[i] == '1':
            res[35-i] = 1
    return res
    
def mask_func(parsed):
    def ret(num):
        for pos, val in parsed.items():
            if val == 0:
                num = num & (~(1 << pos))
            elif val == 1:
                num = num | (1 << pos)
        return num
    return ret

def parse_assignment(row):
    parts = row.split(' = ')
    assert(len(parts) == 2)
    rhs = int(parts[1].strip())
    subparts = parts[0].split('[')
    assert(len(subparts) == 2)
    subsubparts = subparts[1]
    assert(subsubparts[-1] == ']')
    lhs = int(subsubparts[:-1])
    return lhs, rhs

def main():
    data = readlines(FILENAME)

    curr_mask = None
    mem = {}
    for row in data:
        if row.startswith("mask = "):
            mask = row[len("mask = "):]
            assert(len(mask) == 36)
            curr_mask = mask_func(parse_mask(mask))
            # print(curr_mask)
        else:
            assert(row.startswith("mem["))
            lhs, rhs = parse_assignment(row)
            # print(curr_mask)
            # print(lhs, rhs)
            # print(curr_mask(rhs))
            mem[lhs] = curr_mask(rhs)
    # print(mem)

    tot = 0
    for _, val in mem.items():
        tot += val
    print(tot)

def parse_mask_2(raw):
    assert(len(raw) == 36)
    res = {}
    for i in range(36):
        if raw[i] == 'X':
            res[35-i] = 'X'
        elif raw[i] == '0':
            continue
        elif raw[i] == '1':
            res[35-i] = 1
    return res
    
def mask_func_2(parsed):
    def ret(num):
        for pos, val in parsed.items():
            if val == 1:
                num = num | (1 << pos)

        res = [num]
        for pos, val in parsed.items():
            if val != 'X':
                continue
            new_res = []
            for item in res:
                num1 = item & (~(1 << pos))
                num2 = item | (1 << pos)
                new_res += [num1, num2]
            # print(res, pos, new_res)
            res = new_res
        return res

    return ret

def main2():
    data = readlines(FILENAME)

    curr_mask = None
    mem = {}
    for row in data:
        if row.startswith("mask = "):
            mask = row[len("mask = "):]
            assert(len(mask) == 36)
            curr_mask = mask_func_2(parse_mask_2(mask))
            # print(curr_mask)
        else:
            assert(row.startswith("mem["))
            lhs, rhs = parse_assignment(row)
            # print(lhs, rhs)
            # print(curr_mask(lhs))
            actual_lhss = curr_mask(lhs)
            for l in actual_lhss:
                mem[l] = rhs
    # print(mem)

    tot = 0
    for _, val in mem.items():
        tot += val
    print(tot)

if __name__ == '__main__':
    main()
    main2()
