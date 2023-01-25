import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

class Node:
   def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None
        self.children = []

def main():
    data = readlines_split_each_line(FILENAME)
    in_outs = []
    curr_in = None
    curr_out = []
    for line in data:
        if line[0] == '$':
            if curr_in:
                in_outs.append((curr_in, curr_out))
                curr_out = []
            curr_in = line[1:]
        else:
            curr_out.append(line)
    if curr_in:
        in_outs.append((curr_in, curr_out))

    # print_2d(in_outs)
    root_tree = Node('/', 0)
    curr_pos = root_tree

    for inp, outp in in_outs:
        if inp[0] == 'ls':
            curr_pos.children = [item_to_node(item) for item in outp]
            for child in curr_pos.children:
                child.parent = curr_pos
        elif inp[0] == 'cd':
            if inp[1] == '..':
                assert(curr_pos.parent != None)
                curr_pos = curr_pos.parent
            else:
                curr_pos = find_child_with_name(curr_pos.children, inp[1])

    # print(size_of_tree(root_tree))
    print(first(root_tree))

def item_to_node(item):
    if item[0] == 'dir':
        return Node(item[1], 0)
    else:
        return Node(item[1], int(item[0]))

def find_child_with_name(children, name):
    for child in children:
        if child.name == name:
            return child
    print(children, name)
    assert(False)
    return None

def size_of_tree(tree):
    return tree.size + sum(size_of_tree(child) for child in tree.children)

def first(tree):
    ret = 0
    root = size_of_tree(tree)
    if tree.size == 0 and root <= 100000:
        ret += root
    return ret + sum(first(child) for child in tree.children)

def main2():
    data = readlines_split_each_line(FILENAME)
    in_outs = []
    curr_in = None
    curr_out = []
    for line in data:
        if line[0] == '$':
            if curr_in:
                in_outs.append((curr_in, curr_out))
                curr_out = []
            curr_in = line[1:]
        else:
            curr_out.append(line)
    if curr_in:
        in_outs.append((curr_in, curr_out))

    # print_2d(in_outs)
    root_tree = Node('/', 0)
    curr_pos = root_tree

    for inp, outp in in_outs:
        if inp[0] == 'ls':
            curr_pos.children = [item_to_node(item) for item in outp]
            for child in curr_pos.children:
                child.parent = curr_pos
        elif inp[0] == 'cd':
            if inp[1] == '..':
                assert(curr_pos.parent != None)
                curr_pos = curr_pos.parent
            else:
                curr_pos = find_child_with_name(curr_pos.children, inp[1])

    used_space = size_of_tree(root_tree)
    curr_unused = 70000000 - used_space
    need_delete = 30000000 - curr_unused
    # print(need_delete)
    print(min_over(root_tree, need_delete))

def min_over(tree, need_delete):
    if len(tree.children) > 0:
        test = min(min_over(child, need_delete) for child in tree.children)
    else:
        test = 70000000
    this = size_of_tree(tree)
    if tree.size == 0 and this >= need_delete:
        return min(test, this)
    return test

if __name__ == '__main__':
    main()
    main2()
