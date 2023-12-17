import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '16_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    start_beam = ((0, 0), 'R')
    energized = trace_beam(start_beam, data)
    # print(energized)
    # print(data)
    # print(len(energized))
    print(len(set([c[0] for c in energized])))
    
def trace_beam(beam, map):
    running = set()
    trace_beam_iter(running, beam, map)
    return running

def trace_beam_iter(running, beam, map):
    # print(beam)
    new_beams = step_beam_iter(running, beam, map)
    return [trace_beam_iter(running, new_beam, map) for new_beam in new_beams]

def step_beam_iter(running, beam, map):
    if beam in running:
        return [] # already running
    row, col = beam[0]
    if row < 0 or col < 0 or row >= len(map) or col >= len(map[0]):
        # print("EXITED")
        # and don't append
        return []
    elem = map[row][col]
    d = beam[1]
    running.add(beam)
    if elem == '.':
        next_d = d
        if beam[1] == 'L':
            next_row = row
            next_col = col - 1
        elif beam[1] == 'R':
            next_row = row
            next_col = col + 1
        elif beam[1] == 'U':
            next_row = row - 1
            next_col = col
        elif beam[1] == 'D':
            next_row = row + 1
            next_col = col
        else:
            assert(False)
    elif elem == '/':
        if beam[1] == 'L':
            next_row = row + 1
            next_col = col
            next_d = 'D'
        elif beam[1] == 'R':
            next_row = row - 1
            next_col = col
            next_d = 'U'
        elif beam[1] == 'U':
            next_row = row
            next_col = col + 1
            next_d = 'R'
        elif beam[1] == 'D':
            next_row = row
            next_col = col - 1
            next_d = 'L'
        else:
            assert(False)
    elif elem == '\\':
        if beam[1] == 'L':
            next_row = row - 1
            next_col = col
            next_d = 'U'
        elif beam[1] == 'R':
            next_row = row + 1
            next_col = col
            next_d = 'D'
        elif beam[1] == 'U':
            next_row = row
            next_col = col - 1
            next_d = 'L'
        elif beam[1] == 'D':
            next_row = row
            next_col = col + 1
            next_d = 'R'
        else:
            assert(False)
    elif elem == '-':
        next_d = d
        if beam[1] == 'L':
            next_row = row
            next_col = col - 1
        elif beam[1] == 'R':
            next_row = row
            next_col = col + 1
        elif beam[1] == 'U' or beam[1] == 'D':
            next_row_1 = row
            next_col_1 = col + 1
            next_d_1 = 'R'
            next_row_2 = row
            next_col_2 = col - 1
            next_d_2 = 'L'
            return [((next_row_1, next_col_1), next_d_1), ((next_row_2, next_col_2), next_d_2)]
        else:
            assert(False)
    elif elem == '|':
        next_d = d
        if beam[1] == 'L' or beam[1] == 'R':
            next_row_1 = row + 1
            next_col_1 = col
            next_d_1 = 'D'
            next_row_2 = row - 1
            next_col_2 = col
            next_d_2 = 'U'
            return [((next_row_1, next_col_1), next_d_1), ((next_row_2, next_col_2), next_d_2)]
        elif beam[1] == 'U':
            next_row = row - 1
            next_col = col
        elif beam[1] == 'D':
            next_row = row + 1
            next_col = col
        else:
            assert(False)
    else:
        assert(False)
    return [((next_row, next_col), next_d)]

def main2():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    all_poss = []
    for row in range(len(data)):
        all_poss.append(get_energize_val(((row, len(data[0])-1), 'L'), data))
        all_poss.append(get_energize_val(((row, 0), 'R'), data))
    for col in range(len(data[0])):
        all_poss.append(get_energize_val(((len(data)-1, col), 'U'), data))
        all_poss.append(get_energize_val(((0, col), 'D'), data))
    print(max(all_poss))
    # print(get_energize_val(((0, 0), 'R'), data))
    # energized = trace_beam(start_beam, data)
    # # print(energized)
    # # print(data)
    # # print(len(energized))
    # print(len(set([c[0] for c in energized])))

def get_energize_val(start_beam, data):
    energized = trace_beam(start_beam, data)
    # print(energized)
    # print(data)
    # print(len(energized))
    return len(set([c[0] for c in energized]))

if __name__ == '__main__':
    sys.setrecursionlimit(99999)
    main()
    main2()
