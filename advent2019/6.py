import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '6_dat.txt'
mapper = {}

def parse(line):
    items = line.split(')')
    assert len(items) == 2
    return items[0], items[1]

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]

    all_planets = set()
    orbits = dict()
    for left, right in data:
        if left in orbits:
            orbits[left].append(right)
        else:
            orbits[left] = [right]
        all_planets.add(left)
        all_planets.add(right)

    planets_to_the_right = dict() # excludes self, maps each planet to a set of planets to the right
    for planet in all_planets:
        get_planets_ttr(planet, orbits, planets_to_the_right)
    # print(planets_to_the_right)

    count = 0
    for _, v in planets_to_the_right.items():
        count += len(v)
    print(count)

def get_planets_ttr(planet, orbits, planets_to_the_right):
    if planet in planets_to_the_right:
        return planets_to_the_right[planet]
    if planet not in orbits:
        return set()
    full_set = set()
    for next_planet in orbits[planet]:
        down_set = get_planets_ttr(next_planet, orbits, planets_to_the_right)
        full_set.add(next_planet)
        full_set = full_set.union(down_set)
    planets_to_the_right[planet] = full_set
    return planets_to_the_right[planet]


def main2():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]

    all_planets = set()
    orbits = dict()
    for left, right in data:
        if left in orbits:
            orbits[left].append(right)
        else:
            orbits[left] = [right]
        all_planets.add(left)
        all_planets.add(right)

    planets_to_the_right = dict() # excludes self, maps each planet to a set of planets to the right
    for planet in all_planets:
        get_planets_ttr(planet, orbits, planets_to_the_right)
    # print(planets_to_the_right)

    cache = dict()
    min_dist = None
    for candidate, downstream_planets in planets_to_the_right.items():
        if 'YOU' in downstream_planets and 'SAN' in downstream_planets:
            dist_1 = path_distance(candidate, 'YOU', orbits, cache)
            dist_2 = path_distance(candidate, 'SAN', orbits, cache)
            if dist_1 is None or dist_2 is None:
                assert False
            candidate_distance = dist_1 + dist_2
            if min_dist is None or candidate_distance < min_dist:
                min_dist = candidate_distance
    # print(cache)
    print(min_dist - 2)

def path_distance(from_p, to_p, orbits, cache):
    if (from_p, to_p) in cache:
        return cache[(from_p, to_p)]
    if from_p == to_p:
        cache[(from_p, to_p)] = 0
        return cache[(from_p, to_p)]
    if from_p not in orbits:
        cache[(from_p, to_p)] = None
        return cache[(from_p, to_p)]
    all_next = None
    for next_cand in orbits[from_p]:
        result_that = path_distance(next_cand, to_p, orbits, cache)
        if result_that is None:
            continue
        if all_next is None or result_that < all_next:
            all_next = result_that
    if all_next is None:
        cache[(from_p, to_p)] = None
        return cache[(from_p, to_p)]
    cache[(from_p, to_p)] = all_next + 1
    return cache[(from_p, to_p)]

if __name__ == '__main__':
    main()
    main2()
