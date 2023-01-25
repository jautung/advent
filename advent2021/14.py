import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '14_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    top = data[0][0]
    data = [dat.split(' -> ') for dat in data[1]]
    # print(top)
    # print(data)

    insertions = {}
    for dat in data:
        insertions[dat[0]] = dat[1]
    # print(insertions)
    # print(top)
    template = top
    for i in range(10):
        template = step(template, insertions)
    # print(template)
    # print(len(template))

    a = most_common(list(template))
    b = least_common(list(template))
    print(template.count(a)-template.count(b))
    # print(a, b)
    
def step(template, insertions):
    pairs = [template[i:i+2] for i in range(len(template)-1)]
    btwns = [insertions[pair] for pair in pairs]
    new = ''
    for i in range(len(template)):
        new += template[i]
        if i == len(template) - 1:
            break
        new += btwns[i]
    # print(pairs, btwns)
    return new

# Time: 8:45

def main2():
    data = readlines_split_by_newlines(FILENAME)
    top = data[0][0]
    data = [dat.split(' -> ') for dat in data[1]]
    # print(top)
    # print(data)

    insertions = {}
    for dat in data:
        insertions[dat[0]] = dat[1]

    pair_mapping = {}
    for insertion in insertions:
        new = insertions[insertion]
        pair_mapping[insertion] = [insertion[0]+new, new+insertion[1]]
    # print(pair_mapping)

    template = top
    pairs = [template[i:i+2] for i in range(len(template)-1)]
    pair_count = def_dict(0)
    for pair in pairs:
        pair_count[pair] += 1
    # print(pair_count)

    for i in range(40):
        pair_count = step2(pair_count, pair_mapping)
    # print(pair_count)

    first = main1_prime()
    last = main1_prime2()
    # print(first, last)

    letter_counts = def_dict(0)
    for item in pair_count:
        n = pair_count[item]
        letter_counts[item[0]] += n
        letter_counts[item[1]] += n
    letter_counts[first] += 1
    letter_counts[last] += 1

    a = sorted(list(letter_counts.items()), key=lambda x: x[1])
    print(a[-1][1]//2 - a[0][1]//2)

    # a = most_common(list(template))
    # b = least_common(list(template))
    # print(template.count(a)-template.count(b))
    # print(a, b)

def main1_prime():
    data = readlines_split_by_newlines(FILENAME)
    top = data[0][0]
    data = [dat.split(' -> ') for dat in data[1]]
    # print(top)
    # print(data)

    insertions = {}
    for dat in data:
        insertions[dat[0]] = dat[1]
    # print(insertions)
    # print(top)
    template = top[:2]
    for i in range(40):
        template = step1_prime(template, insertions)
    return template[0]
    # print(template)
    # print(len(template))

    # a = most_common(list(template))
    # b = least_common(list(template))
    # print(template.count(a)-template.count(b))
    # print(a, b)

def step1_prime(template, insertions):
    pairs = [template[i:i+2] for i in range(len(template)-1)]
    btwns = [insertions[pair] for pair in pairs]
    new = ''
    for i in range(len(template)):
        new += template[i]
        if i == len(template) - 1:
            break
        new += btwns[i]
    # print(pairs, btwns)
    return new[:2]

def main1_prime2():
    data = readlines_split_by_newlines(FILENAME)
    top = data[0][0]
    data = [dat.split(' -> ') for dat in data[1]]
    # print(top)
    # print(data)

    insertions = {}
    for dat in data:
        insertions[dat[0]] = dat[1]
    # print(insertions)
    # print(top)
    template = top[-2:]
    for i in range(40):
        template = step1_prime2(template, insertions)
    return template[-1]
    # print(template)
    # print(len(template))

    # a = most_common(list(template))
    # b = least_common(list(template))
    # print(template.count(a)-template.count(b))
    # print(a, b)

def step1_prime2(template, insertions):
    pairs = [template[i:i+2] for i in range(len(template)-1)]
    btwns = [insertions[pair] for pair in pairs]
    new = ''
    for i in range(len(template)):
        new += template[i]
        if i == len(template) - 1:
            break
        new += btwns[i]
    # print(pairs, btwns)
    return new[-2:]

def step2(pair_count, pair_mapping):
    new_pair_count = def_dict(0)
    for pair in pair_count:
        n = pair_count[pair]
        new_pair_count[pair_mapping[pair][0]] += n
        new_pair_count[pair_mapping[pair][1]] += n
        # print(n, pair_mapping[pair][0], pair_mapping[pair][1])
    return new_pair_count

# Time: 27:16

if __name__ == '__main__':
    main()
    main2()
