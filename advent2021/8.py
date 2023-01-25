import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
mapper = {
    frozenset(['c','f']): '1',
    frozenset(['a','c','f']): '7',
    frozenset(['b','c','d','f']): '4',
    frozenset(['a','c','d','e','g']): '2',
    frozenset(['a','c','d','f','g']): '3',
    frozenset(['a','b','d','f','g']): '5',
    frozenset(['a','b','c','e','f','g']): '0',
    frozenset(['a','b','d','e','f','g']): '6',
    frozenset(['a','b','c','d','f','g']): '9',
    frozenset(['a','b','c','d','e','f','g']): '8',
}

def main():
    data = readlines(FILENAME)
    data = [[[set(i) for i in j.split()] for j in dat.split(' | ')] for dat in data]
    easy_sizes = [2, 4, 3, 7]
    count = 0
    for dat in data:
        easy_sets = []
        for item in dat[0]:
            if len(item) in easy_sizes:
                easy_sets.append(item)
        for out in dat[1]:
            if out in easy_sets:
                count += 1
    print(count)

def main2():
    data = readlines(FILENAME)
    data = [[[set(i) for i in j.split()] for j in dat.split(' | ')] for dat in data]

    outs = []
    for dat in data:
        bar_mapping = {} # encoded to real
        fives = []
        sixes = []
        for item in dat[0]:
            if len(item) == 2:
                cf = item
            elif len(item) == 4:
                bcdf = item
            elif len(item) == 5:
                fives.append(item)
            elif len(item) == 6:
                sixes.append(item)
            elif len(item) == 3:
                acf = item
            elif len(item) == 7:
                abcdefg = item
        adg = fives[0].intersection(fives[1]).intersection(fives[2])
        abfg = sixes[0].intersection(sixes[1]).intersection(sixes[2])

        a = acf - cf
        abcdf = acf.union(bcdf)
        bcdf = abcdf - a

        bd = bcdf - cf
        cf = cf
        eg = abcdefg - abcdf

        dg = adg - a
        bfg = abfg - a

        d = bd.intersection(dg)
        b = bd - d
        g = dg - d
        e = eg - g
        f = bfg - b - g
        c = cf - f

        bar_mapping[a.pop()] = 'a'
        bar_mapping[b.pop()] = 'b'
        bar_mapping[c.pop()] = 'c'
        bar_mapping[d.pop()] = 'd'
        bar_mapping[e.pop()] = 'e'
        bar_mapping[f.pop()] = 'f'
        bar_mapping[g.pop()] = 'g'

        decoded_vals = []
        for out in dat[1]:
            decoded_out = [bar_mapping[i] for i in out]
            decoded_val = mapper[frozenset(decoded_out)]
            decoded_vals.append(decoded_val)
        outs.append(int(''.join(decoded_vals)))
    print(sum(outs))

if __name__ == '__main__':
    main()
    main2()

# 40:55
