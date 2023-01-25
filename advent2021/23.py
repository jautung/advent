import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '23_dat.txt'
MAPPER = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

# TARGET_POS = {
#     'Ao': 'A',
#     'Ai': 'A',
#     'Bo': 'B',
#     'Bi': 'B',
#     'Co': 'C',
#     'Ci': 'C',
#     'Do': 'D',
#     'Di': 'D',
#     'eA': None,
#     'cA': None,
#     'ab': None,
#     'bc': None,
#     'cd': None,
#     'eD': None,
#     'cD': None,
# }

DISTS = {
    frozenset(['Ao','eA']): 2,
    frozenset(['Ao','cA']): 3,
    frozenset(['Ao','ab']): 2,
    frozenset(['Ao','bc']): 4,
    frozenset(['Ao','cd']): 6,
    frozenset(['Ao','eD']): 8,
    frozenset(['Ao','cD']): 9,
    frozenset(['Ai','eA']): 2+1,
    frozenset(['Ai','cA']): 3+1,
    frozenset(['Ai','ab']): 2+1,
    frozenset(['Ai','bc']): 4+1,
    frozenset(['Ai','cd']): 6+1,
    frozenset(['Ai','eD']): 8+1,
    frozenset(['Ai','cD']): 9+1,
    frozenset(['Bo','eA']): 4,
    frozenset(['Bo','cA']): 5,
    frozenset(['Bo','ab']): 2,
    frozenset(['Bo','bc']): 2,
    frozenset(['Bo','cd']): 4,
    frozenset(['Bo','eD']): 6,
    frozenset(['Bo','cD']): 7,
    frozenset(['Bi','eA']): 4+1,
    frozenset(['Bi','cA']): 5+1,
    frozenset(['Bi','ab']): 2+1,
    frozenset(['Bi','bc']): 2+1,
    frozenset(['Bi','cd']): 4+1,
    frozenset(['Bi','eD']): 6+1,
    frozenset(['Bi','cD']): 7+1,
    frozenset(['Co','eA']): 6,
    frozenset(['Co','cA']): 7,
    frozenset(['Co','ab']): 4,
    frozenset(['Co','bc']): 2,
    frozenset(['Co','cd']): 2,
    frozenset(['Co','eD']): 4,
    frozenset(['Co','cD']): 5,
    frozenset(['Ci','eA']): 6+1,
    frozenset(['Ci','cA']): 7+1,
    frozenset(['Ci','ab']): 4+1,
    frozenset(['Ci','bc']): 2+1,
    frozenset(['Ci','cd']): 2+1,
    frozenset(['Ci','eD']): 4+1,
    frozenset(['Ci','cD']): 5+1,
    frozenset(['Do','eA']): 8,
    frozenset(['Do','cA']): 9,
    frozenset(['Do','ab']): 6,
    frozenset(['Do','bc']): 4,
    frozenset(['Do','cd']): 2,
    frozenset(['Do','eD']): 2,
    frozenset(['Do','cD']): 3,
    frozenset(['Di','eA']): 8+1,
    frozenset(['Di','cA']): 9+1,
    frozenset(['Di','ab']): 6+1,
    frozenset(['Di','bc']): 4+1,
    frozenset(['Di','cd']): 2+1,
    frozenset(['Di','eD']): 2+1,
    frozenset(['Di','cD']): 3+1,
}

BLOCKING = {
    frozenset(['Ao','cA']): ['eA'],
    frozenset(['Ao','eA']): [],
    frozenset(['Ao','ab']): [],
    frozenset(['Ao','bc']): ['ab'],
    frozenset(['Ao','cd']): ['ab', 'bc'],
    frozenset(['Ao','eD']): ['ab', 'bc', 'cd'],
    frozenset(['Ao','cD']): ['ab', 'bc', 'cd', 'eD'],
    frozenset(['Ai','cA']): ['Ao', 'eA'],
    frozenset(['Ai','eA']): ['Ao'],
    frozenset(['Ai','ab']): ['Ao'],
    frozenset(['Ai','bc']): ['Ao', 'ab'],
    frozenset(['Ai','cd']): ['Ao', 'ab', 'bc'],
    frozenset(['Ai','eD']): ['Ao', 'ab', 'bc', 'cd'],
    frozenset(['Ai','cD']): ['Ao', 'ab', 'bc', 'cd', 'eD'],
    frozenset(['Bo','cA']): ['ab', 'eA'],
    frozenset(['Bo','eA']): ['ab'],
    frozenset(['Bo','ab']): [],
    frozenset(['Bo','bc']): [],
    frozenset(['Bo','cd']): ['bc'],
    frozenset(['Bo','eD']): ['bc', 'cd'],
    frozenset(['Bo','cD']): ['bc', 'cd', 'eD'],
    frozenset(['Bi','cA']): ['Bo', 'ab', 'eA'],
    frozenset(['Bi','eA']): ['Bo', 'ab'],
    frozenset(['Bi','ab']): ['Bo'],
    frozenset(['Bi','bc']): ['Bo'],
    frozenset(['Bi','cd']): ['Bo', 'bc'],
    frozenset(['Bi','eD']): ['Bo', 'bc', 'cd'],
    frozenset(['Bi','cD']): ['Bo', 'bc', 'cd', 'eD'],
    frozenset(['Co','cA']): ['bc', 'ab', 'eA'],
    frozenset(['Co','eA']): ['bc', 'ab'],
    frozenset(['Co','ab']): ['bc'],
    frozenset(['Co','bc']): [],
    frozenset(['Co','cd']): [],
    frozenset(['Co','eD']): ['cd'],
    frozenset(['Co','cD']): ['cd', 'eD'],
    frozenset(['Ci','cA']): ['Co', 'bc', 'ab', 'eA'],
    frozenset(['Ci','eA']): ['Co', 'bc', 'ab'],
    frozenset(['Ci','ab']): ['Co', 'bc'],
    frozenset(['Ci','bc']): ['Co'],
    frozenset(['Ci','cd']): ['Co'],
    frozenset(['Ci','eD']): ['Co', 'cd'],
    frozenset(['Ci','cD']): ['Co', 'cd', 'eD'],
    frozenset(['Do','cA']): ['cd', 'bc', 'ab', 'eA'],
    frozenset(['Do','eA']): ['cd', 'bc', 'ab'],
    frozenset(['Do','ab']): ['cd', 'bc'],
    frozenset(['Do','bc']): ['cd'],
    frozenset(['Do','cd']): [],
    frozenset(['Do','eD']): [],
    frozenset(['Do','cD']): ['eD'],
    frozenset(['Di','cA']): ['Do', 'cd', 'bc', 'ab', 'eA'],
    frozenset(['Di','eA']): ['Do', 'cd', 'bc', 'ab'],
    frozenset(['Di','ab']): ['Do', 'cd', 'bc'],
    frozenset(['Di','bc']): ['Do', 'cd'],
    frozenset(['Di','cd']): ['Do'],
    frozenset(['Di','eD']): ['Do'],
    frozenset(['Di','cD']): ['Do', 'eD'],
}

def main():
    # toy data
    # pos = {
    #     'Ao': 'B1',
    #     'Ai': 'A1',
    #     'Bo': 'C1',
    #     'Bi': 'D1',
    #     'Co': 'B2',
    #     'Ci': 'C2',
    #     'Do': 'D2',
    #     'Di': 'A2',
    #     'eA': None,
    #     'cA': None,
    #     'ab': None,
    #     'bc': None,
    #     'cd': None,
    #     'eD': None,
    #     'cD': None,
    # }
    # real data
    pos = {
        'Ao': 'D1',
        'Ai': 'C1',
        'Bo': 'A1',
        'Bi': 'A2',
        'Co': 'C2',
        'Ci': 'B1',
        'Do': 'D2',
        'Di': 'B2',
        'eA': None,
        'cA': None,
        'ab': None,
        'bc': None,
        'cd': None,
        'eD': None,
        'cD': None,
    }
    paths = [(pos, [], set(), set(), 0)] # current pos, current energy expended
    known_best = None
    # known_best = 14522
    step = 1
    while len(paths) > 0:
        # paths = sorted(paths, key=lambda x: x[4], reverse=True) # this heuristic explores the best branch first (i.e. the lowest_energy)
        curr_pos, move_log, moved_out, moved_back_in, curr_energy = paths.pop()
        if known_best and curr_energy >= known_best:
            continue
        nexts = possible_nexts(curr_pos, move_log, moved_out, moved_back_in)
        for new_pos, new_move_log, new_moved_out, new_moved_back_in, energy_expended in nexts:
            if hit_target(new_pos):
                curr_candidate = curr_energy + energy_expended
                if not known_best or curr_candidate < known_best:
                    known_best = curr_candidate
                    # print(known_best)
                    # print('got one', curr_energy + energy_expended)
                    print('COMPLETED in ', known_best, '; nodes left to search:', len(paths), '; step:', step)
                    # print(known_best)
                    print(new_move_log)
                    # print(new_moved_back_in)
                    # print(curr_energy + energy_expended)
                    # if curr_energy + energy_expended < 17100:
                    #     return
            else:
                paths.append((new_pos, new_move_log, new_moved_out, new_moved_back_in, curr_energy + energy_expended))
        # if step % 1000 == 0:
        #     print('ugh', step, len(paths))
        #     print(paths[-1][1])
        #     print(len(paths[-1][3]))
        #     print(paths[-1][4])
        # for i in paths:
        #     print(i)
        # print()
        # if step == 2:
        #     exit(1)
        step += 1
    print(known_best)

def hit_target(pos):
    for in_cave in ['Ao', 'Ai', 'Bo', 'Bi', 'Co', 'Ci', 'Do', 'Di']:
        if not pos[in_cave] or pos[in_cave][0] != in_cave[0]:
            return False
    return True

def possible_nexts(pos, move_log, moved_out, moved_back_in):
    res = []
    for in_cave in ['Ao', 'Ai', 'Bo', 'Bi', 'Co', 'Ci', 'Do', 'Di']:
        for out_cave in ['eA', 'cA', 'ab', 'bc', 'cd', 'eD', 'cD']:
            if len(move_log) > 0 and move_log[-1][1] == out_cave and move_log[-1][2] == in_cave: # please don't immediately undo what you did; that's dumb
                continue
            if pos[in_cave] and not pos[out_cave]:
                if in_cave[1] == 'i' and pos[in_cave][0] == in_cave[0]: # please don't leave home if you are already in inner home
                    continue
                if pos[in_cave] in moved_out and pos[in_cave] in moved_back_in: # cannot move again
                    continue
                blockers = BLOCKING[frozenset([in_cave, out_cave])]
                if sum([pos[blocker] != None for blocker in blockers]) == 0:
                    res.append(change_pos(pos, move_log, moved_out, moved_back_in, in_cave, out_cave, moving_out=True))
    for out_cave in ['eA', 'cA', 'ab', 'bc', 'cd', 'eD', 'cD']:
        for in_cave in ['Ao', 'Ai', 'Bo', 'Bi', 'Co', 'Ci', 'Do', 'Di']:
            if len(move_log) > 0 and move_log[-1][1] == in_cave and move_log[-1][2] == out_cave: # please don't immediately undo what you did; that's dumb
                continue
            if pos[out_cave] and not pos[in_cave]:
                if in_cave[1] == 'o' and not pos[in_cave[0] + 'i']: # why would you stay on the outside of the cave if there's no one inside
                    continue
                if pos[out_cave][0] != in_cave[0]: # must move to destination already
                    continue
                if in_cave[1] == 'o' and pos[in_cave[0] + 'i'] and pos[in_cave[0] + 'i'][0] != in_cave[0]: # other dude in the cave is not at home yet
                    continue
                blockers = BLOCKING[frozenset([out_cave, in_cave])]
                if sum([pos[blocker] != None for blocker in blockers]) == 0:
                    res.append(change_pos(pos, move_log, moved_out, moved_back_in, out_cave, in_cave, moving_out=False))
    return res

def change_pos(pos, move_log, moved_out, moved_back_in, from_loc, to_loc, moving_out):
    new_pos = copy.deepcopy(pos)
    new_move_log = copy.deepcopy(move_log)
    new_moved_out = copy.deepcopy(moved_out)
    new_moved_back_in = copy.deepcopy(moved_back_in)

    moving = new_pos[from_loc]

    new_pos[to_loc] = new_pos[from_loc]
    new_pos[from_loc] = None

    if moving_out:
        new_moved_out.add(moving)
    else:
        new_moved_back_in.add(moving)

    new_move_log.append((moving, from_loc, to_loc))

    return new_pos, new_move_log, new_moved_out, new_moved_back_in, MAPPER[moving[0]] * DISTS[frozenset([from_loc, to_loc])]

# holy cow this takes like 5 minutes to run, but i guess at least it completes now with 10,000 heuristics?
# the test data took 5 minutes to run though
# jk it has been 20 minutes
# lol i worked out the 14346 answer by hand faster than the thing took to run (probably took like 20 minutes to do by hand)
# Time: 2:44:23 rip me

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

# Time: good lord it's 1am and i've spent 3 hours on this imma peace out for now

if __name__ == '__main__':
    main()
    main2()
