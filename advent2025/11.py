import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '11_dat.txt'
mapper = {}

def parse_line(line):
    parts = line.split(':')
    start = parts[0].strip()
    connectors = set([x.strip() for x in parts[1].strip().split(' ')])
    return start, connectors

def main():
    data = readlines(FILENAME)
    data = [parse_line(dat) for dat in data]
    # print_2d(data)

    # top-down DP
    cached = dict() # mapping from nodes to a list of paths
    pending_compute = set()
    counter = [1]
    def find_all_paths(end_node):
        assert end_node not in pending_compute
        if end_node in cached:
            return cached[end_node]
        if end_node == "you":
            cached[end_node] = [[end_node]]
            return cached[end_node]
        # print('computing', counter[0], end_node)
        counter[0] += 1
        pending_compute.add(end_node)
        all_paths = []
        for dat in data:
            start, connectors = dat
            if end_node in connectors:
                if start in pending_compute:
                    assert False
                    continue
                prev_paths = find_all_paths(start)
                all_paths += [pp + [end_node] for pp in prev_paths]
        pending_compute.remove(end_node)
        cached[end_node] = all_paths
        return cached[end_node]

    out_paths = find_all_paths("out")
    # print_2d(out_paths)
    print(len(out_paths))

def add_4_tup(a,b):
    a0,a1,a2,a3 = a
    b0,b1,b2,b3 = b
    return a0+b0,a1+b1,a2+b2,a3+b3

def main2():
    data = readlines(FILENAME)
    data = [parse_line(dat) for dat in data]
    # print_2d(data)

    # top-down DP
    # always starting from "svr"
    # mapping from end-node to a 4-tuple of:
    # 1. num paths containing both "dac" and "fft"
    # 2. num paths containing "dac" not "fft"
    # 3. num paths containing "fft" not "dac"
    # 4. num paths containing neither "dac" nor "fft"
    cached = dict()
    pending_compute = set()
    counter = [1]
    def find_all_paths(end_node):
        assert end_node not in pending_compute
        if end_node in cached:
            return cached[end_node]
        if end_node == "svr":
            cached[end_node] = (0,0,0,1)
            return cached[end_node]
        # print('computing', counter[0], end_node)
        counter[0] += 1
        pending_compute.add(end_node)
        final_tup = (0,0,0,0)
        for dat in data:
            start, connectors = dat
            if end_node in connectors:
                if start in pending_compute:
                    assert False
                    continue
                # print("- before recursive find_all_paths")
                prev_paths = find_all_paths(start)
                if end_node == "dac":
                    assert prev_paths[0] == 0
                    assert prev_paths[1] == 0
                    increment_tup = (prev_paths[0] + prev_paths[2],prev_paths[1] + prev_paths[3],0,0)
                elif end_node == "fft":
                    assert prev_paths[0] == 0
                    assert prev_paths[2] == 0
                    increment_tup = (prev_paths[0] + prev_paths[1],0,prev_paths[2] + prev_paths[3],0)
                else:
                    increment_tup = prev_paths
                # print(f"- after recursive find_all_paths, {len(prev_paths)}")
                # final_tup += [pp.union(set([end_node])) for pp in prev_paths]
                final_tup = add_4_tup(final_tup, increment_tup)
                # print(f"- after append recursive find_all_paths, {len(prev_paths)}")
        pending_compute.remove(end_node)
        cached[end_node] = final_tup
        return cached[end_node]

    out_paths = find_all_paths("out")
    # print(out_paths)
    print(out_paths[0])
    # print('filtering')
    # filtered_out_paths = [op for op in out_paths if "dac" in op and "fft" in op]
    # print_2d(filtered_out_paths)
    # print(len(filtered_out_paths))

if __name__ == '__main__':
    main()
    main2()
