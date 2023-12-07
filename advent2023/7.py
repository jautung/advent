from collections import Counter
import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    data.sort(key=power)
    ret = 0
    for i, d in enumerate(data):
        # print(i+1, d)
        ret += ((i+1) * d[3])
    print(ret)

def power(dat):
    raw, hand, hand_type, bid = dat
    return (15**5) * (7-hand_type) + \
        (15**4) * val(raw[0]) + \
        (15**3) * val(raw[1]) + \
        (15**2) * val(raw[2]) + \
        (15**1) * val(raw[3]) + \
        (15**0) * val(raw[4])

def val(c):
    return 12 - ORDERING.index(c)

def parse(dat):
    a = dat.split()
    raw = [c for c in a[0]]
    hand = Counter(raw)
    hand_type = classify(hand)
    bid = int(a[1])
    return raw, hand, hand_type, bid

FIVE_OAK = 1
FOUR_OAK = 2
FULL_HOUSE = 3
THREE_OAK = 4
TWO_PAIR = 5
ONE_PAIR = 6
HIGH = 7

ORDERING = 'AKQJT98765432'

def classify(hand: Counter):
    kv = []
    for k in hand.keys():
        kv.append((k, hand[k]))
    vs = [x[1] for x in kv]
    max_n = max(vs)
    if max_n == 5:
        return FIVE_OAK
    if max_n == 4:
        return FOUR_OAK
    if max_n == 3:
        if 2 in vs:
            return FULL_HOUSE
        else:
            return THREE_OAK
    if max_n == 2:
        if len(vs) == 3:
            return TWO_PAIR
        else:
            return ONE_PAIR
    return HIGH

def main2():
    data = readlines(FILENAME)
    data = [parse_2(dat) for dat in data]
    data.sort(key=power_2)
    # for dat in data:
    #     print(''.join(dat[0]), dat[2])
    ret = 0
    for i, d in enumerate(data):
        # print(i+1, d)
        ret += ((i+1) * d[3])
    print(ret)

ORDERING_2 = 'AKQT98765432J'

def power_2(dat):
    raw, hand, hand_type, bid = dat
    return (15**5) * (7-hand_type) + \
        (15**4) * val_2(raw[0]) + \
        (15**3) * val_2(raw[1]) + \
        (15**2) * val_2(raw[2]) + \
        (15**1) * val_2(raw[3]) + \
        (15**0) * val_2(raw[4])

def val_2(c):
    return 12 - ORDERING_2.index(c)

def parse_2(dat):
    a = dat.split()
    raw = [c for c in a[0]]
    hand = Counter(raw)
    hand_type = classify_2(hand)
    bid = int(a[1])
    return raw, hand, hand_type, bid

def classify_2(hand: Counter):
    kv = []
    for k in hand.keys():
        if k == 'J':
            continue
        kv.append((k, hand[k]))
    vs = [x[1] for x in kv]
    jokers = hand.get('J', 0)
    # print(vs, jokers)
    if jokers == 5:
        return FIVE_OAK
    possible_augmented_vs = [vs]
    
    def incr_by_1(possible_augmented_vs):
        ret = []
        for vs in possible_augmented_vs:
            for i in range(len(vs)):
                curr_copy = copy.deepcopy(vs)
                curr_copy[i] += 1
                ret.append(curr_copy)
        return ret
        
    for j in range(jokers):
        possible_augmented_vs = incr_by_1(possible_augmented_vs)
    
    def from_vs(vs):
        max_n = max(vs)
        if max_n == 5:
            return FIVE_OAK
        if max_n == 4:
            return FOUR_OAK
        if max_n == 3:
            if 2 in vs:
                return FULL_HOUSE
            else:
                return THREE_OAK
        if max_n == 2:
            if len(vs) == 3:
                return TWO_PAIR
            else:
                return ONE_PAIR
        return HIGH

    return min([from_vs(vs) for vs in possible_augmented_vs])
    # print('a', possible_augmented_vs)
    # max_n = max(vs)
    # augmented_vs = []
    # first_time = True
    # for a in vs:
    #     if a == max_n and first_time:
    #         augmented_vs.append(a + jokers)
    #         first_time = False
    #     else:
    #         augmented_vs.append(a)
    # # print(augmented_vs)
    # max_n_with_jokers = max(augmented_vs)
    # if max_n_with_jokers == 5:
    #     return FIVE_OAK
    # if max_n_with_jokers == 4:
    #     return FOUR_OAK
    # if max_n_with_jokers == 3:
    #     if 2 in augmented_vs:
    #         return FULL_HOUSE
    #     else:
    #         return THREE_OAK
    # if max_n_with_jokers == 2:
    #     if len(augmented_vs) == 3:
    #         return TWO_PAIR
    #     else:
    #         return ONE_PAIR
    # return HIGH

if __name__ == '__main__':
    main()
    main2()
