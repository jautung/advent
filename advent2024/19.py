import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '19_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data[0])
    # print(data[1])
    towels = [x.strip() for x in data[0][0].split(',')]
    # towels = sorted(towels, key=lambda x: len(x), reverse=True) # maybe this is faster?
    # print(max([len(k) for k in towels]))
    # max_towel_len = max([len(k) for k in towels])
    # exit(1)
    # print(towels)
    designs = data[1]
    # print(designs)
    # print(towels)
    # definitely_cannot_sequences = set() # of length max_towel_len

    # maybe simple backtracking?
    # def can_do_design(design):
    #     arranged_towels = [] # stores LISTS of (index, towel), the bottom path is the one we are currently on
    #     position_to_start_next = 0
    #     while True:
    #         # print(arranged_towels)
    #         # position_to_start_next = sum([len(x[0][1]) for x in arranged_towels])
    #         if position_to_start_next == len(design):
    #             break
    #         # to_match = design[position_to_start_next:]
    #         short_circuit_check = design[position_to_start_next:position_to_start_next+max_towel_len]
    #         matches = []
    #         if short_circuit_check not in definitely_cannot_sequences:
    #             for i, towel in enumerate(towels):
    #                 if design[position_to_start_next:position_to_start_next+len(towel)] == towel:
    #                 # if to_match.startswith(towel):
    #                     # print('matched', to_match, towel, 'when already', arranged_towels, 'prefix', ''.join([x[0][1] for x in arranged_towels]))
    #                     matches.append((i, towel))
    #         # print('no?', matches)
    #         if len(matches) > 0:
    #             # just progress with the first one
    #             arranged_towels.append(matches)
    #             position_to_start_next += len(matches[0][1])
    #             continue
    #         print(position_to_start_next, max_towel_len, len(design))
    #         if position_to_start_next+max_towel_len <= len(design):
    #             definitely_cannot_sequences.add(short_circuit_check)
    #             print('XXX', short_circuit_check)
    #         # need to backtrack here                
    #         # last_matches = arranged_towels[-1]
    #         # definitely_removed_len = last_matches[0]
    #         # last_matches = last_matches[1:]
    #         steps = 1
    #         found = False
    #         while steps <= len(arranged_towels):
    #             last_maybe_fork = arranged_towels[-steps]
    #             # print('last_maybe_fork', last_maybe_fork)
    #             position_to_start_next -= len(last_maybe_fork[0][1])
    #             if len(last_maybe_fork) > 1:
    #                 found = True
    #                 break
    #             steps += 1
    #         if not found:
    #             # print('huh')
    #             return False
    #         # print('1last_maybe_fork', last_maybe_fork, 'arranged_towels', arranged_towels, steps)
    #         arranged_towels = arranged_towels[:len(arranged_towels)-(steps-1)]
    #         # print('2last_maybe_fork', last_maybe_fork, 'arranged_towels', arranged_towels, steps)
    #         assert len(arranged_towels) > 0
    #         arranged_towels[-1] = last_maybe_fork[1:]
    #         position_to_start_next += len(arranged_towels[-1][0][1])
    #         # print('backed!', len(arranged_towels), arranged_towels)
    #         print('prefix', ''.join([x[0][1] for x in arranged_towels]))

    #     assert position_to_start_next == len(design)
    #     # print(arranged_towels)
    #     return True

    # I am a derp and did not cache, and also this is an easy recursion...
    cached_answers = dict()
    for towel in towels:
        cached_answers[towel] = True
    def can_do_design(design):
        # if len(design) == 0:
        #     return True
        # print('start', design)
        if design in cached_answers:
            # print('retrieving stored', design)
            return cached_answers[design]
        for towel in towels:
            if design.startswith(towel):
                # print(towel, design[len(towel):])
                if can_do_design(design[len(towel):]):
                    # print('storing true', design)
                    cached_answers[design] = True
                    return True
        # print('storing false', design)
        cached_answers[design] = False
        return False

    c = 0
    for d in designs:
        # print(d, can_do_design(d))
        if can_do_design(d):
            # print(d, 'can')
            c += 1
        # else:
            # print(d, 'cannot')
    # print(cached_answers)
    # print(can_do_design('brwrr'))
    # # print(can_do_design('bbrgwb'))
    print(c)



def main2():
    data = readlines_split_by_newlines(FILENAME)
    towels = [x.strip() for x in data[0][0].split(',')]
    designs = data[1]

    cached_answers = dict()
    cached_answers[''] = 1
    def ways_to_do(design):
        # print('start', design)
        if design in cached_answers:
            # print('retrieving stored', design)
            return cached_answers[design]
        counter = 0
        for towel in towels:
            if design.startswith(towel):
                # print(towel, design[len(towel):])
                next_ways = ways_to_do(design[len(towel):])
                counter += next_ways
        # print('storing false', design)
        cached_answers[design] = counter
        return counter

    c = 0
    for d in designs:
        # print(d, ways_to_do(d))
        # if ways_to_do(d):
        #     # print(d, 'can')
        #     c += 1
        # else:
            # print(d, 'cannot')
        c += ways_to_do(d)
    # print(cached_answers)
    # print(ways_to_do('brwrr'))
    # # print(ways_to_do('bbrgwb'))
    print(c)


if __name__ == '__main__':
    main()
    main2()
