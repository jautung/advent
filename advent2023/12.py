import itertools
import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '12_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [proc(dat) for dat in data]
    # print(data)
    # print([brute(dat) for dat in data])
    # print(sum([brute(dat) for dat in data]))
    s = 0
    for index, dat in enumerate(data):
        # print(f"{index+1} of {len(data)}")
        b = brute(dat)
        s += b
    print(s)

def brute(dat):
    onsen, grps = dat
    # print(onsen, grps)
    possibilities = dr_strange(onsen)
    # print(possibilities)
    b = [groupify(x) for x in possibilities]
    # print(b)
    # exit(1)
    return sum([1 if match(x, grps) else 0 for x in b])

def dr_strange(onsen):
    if '?' not in onsen:
        return [onsen]
    i = onsen.index('?')
    o1 = copy.deepcopy(onsen)
    o1[i] = '.'
    o2 = copy.deepcopy(onsen)
    o2[i] = '#'
    return dr_strange(o1) + dr_strange(o2)

def groupify(x):
    i = itertools.groupby(x)
    return [len(list(group)) for key, group in i if key == '#']

def match(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def proc(dat):
    dat = dat.split()
    onsen = [c for c in dat[0]]
    grps = [int(b) for b in dat[1].split(',')]
    return onsen, grps

def main2():
    data = readlines(FILENAME)
    data = [proc(dat) for dat in data]
    # print(data)
    data = [mod(dat) for dat in data]
    # print(data)
    # print([brute(dat) for dat in data])
    # print(sum([brute(dat) for dat in data]))
    s = 0
    for index, dat in enumerate(data):
        # print(f"{index+1} of {len(data)}")
        b = dp(dat)
        # print(b)
        s += b
    print(s)

def i_non_dot(lst):
    for i in range(len(lst)):
        if lst[i] != '.':
            return i
    return -1

def dp(dat):
    onsen, grps = dat
    real_n = sum(grps)
    min_bound = len([1 for a in onsen if a == '#'])
    maybes = len([1 for a in onsen if a == '?'])
    length_onsen = len(onsen)
    cache = dict()
    return dp_with_meta(onsen, grps, length_onsen, real_n, min_bound, maybes, cache)

def dp_with_meta(onsen, grps, length_onsen, real_n, min_bound, maybes, cache):
    # no way it's the cache right?!!??!?!
    # OMG ITS THE CACHE I SPENT SO MUCH TIME OPTIMIZING EVERYTHING ELSE DERP
    key = ''.join(onsen) + ''.join([str(x) for x in grps])
    if key in cache:
        return cache[key]
    
    # print(onsen, grps, length_onsen, real_n, min_bound, maybes)
    # print(onsen, length_onsen)
    # assert(len(onsen) == length_onsen)
    # onsen, grps = dat
    if real_n < min_bound or real_n > min_bound + maybes:
        cache[key] = 0
        return 0
    
    if length_onsen < real_n + len(grps) - 1:
        cache[key] = 0
        return 0 # not enough for stuff + separators

    # if len(grps) == 0:
    if real_n == 0:
        if '#' in onsen:
            cache[key] = 0
            return 0 # violation
        cache[key] = 1
        return 1 # all empty left
    # print(onsen, grps)
    if length_onsen == 0:
        cache[key] = 0
        return 0 # otherwise would have been up there len(grps) == 0

    if onsen[0] == '.':
        xx = i_non_dot(onsen)
        if xx == -1:
            cache[key] = 0
            return 0 # otherwise would have been up there len(grps) == 0
        cache[key] = dp_with_meta(onsen[xx:], grps, length_onsen - xx, real_n, min_bound, maybes, cache)
        return cache[key]

    if onsen[0] == '#':
        l = grps[0]
        if length_onsen < l:
            cache[key] = 0
            return 0
        question_count = 0
        hash_count = 0
        for c in onsen[:l]:
            if c == '.':
                cache[key] = 0
                return 0
            elif c == '?':
                question_count += 1
            else:
                hash_count += 1
        # if not all([c == '?' or c == '#' for c in onsen[:l]]):
        #     return 0
        # all of these are forced to be #
        if length_onsen > l:
            if onsen[l] == '#':
                cache[key] = 0
                return 0 # we need a separator, so it must be . (or ?)
            if onsen[l] == '.':
                cache[key] = dp_with_meta(onsen[l+1:], grps[1:], length_onsen - l - 1, real_n - l, min_bound - hash_count, maybes - question_count, cache)
                return cache[key]
            if onsen[l] == '?':
                cache[key] = dp_with_meta(onsen[l+1:], grps[1:], length_onsen - l - 1, real_n - l, min_bound - hash_count, maybes - question_count - 1, cache)
                return cache[key]
        return 1 # exact length
    
    if onsen[0] == '?':
        l = grps[0]
        if length_onsen < l:
            cache[key] = 0
            return 0
        # o_copy = copy.deepcopy(onsen)
        # o_copy[0] = '#'
        # order is important here because we mutat
        a1 = dp_with_meta(onsen[1:], grps, length_onsen - 1, real_n, min_bound, maybes - 1, cache)
        onsen[0] = '#'
        # order is important here because we mutat
        a2 = dp_with_meta(onsen, grps, length_onsen, real_n, min_bound + 1, maybes - 1, cache)
        cache[key] = a1 + a2
        return a1 + a2
        # return dp((o_copy, grps)) + dp((onsen[1:], grps))

        # if not all([c == '?' or c == '#' for c in onsen[:l]]):
        #     return 0
        # # all of these are forced to be #
        # if onsen[l] == '#':
        #     return 0 # we need a separator, so it must be . (or ?)
        # return dp((onsen[l+1:], grps[1:]))
    
    # else:
    #     assert(False)
    # i_question = onsen.find('?')
    # i_hash = onsen.find('#')
    # assert(i_question != -1 or i_hash != -1)
    
    # def do_hash(i_hash):
    #     l = grps[0]
    #     if 
    #     pass

    # def do_question(i_question):
    #     pass
    
    # if i_question == -1:
    #     return do_hash(i_hash)
    # elif i_hash == -1:
    #     return do_question(i_question)
    # elif i_question < i_hash:
    #     return do_question(i_question)
    # elif i_hash < i_question:
    #     return do_hash(i_hash)
    # else:
    #     assert(False)
    # exit(1)

def mod(dat):
    onsen, grps = dat
    # print(onsen)
    k = '?'.join([''.join(onsen)] * 5)
    # print(k)
    return [c for c in k], grps * 5
    # exit(1) 

if __name__ == '__main__':
    main()
    main2()
