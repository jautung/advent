import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '21_dat.txt'
mapper = {}

STARTING_POSITION_1 = 9
STARTING_POSITION_2 = 10

# STARTING_POSITION_1 = 4
# STARTING_POSITION_2 = 8

class Die:
    det_die_num = 1
    roll_count = 0

    def __init__(self):
        return

    def roll_die(self):
        t = Die.det_die_num
        Die.det_die_num += 1
        Die.roll_count += 1
        return t

def main():
    # data = readlines(FILENAME)
    # data = [int(dat) for dat in data]

    # det_die_num = 1
    # def roll_die():
    #     t = det_die_num
    #     det_die_num += 1
    #     return t

    die = Die()

    pos1 = STARTING_POSITION_1
    pos2 = STARTING_POSITION_2
    sc1 = 0
    sc2 = 0
    while True:
        tot1 = die.roll_die() + die.roll_die() + die.roll_die()
        pos1 += tot1
        pos1 = correct_pos(pos1)
        sc1 += pos1

        if sc1 >= 1000 or sc2 >= 1000:
            # print(min(sc1,sc2))
            # print(die.roll_count)
            print(min(sc1,sc2)*die.roll_count)
            return

        tot2 = die.roll_die() + die.roll_die() + die.roll_die()
        pos2 += tot2
        pos2 = correct_pos(pos2)
        sc2 += pos2

        # print(tot1, pos1, sc1, tot2, pos2, sc2)

        if sc1 >= 1000 or sc2 >= 1000:
            # print(min(sc1,sc2))
            # print(die.roll_count)
            print(min(sc1,sc2)*die.roll_count)
            return

def correct_pos(pos):
    return ((pos-1)%10)+1

# TIME: 11:17

def main2():
    # data = readlines(FILENAME)
    # data = [int(dat) for dat in data]

    # det_die_num = 1
    # def roll_die():
    #     t = det_die_num
    #     det_die_num += 1
    #     return t

    triple_freq = one_triple()

    universes = []
    # each containing (pos1, pos2, sc1, sc2, p1_turn?, count) waiting to be simulated

    collapsed_1_wins = 0
    collapsed_2_wins = 0
    universes.append((STARTING_POSITION_1, STARTING_POSITION_2, 0, 0, True, 1))
    while len(universes) > 0:
        universe = universes.pop()
        for tot, freq in triple_freq.items():
            pos1, pos2, sc1, sc2, is_p1_turn, count = universe
            if is_p1_turn:
                pos1 += tot
                pos1 = correct_pos(pos1)
                sc1 += pos1
            else:
                pos2 += tot
                pos2 = correct_pos(pos2)
                sc2 += pos2
            if sc1 >= 21:
                collapsed_1_wins += freq * count
                continue
            elif sc2 >= 21:
                collapsed_2_wins += freq * count
                continue
            universes.append((pos1, pos2, sc1, sc2, not is_p1_turn, freq * count))
    # for universe in universes:
    #     print(universe)
    print(collapsed_1_wins, collapsed_2_wins, max(collapsed_1_wins, collapsed_2_wins))

# TIME: 32:10

def one_triple():
    scores = def_dict(0)
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                scores[i+j+k] += 1
    return scores

if __name__ == '__main__':
    main()
    main2()
