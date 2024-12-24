import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '24_dat.txt'
mapper = {}

def parse_input(line):
    x = line.split(':')
    return (x[0].strip(), x[1].strip() == '1')

def parse_logic(line):
    x = line.split('->')
    outp = x[1].strip()
    inp = x[0]
    if ' AND ' in inp:
        y = inp.split('AND')
        return ('AND', y[0].strip(), y[1].strip(), outp)
    if ' XOR ' in inp:
        y = inp.split('XOR')
        return ('XOR', y[0].strip(), y[1].strip(), outp)
    if ' OR ' in inp:
        y = inp.split('OR')
        return ('OR', y[0].strip(), y[1].strip(), outp)
    assert False

def main():
    data = readlines_split_by_newlines(FILENAME)
    initials = [parse_input(dat) for dat in data[0]]
    wires = [parse_logic(dat) for dat in data[1]]
    # print_2d(initials)
    # print_2d(wires)

    known_map = dict()
    for i in initials:
        known_map[i[0]] = i[1]
    # print(known_map)

    connection_map = dict()
    for i in wires:
        connection_map[i[3]] = (i[0], i[1], i[2])
    # print(connection_map)

    all_items = set()
    for i in initials:
        all_items.add(i[0])
    for i in wires:
        all_items.add(i[1])
        all_items.add(i[2])
        all_items.add(i[3])

    # print(all_items)
    while len(known_map) != len(all_items):
        # print('x', len(known_map), len(all_items))
        for connection in connection_map:
            # print(connection)
            if connection in known_map:
                continue # already known
            logic = connection_map[connection]
            # print(logic)
            if not (logic[1] in known_map and logic[2] in known_map):
                continue # cannot determine yet
            inp1 = known_map[logic[1]]
            inp2 = known_map[logic[2]]
            if logic[0] == 'AND':
                # print('AND')
                known_map[connection] = inp1 and inp2
                continue
            if logic[0] == 'XOR':
                # print('XOR')
                known_map[connection] = inp1 ^ inp2
                continue
            if logic[0] == 'OR':
                # print('OR')
                known_map[connection] = inp1 or inp2
                continue
            assert False
        # exit(1)

    # print(known_map)

    z_index = 0
    ans = []
    while True:
        maybe_wire = f'z{z_index:02}'
        if maybe_wire not in known_map:
            break
        ans.append(1 if known_map[maybe_wire] else 0)
        z_index += 1
    
    real = 0
    for k in reversed(ans):
        real += k
        real *= 2
    print(real // 2)

def main2():
    data = readlines_split_by_newlines(FILENAME)
    initials = [parse_input(dat) for dat in data[0]]
    wires = [parse_logic(dat) for dat in data[1]]
    # print_2d(initials)
    # print_2d(wires)

    known_map = dict()
    for i in initials:
        known_map[i[0]] = False
    # print(known_map)

    connection_map = dict()
    for i in wires:
        connection_map[i[3]] = (i[0], i[1], i[2])
    # print(connection_map)

    all_items = set()
    for i in initials:
        all_items.add(i[0])
    for i in wires:
        all_items.add(i[1])
        all_items.add(i[2])
        all_items.add(i[3])

    # print(all_items)
    while len(known_map) != len(all_items):
        # print('x', len(known_map), len(all_items))
        for connection in connection_map:
            # print(connection)
            if connection in known_map:
                continue # already known
            logic = connection_map[connection]
            # print(logic)
            if not (logic[1] in known_map and logic[2] in known_map):
                continue # cannot determine yet
            inp1 = known_map[logic[1]]
            inp2 = known_map[logic[2]]
            if logic[0] == 'AND':
                # print('AND')
                known_map[connection] = inp1 and inp2
                continue
            if logic[0] == 'XOR':
                # print('XOR')
                known_map[connection] = inp1 ^ inp2
                continue
            if logic[0] == 'OR':
                # print('OR')
                known_map[connection] = inp1 or inp2
                continue
            assert False
        # exit(1)

    # print(known_map)

    z_index = 0
    ans = []
    while True:
        maybe_wire = f'z{z_index:02}'
        if maybe_wire not in known_map:
            break
        ans.append(1 if known_map[maybe_wire] else 0)
        z_index += 1
    
    real = 0
    for k in reversed(ans):
        real += k
        real *= 2
    print(real // 2)

if __name__ == '__main__':
    # main()
    main2()
