import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '23_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    def parse(x):
        b = x.split('-')
        return frozenset([b[0], b[1]])
    data = [parse(dat) for dat in data]

    all_connections = set(data)
    # print_2d(all_connections)

    all_comps = set()
    for d in data:
        for k in d:
            all_comps.add(k)

    # print_2d(data)
    # print_2d(all_comps)
    triples = set()
    for d in all_connections:
        l_d = list(d)
        first = l_d[0]
        second = l_d[1]
        # print(first, second)
        for c in all_comps:
            if frozenset([c, first]) in all_connections and frozenset([c, second]) in all_connections:
                # print('YES', c)
                triples.add(frozenset([c, first, second]))
    # print_2d(triples)
    final_counter = 0
    for t in triples:
        for inner_t in t:
            if inner_t.startswith('t'):
                final_counter += 1
                break
    print(final_counter)


def main2():
    data = readlines(FILENAME)
    def parse(x):
        b = x.split('-')
        return frozenset([b[0], b[1]])
    data = [parse(dat) for dat in data]

    all_2_connections = set(data)

    all_comps = set()
    for d in data:
        for k in d:
            all_comps.add(k)

    def up_level(n_connections, n):
        n_plus_one_connections = set()
        for d in n_connections:
            l_d = list(d)
            first = l_d[0]
            rest = l_d[1:]
            for c in all_comps:
                if frozenset([c] + rest) in n_connections and frozenset([c, first]) in all_2_connections:
                    n_plus_one_connections.add(frozenset([c, first] + rest))
        return n_plus_one_connections

    level = 2
    n_connections = all_2_connections
    while True:
        print(level, len(n_connections))
        # print(level, n_connections)
        # print()
        n_connections = up_level(n_connections, level)
        level += 1
        if len(n_connections) == 1:
            print(','.join(sorted(list(n_connections)[0])))
            break


    # print_2d(all_2_connections)
    # thirds = up_level(all_2_connections, 2)
    # print_2d(thirds)
    # fourths = up_level(thirds, 3)
    # print_2d(fourths)
    # fifths = up_level(fourths, 3)
    # print('a', fifths)

if __name__ == '__main__':
    # main()
    main2()
