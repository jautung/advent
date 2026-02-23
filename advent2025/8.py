import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
mapper = {}

def distance_sq(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

# FIRST_N = 10
FIRST_N = 1000

def main():
    data = readlines(FILENAME)
    data = [[int(d) for d in dat.split(',')] for dat in data]
    # print_2d(data)
    num_total = len(data)

    dists = {}
    dist_tups = []
    for i in range(num_total):
        for j in range(i+1, num_total):
            d = distance_sq(data[i], data[j])
            dists[(i,j)] = d
            dist_tups.append((d, (i,j)))
    # print_2d(dist_tups)
    dist_tups.sort()
    # print_2d(dist_tups)
    connections = [k[1] for k in dist_tups[:FIRST_N]]
    # print(connections)

    def get_neighbors(node):
        res = set()
        for c in connections:
            if c[0] == node:
                res.add(c[1])
            elif c[1] == node:
                res.add(c[0])
        return res

    # bfs it out
    groups = []
    seen = set()
    for i in range(num_total):
        if i in seen:
            continue
        seen.add(i)

        group = set()
        group.add(i)
        to_search = [i]
        while len(to_search) > 0:
            search = to_search.pop()
            neighbors = get_neighbors(search)
            for neighbor in neighbors:
                if neighbor in group:
                    continue
                seen.add(neighbor)
                group.add(neighbor)
                to_search.append(neighbor)
        # print("group", group)
        groups.append(group)

    # print("all", groups)
    lens = [len(g) for g in groups]
    lens.sort(reverse=True)
    # print(lens)
    print(product(lens[:3]))

def main2():
    data = readlines(FILENAME)
    data = [[int(d) for d in dat.split(',')] for dat in data]
    # print_2d(data)
    num_total = len(data)

    dists = {}
    dist_tups = []
    for i in range(num_total):
        for j in range(i+1, num_total):
            d = distance_sq(data[i], data[j])
            dists[(i,j)] = d
            dist_tups.append((d, (i,j)))
    # print_2d(dist_tups)
    dist_tups.sort()
    # print_2d(dist_tups)
    connections = [k[1] for k in dist_tups]
    # these are connections in order
    # print(connections)

    index_to_group_mapping = dict()
    group_to_indices_mapping = dict()
    for i in range(num_total):
        index_to_group_mapping[i] = i
        group_to_indices_mapping[i] = set([i])
    
    # print(index_to_group_mapping)
    # print(group_to_indices_mapping)

    group_number = num_total
    for connect in connections:
        # simul connecting those two
        a = connect[0]
        b = connect[1]
        group_a = index_to_group_mapping[a]
        group_b = index_to_group_mapping[b]
        if group_a == group_b:
            # does nothing
            continue
        # merge group_a and group_b into a new group number
        new_gn = group_number
        group_number += 1

        new_set = set()
        for i in group_to_indices_mapping[group_a]:
            index_to_group_mapping[i] = new_gn
            new_set.add(i)
        for i in group_to_indices_mapping[group_b]:
            index_to_group_mapping[i] = new_gn
            new_set.add(i)

        del group_to_indices_mapping[group_a]
        del group_to_indices_mapping[group_b]
        group_to_indices_mapping[new_gn] = new_set

        if len(new_set) == num_total:
            # print('yay', connect)
            last_connect = connect
            break

    # print(last_connect)
    connect_a = data[last_connect[0]]
    connect_b = data[last_connect[1]]
    # print(connect_a, connect_b)

    print(connect_a[0] * connect_b[0])

if __name__ == '__main__':
    main()
    main2()
