import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '12_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [dat.split('-') for dat in data]
    vertices = set(flatten(data))
    edges = [frozenset([dat[0], dat[1]]) for dat in data]

    def find_potential(vertex, exhausted):
        res = set()
        for dest in vertices:
            if dest == 'start':
                continue
            if dest == vertex:
                continue
            if dest in exhausted:
                continue
            if frozenset([vertex, dest]) in edges:
                res.add(dest)
        return res

    # print(vertices)
    # print(edges)
    # print(find_potential('start', set()))
    paths = [(['start'], set())]
    full_paths = []
    while len(paths) > 0:
        # print(paths)
        path = paths.pop()
        exhausted = copy.deepcopy(path[1])
        dests = find_potential(path[0][-1], exhausted)
        for dest in dests:
            exhausted = copy.deepcopy(path[1])
            if dest == 'end':
                full_paths.append(path[0] + [dest])
                continue
            if dest.islower():
                exhausted.add(dest)
                paths.append((path[0] + [dest], exhausted))
            else:
                paths.append((path[0] + [dest], exhausted))
    # for i in full_paths:
    #     print(i)
    print(len(full_paths))

# Time: 13:22

def main2():
    data = readlines(FILENAME)
    data = [dat.split('-') for dat in data]
    vertices = set(flatten(data))
    edges = [frozenset([dat[0], dat[1]]) for dat in data]

    def find_potential(vertex, exhausted, used_special_case):
        res = set()
        for dest in vertices:
            if dest == 'start':
                continue
            if dest == vertex:
                continue
            if frozenset([vertex, dest]) in edges:
                if dest in exhausted:
                    if used_special_case:
                        continue
                    else:
                        res.add((dest, True))
                else:
                    res.add((dest, used_special_case))
        return res

    # print(vertices)
    # print(edges)
    # print(find_potential('start', set()))
    paths = [(['start'], set(), False)]
    full_paths = []
    i = 0
    while len(paths) > 0:
        i += 1
        # print(paths)
        # print()
        path = paths.pop()
        exhausted = copy.deepcopy(path[1])
        used_special_case = path[2]
        dests = find_potential(path[0][-1], exhausted, used_special_case)
        for dest, new_used_special_case in dests:
            exhausted = copy.deepcopy(path[1])
            if dest == 'end':
                full_paths.append(path[0] + [dest])
                continue
            if dest.islower():
                exhausted.add(dest)
                paths.append((path[0] + [dest], exhausted, new_used_special_case))
            else:
                paths.append((path[0] + [dest], exhausted, new_used_special_case))
        # if i == 4:
        #     break
    # for i in full_paths:
    #     print(i)
    print(len(full_paths))

# Time: 23:40

if __name__ == '__main__':
    main()
    main2()
