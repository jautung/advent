import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    
    def fix_rep(val):
        if val >= 0:
            return val
        else:
            return val % 65536

    parsed = dict()
    for dat in data:
        dat = dat.split(' -> ')
        ins = dat[0].split()
        out = dat[1].split()[0]
        parsed[out] = ins

    outs = [out for out in parsed]
    assert(len(set(outs)) == len(outs))

    cached = dict()

    def get_val(val):
        if val in cached:
            return cached[val]
        elif val in parsed:
            return get_final(val)
        else:
            return int(val)

    def get_final(wire):
        ins = parsed[wire]
        if len(ins) == 1:
            res = fix_rep(get_val(ins[0]))
        elif len(ins) == 3 and ins[1] == 'AND':
            res = fix_rep(get_val(ins[0]) & get_val(ins[2]))
        elif len(ins) == 3 and ins[1] == 'OR':
            res = fix_rep(get_val(ins[0]) | get_val(ins[2]))
        elif len(ins) == 3 and ins[1] == 'LSHIFT':
            res = fix_rep(get_val(ins[0]) << get_val(ins[2]))
        elif len(ins) == 3 and ins[1] == 'RSHIFT':
            res = fix_rep(get_val(ins[0]) >> get_val(ins[2]))
        elif len(ins) == 2 and ins[0] == 'NOT':
            res = fix_rep(~get_val(ins[1]))
        cached[wire] = res
        return res

    # for c in list('defghixy'):
    #     print(get_final(c))

    print(get_final('a'))
    # RES = 16076

def main2():
    data = readlines(FILENAME)
    
    def fix_rep(val):
        if val >= 0:
            return val
        else:
            return val % 65536

    parsed = dict()
    for dat in data:
        dat = dat.split(' -> ')
        ins = dat[0].split()
        out = dat[1].split()[0]
        parsed[out] = ins

    outs = [out for out in parsed]
    assert(len(set(outs)) == len(outs))

    cached = dict()

    B_OVERRIDE = 16076

    def get_val(val):
        if val == 'b':
            return B_OVERRIDE
        elif val in cached:
            return cached[val]
        elif val in parsed:
            return get_final(val)
        else:
            return int(val)

    def get_final(wire):
        ins = parsed[wire]
        if len(ins) == 1:
            res = fix_rep(get_val(ins[0]))
        elif len(ins) == 3 and ins[1] == 'AND':
            res = fix_rep(get_val(ins[0]) & get_val(ins[2]))
        elif len(ins) == 3 and ins[1] == 'OR':
            res = fix_rep(get_val(ins[0]) | get_val(ins[2]))
        elif len(ins) == 3 and ins[1] == 'LSHIFT':
            res = fix_rep(get_val(ins[0]) << get_val(ins[2]))
        elif len(ins) == 3 and ins[1] == 'RSHIFT':
            res = fix_rep(get_val(ins[0]) >> get_val(ins[2]))
        elif len(ins) == 2 and ins[0] == 'NOT':
            res = fix_rep(~get_val(ins[1]))
        cached[wire] = res
        return res

    # for c in list('defghixy'):
    #     print(get_final(c))

    print(get_final('a'))

if __name__ == '__main__':
    main()
    main2()
