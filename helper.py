from collections import Counter
from collections import defaultdict
import math

################################################################################
# PARSING
################################################################################

def readlines(filename):
    f = open(filename, 'r')
    return [line.strip('\n') for line in f.readlines()]

def readlines_split_each_line(filename):
    f = open(filename, 'r')
    return [line.strip('\n').split() for line in f.readlines()]

def readlines_split_by_newlines(filename):
    f = open(filename, 'r')
    lines = [line.strip('\n') for line in f.readlines()]
    res = []
    group = []
    for line in lines:
        if line == '':
            res.append(group)
            group = []
        else:
            group.append(line)
    if len(group) > 0:
        res.append(group)
    return res

def readlines_partitioned(filename, n):
    f = open(filename, 'r')
    lines = [line.strip('\n') for line in f.readlines()]
    return [lines[i:i+n] for i in range(0, len(lines), n)]

def readlines_sliding(filename, n):
    f = open(filename, 'r')
    lines = [line.strip('\n') for line in f.readlines()]
    return [lines[i:i+n] for i in range(0, len(lines)-n+1)]

################################################################################
# RANDOM
################################################################################

def print_2d(array):
    for row in array:
        print(row)
    print()

def transpose(matrix):
    return [*zip(*matrix)]

def product(lst):
    return math.prod(lst)

def most_common(lst, default_if_tie = None):
    res = Counter(lst).most_common()
    if len(res) == 1:
        return res[0][0]
    elif res[0][1] == res[1][1]:
        return default_if_tie
    else:
        return res[0][0]

def least_common(lst, default_if_tie = None):
    res = Counter(lst).most_common()
    if len(res) == 1:
        return res[-1][0]
    elif res[-1][1] == res[-2][1]:
        return default_if_tie
    else:
        return res[-1][0]

def bin_to_int(bin_rep):
    return int(bin_rep, 2)

def flatten(lst):
    if len(lst) == 0:
        return lst
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])

def def_dict(val):
    return defaultdict(lambda: val)

def dupe_array_with_def_value(array, val):
    return [[val for j in range(len(array[0]))] for i in range(len(array))]

def add_tup(a, b):
    return (a[0] + b[0], a[1] + b[1])

def manhattan(a, b=(0,0)):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
