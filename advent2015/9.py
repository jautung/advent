import sys 
sys.path.append('..')

import copy
import itertools
from collections import defaultdict
from helper import *

FILENAME = '9_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)

    all_cities = set()
    dists = dict()
    def parse(dat):
        all_cities.add(dat[0])
        all_cities.add(dat[2])
        dists[frozenset([dat[0], dat[2]])] = int(dat[-1])

    [parse(dat) for dat in data]
    
    # print_2d(data)
    # print(all_cities)

    min_seen = None
    max_seen = None
    for order in itertools.permutations(list(all_cities)):
        # print(order)
        trip = sum([dists[frozenset(order[i:i+2])] for i in range(len(order) - 1)])
        # print(trip)
        if min_seen == None or trip < min_seen:
            min_seen = trip
        if max_seen == None or trip > max_seen:
            max_seen = trip
    print(min_seen)
    print(max_seen)

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
