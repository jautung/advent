import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '18_dat.txt'
DATA = [
    [[[3,9],[7,2]],[[8,4],[[5,6],0]]],
    [[[1,[4,9]],[[1,8],[1,5]]],[[[2,6],[6,7]],[[4,6],[9,0]]]],
    [[[[9,2],1],[[0,7],[9,6]]],[[5,9],[7,[6,9]]]],
    [8,9],
    [[4,[6,1]],[2,[[6,7],2]]],
    [[6,[[4,1],5]],[4,9]],
    [[[0,6],[8,[8,5]]],[6,9]],
    [[0,[1,0]],[[8,[7,4]],[[1,1],[5,0]]]],
    [[[1,[0,1]],6],[1,9]],
    [[2,[[9,0],[6,1]]],[[8,4],[5,7]]],
    [[[[5,3],[0,9]],[1,[0,7]]],[[9,0],[2,[2,0]]]],
    [[2,[2,[6,8]]],[[9,[5,4]],[4,[3,4]]]],
    [[[[4,0],[7,0]],[[4,8],[5,8]]],[[[7,2],[2,2]],[[3,3],3]]],
    [[5,0],5],
    [[8,[[5,0],2]],[6,[5,1]]],
    [[[9,[8,8]],[8,7]],[[[4,2],4],[[5,1],[4,8]]]],
    [[[[1,1],3],5],9],
    [[[[1,7],[6,5]],5],[[0,6],0]],
    [[9,6],2],
    [[[2,[0,8]],[8,[2,1]]],5],
    [[[9,[3,7]],3],[0,[5,9]]],
    [[[2,[1,7]],6],[[7,[8,2]],[[8,2],8]]],
    [[[[1,2],1],5],2],
    [4,[8,[3,9]]],
    [[[[8,9],[6,0]],[[1,6],7]],8],
    [[2,[8,1]],3],
    [[2,2],[[8,[0,2]],[[5,0],5]]],
    [9,[2,[[6,1],[8,9]]]],
    [[4,[[6,6],4]],[[[9,3],[3,1]],5]],
    [[[7,8],1],0],
    [[[8,8],[[1,0],7]],[4,6]],
    [9,8],
    [[[[4,2],9],[[9,9],7]],[7,[9,[5,8]]]],
    [[4,[4,[3,3]]],8],
    [0,2],
    [[4,[5,5]],[9,[[6,9],4]]],
    [[[7,3],[[1,2],6]],[[[2,4],[6,7]],[[5,0],9]]],
    [[[[2,0],5],[4,5]],[[[6,5],[6,0]],[1,[3,4]]]],
    [[3,[6,8]],[[[3,0],0],[[2,8],7]]],
    [[[4,[6,2]],[9,[4,1]]],[8,[3,4]]],
    [[[6,[6,8]],[7,[2,0]]],[4,[[8,7],[1,6]]]],
    [2,[0,[4,0]]],
    [[[[0,5],1],8],[[9,[0,3]],3]],
    [[[3,[5,2]],[3,[3,2]]],[[[7,3],1],7]],
    [1,[[[1,8],[1,7]],0]],
    [[8,6],[[0,4],4]],
    [[[8,2],[4,6]],3],
    [5,[[[7,5],[4,5]],[0,2]]],
    [[3,[3,6]],6],
    [[[[6,8],[5,7]],[[7,3],5]],[[8,[4,8]],8]],
    [[[[5,8],[3,1]],[[3,7],[7,0]]],[[9,7],0]],
    [[2,[[5,3],8]],0],
    [0,[2,8]],
    [[8,9],[[[2,2],[4,7]],[[4,0],1]]],
    [[[[3,0],8],[[7,3],[6,1]]],[[3,8],[4,2]]],
    [[[[6,7],[4,3]],[[3,9],5]],8],
    [[[7,7],[[3,4],7]],[[[0,4],1],9]],
    [[[7,5],5],[[2,[9,9]],[0,[3,5]]]],
    [[[[3,3],[6,1]],[5,8]],[[4,7],[8,1]]],
    [[[0,[7,3]],[6,[7,2]]],[[0,8],7]],
    [[[2,7],[9,7]],[8,[3,8]]],
    [[[0,2],6],[[9,[6,5]],[[3,9],1]]],
    [[7,[[3,4],[2,8]]],[[[4,1],4],7]],
    [[3,[[3,4],6]],[[3,9],[[4,5],[3,0]]]],
    [[[5,[5,1]],[2,4]],[1,[[1,6],6]]],
    [[[5,6],[[1,3],[5,0]]],[[[4,1],8],[5,5]]],
    [[[[2,0],7],[[8,9],1]],[[[4,0],[1,6]],1]],
    [[[2,0],[[4,2],[9,9]]],[4,9]],
    [[[[1,9],6],2],[[5,4],[2,4]]],
    [[[[4,1],[4,5]],[[2,3],2]],[3,[[8,8],1]]],
    [[[[8,1],0],[2,2]],[[2,[7,1]],1]],
    [[[7,4],[[1,3],5]],[[6,8],[[0,0],2]]],
    [[[1,2],8],[[[1,7],[4,0]],[[8,2],8]]],
    [[[0,8],[3,6]],[[[5,3],7],[9,7]]],
    [[4,6],[[[7,9],[7,5]],[[4,6],[8,4]]]],
    [[[[7,3],0],[[6,2],[7,2]]],[9,[[8,0],3]]],
    [[[3,0],1],[[2,3],1]],
    [[[5,[8,6]],[[1,2],2]],[[[1,4],6],[5,[7,1]]]],
    [[[[1,5],8],[0,0]],4],
    [[[7,[6,8]],3],[[5,1],[[2,8],[4,6]]]],
    [3,[[[5,8],[4,5]],[[7,7],8]]],
    [[6,[7,[8,2]]],[[9,0],0]],
    [[[8,[7,6]],1],[[2,4],6]],
    [[[[0,4],2],[0,7]],[6,6]],
    [1,[[1,9],[9,3]]],
    [[[[5,2],[5,3]],[[9,0],4]],2],
    [[[[5,5],3],[7,[1,2]]],[6,[7,2]]],
    [[[[2,1],3],8],[[2,[8,2]],[7,4]]],
    [[8,[9,[1,8]]],[[[4,4],[0,6]],[6,3]]],
    [[[1,6],[1,[2,5]]],0],
    [[[[0,1],[7,2]],[[7,2],3]],[2,[[7,8],[0,7]]]],
    [[[[1,8],8],[[5,7],[3,4]]],[[[2,5],[7,4]],[[8,4],9]]],
    [[[2,2],[5,[1,0]]],[[[6,6],[3,0]],[[8,5],5]]],
    [[[[8,2],[4,8]],[9,4]],[[8,[7,9]],0]],
    [[3,[5,[2,4]]],[[[8,1],0],[[0,4],[4,5]]]],
    [[5,[9,[3,8]]],[4,[1,[5,2]]]],
    [[[3,[0,6]],[7,[8,7]]],[[6,8],[[8,7],0]]],
    [[[[0,2],5],[4,6]],3],
    [[6,7],[[1,[4,6]],9]],
    [7,[3,[[8,8],5]]],
]

# DATA = [
#     [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
#     [[[5,[2,8]],4],[5,[[9,9],0]]],
#     [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
#     [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
#     [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
#     [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
#     [[[[5,4],[7,7]],8],[[8,3],8]],
#     [[9,3],[[9,9],[6,[4,9]]]],
#     [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
#     [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]],
# ]

def main():
    trees = [convert_to_tree(dat) for dat in DATA]
    running_sum = trees[0]
    for i in range(1, len(trees)):
        new = trees[i]
        running_sum = add_trees(running_sum, new)
        # print('running_sum', read_as_snail(running_sum))
        snail_reduce_full(running_sum)
    # print(read_as_snail(running_sum))
    print(magnitude(running_sum))

    # tree = convert_to_tree([12,1])
    # print_tree(tree)
    # updated = snail_reduce(tree)
    # print()
    # print(updated)
    # print_tree(tree)
    # print(read_as_snail(tree))

class Node:
   def __init__(self, left=None, right=None, parent=None, number=None, depth=None):
      self.left = left
      self.right = right
      self.parent = parent
      self.number = number
      self.depth = depth

def convert_to_tree(snail, depth=0):
    if isinstance(snail, list):
        new_node = Node(left=convert_to_tree(snail[0], depth=depth+1), right=convert_to_tree(snail[1], depth=depth+1), depth=depth)
        new_node.left.parent = new_node
        new_node.right.parent = new_node
        return new_node
    else:
        return Node(number=snail, depth=depth)

def print_tree(node, indentation=0):
    if node.left == None and node.right == None:
        print(' ' * indentation + str(node.number) + '(depth=' + str(node.depth) + ')' + '; parent', node.parent != None)
    else:
        print_tree(node.left, indentation=indentation+1)
        print(' ' * indentation + '*' + '(depth=' + str(node.depth) + ')' + '; parent', node.parent != None)
        print_tree(node.right, indentation=indentation+1)

def read_as_snail(node):
    if node.left == None and node.right == None:
        return str(node.number)
    else:
        return '[' + read_as_snail(node.left) + ',' + read_as_snail(node.right) + ']'

def add_trees(node1, node2):
    new_node = Node(left=node1, right=node2, depth=0)
    incr_depth(node1)
    incr_depth(node2)
    node1.parent = new_node
    node2.parent = new_node
    return new_node

def incr_depth(node):
    node.depth += 1
    if node.left != None and node.right != None:
        incr_depth(node.left)
        incr_depth(node.right)

def snail_reduce_full(node):
    while True:
        # print('snail_reduce_full_iter', read_as_snail(node))
        # print_tree(node)
        if not snail_reduce(node):
            break

def snail_reduce(node):
    updated = False
    exploder = leftmost_exploder(node)
    if exploder != None:
        # print('exploding')
        explode(exploder)
        updated = True
    else:
        splitter = leftmost_fattie(node)
        if splitter != None:
            # print('splitting')
            split(splitter)
            updated = True
    return updated

def leftmost_exploder(node):
    if node.depth == 4 and node.left != None and node.right != None:
        return node
    if node.left == None and node.right == None:
        return None
    try_left = leftmost_exploder(node.left)
    if try_left != None:
        return try_left
    else:
        return leftmost_exploder(node.right)

def explode(node):
    left_neighbor = rightmost_left_neighbor(node)
    if left_neighbor:
        left_neighbor.number += node.left.number
    right_neighbor = leftmost_right_neighbor(node)
    if right_neighbor:
        right_neighbor.number += node.right.number
    new_node = Node(number=0,depth=node.depth)
    if node.parent.left == node:
        # print('left')
        node.parent.left = new_node
        new_node.parent = node.parent
    elif node.parent.right == node:
        # print('right')
        node.parent.right = new_node
        new_node.parent = node.parent

def rightmost_left_neighbor(node):
    if node.parent == None:
        return None
    elif node.parent.left == node:
        return rightmost_left_neighbor(node.parent)
    elif node.parent.right == node:
        return rightmost_leaf(node.parent.left)

def rightmost_leaf(node):
    if node.left == None and node.right == None:
        return node
    else:
        return rightmost_leaf(node.right)

def leftmost_right_neighbor(node):
    if node.parent == None:
        return None
    elif node.parent.right == node:
        return leftmost_right_neighbor(node.parent)
    elif node.parent.left == node:
        return leftmost_leaf(node.parent.right)

def leftmost_leaf(node):
    if node.left == None and node.right == None:
        return node
    else:
        return leftmost_leaf(node.left)

def leftmost_fattie(node):
    if node.left == None and node.right == None and node.number >= 10:
        return node
    if node.left == None and node.right == None:
        return None
    try_left = leftmost_fattie(node.left)
    if try_left != None:
        return try_left
    else:
        return leftmost_fattie(node.right)

def split(node):
    new_left = node.number // 2
    new_right = node.number - new_left
    new_node = Node(left=Node(number=new_left, depth=node.depth+1), right=Node(number=new_right, depth=node.depth+1), depth=node.depth)
    new_node.left.parent = new_node
    new_node.right.parent = new_node
    if node.parent.left == node:
        # print('left')
        node.parent.left = new_node
        new_node.parent = node.parent
    elif node.parent.right == node:
        # print('right')
        node.parent.right = new_node
        new_node.parent = node.parent

def magnitude(node):
    if node.left == None and node.right == None:
        return node.number
    else:
        return 3*magnitude(node.left) + 2*magnitude(node.right)

# def get_nesting(snail, level=0):
#     if not isinstance(snail, list):
#         return (level, snail)
#     return (level, [get_nesting(snail[0], level+1), get_nesting(snail[1], level+1)])

# Time: 1:17:48 --- wow this was hard

def main2():
    trees = [convert_to_tree(dat) for dat in DATA]
    # test_sum = add_trees(convert_to_tree([[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]), convert_to_tree([[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]))
    # snail_reduce_full(test_sum)
    # print(read_as_snail(test_sum))
    # print(magnitude(test_sum))
    max_mag = None
    for tree1 in copy.deepcopy(trees):
        for tree2 in copy.deepcopy(trees):
            test_sum = add_trees(copy.deepcopy(tree1), copy.deepcopy(tree2))
            snail_reduce_full(test_sum)
            mag = magnitude(test_sum)
            if max_mag == None or mag > max_mag:
                max_mag = mag
    print(max_mag)

# Time: 1:28:57

if __name__ == '__main__':
    main()
    main2()
