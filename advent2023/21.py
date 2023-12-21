import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '21_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print_2d(data)
    N_ROWS = len(data)
    N_COLS = len(data[0])
    def find_s():
        for row in range(N_ROWS):
            for col in range(N_COLS):
                if data[row][col] == 'S':
                    return (row, col)
    def can_move_to(row, col):
        if row < 0 or col < 0 or row >= N_ROWS or col >= N_COLS:
            return False
        return data[row][col] == '.' or data[row][col] == 'S'
    POS_OF_S = find_s()
    
    # print(POS_OF_S)
    MAX_STEPS = 64
    EXACT_STEPS = 64
    # apply bfs
    current_queue = []
    # (<pos>, <current dist>, parity)
    current_queue.append((POS_OF_S, 0, True))
    once_in_queue = set()
    once_in_queue.add(POS_OF_S)
    counter = 0
    while len(current_queue) > 0:
        current_node = current_queue.pop(0)
        current_pos, current_length, current_parity = current_node
        if EXACT_STEPS % 2 == 0:
            if current_parity:
                counter += 1
        else:
            if not current_parity:
                counter += 1
        if current_length == MAX_STEPS:
            continue
        possible_neighbors = [
            (current_pos[0]-1, current_pos[1]),
            (current_pos[0]+1, current_pos[1]),
            (current_pos[0], current_pos[1]-1),
            (current_pos[0], current_pos[1]+1),
        ]
        valid_neighbors = [n for n in possible_neighbors if can_move_to(n[0], n[1])]
        valid_neighbors_to_explore = [n for n in valid_neighbors if n not in once_in_queue]
        for n in valid_neighbors_to_explore:
            current_queue.append((n, current_length + 1, not current_parity))
            once_in_queue.add(n)
    # print(once_in_queue)    
    print(counter)

def main2():
    # data = readlines(FILENAME)
    # data = [[c for c in dat] for dat in data]
    # # print_2d(data)
    # N_ROWS = len(data)
    # N_COLS = len(data[0])
    # def find_s():
    #     for row in range(N_ROWS):
    #         for col in range(N_COLS):
    #             if data[row][col] == 'S':
    #                 return (row, col)
    # def can_move_to(row, col):
    #     normalized_row = ((row % N_ROWS) + N_ROWS) % N_ROWS
    #     normalized_col = ((col % N_COLS) + N_COLS) % N_COLS
    #     return data[normalized_row][normalized_col] == '.' or data[normalized_row][normalized_col] == 'S'
    # POS_OF_S = find_s()
    
    # # print(POS_OF_S)
    # MAX_STEPS = 500
    # EXACT_STEPS = 500
    # # apply bfs
    # current_queue = []
    # # (<pos>, <current dist>, parity)
    # current_queue.append((POS_OF_S, 0, True))
    # once_in_queue = set()
    # once_in_queue.add(POS_OF_S)
    # counter = 0
    # while len(current_queue) > 0:
    #     current_node = current_queue.pop(0)
    #     current_pos, current_length, current_parity = current_node
    #     if EXACT_STEPS % 2 == 0:
    #         if current_parity:
    #             counter += 1
    #     else:
    #         if not current_parity:
    #             counter += 1
    #     if current_length == MAX_STEPS:
    #         continue
    #     possible_neighbors = [
    #         (current_pos[0]-1, current_pos[1]),
    #         (current_pos[0]+1, current_pos[1]),
    #         (current_pos[0], current_pos[1]-1),
    #         (current_pos[0], current_pos[1]+1),
    #     ]
    #     valid_neighbors = [n for n in possible_neighbors if can_move_to(n[0], n[1])]
    #     valid_neighbors_to_explore = [n for n in valid_neighbors if n not in once_in_queue]
    #     for n in valid_neighbors_to_explore:
    #         current_queue.append((n, current_length + 1, not current_parity))
    #         once_in_queue.add(n)
    # # print(once_in_queue)    
    # print(counter)

    # need to get the number of copies of board FULLY covered, then search the edges?
    # OH. the border is all dots. so i can really leverage that, huh
    # quickest path is probably jam the border and fly out
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print_2d(data)
    N_ROWS = len(data)
    N_COLS = len(data[0])
    def find_s():
        for row in range(N_ROWS):
            for col in range(N_COLS):
                if data[row][col] == 'S':
                    return (row, col)
    POS_OF_S = find_s()
    
    def can_move_to(row, col):
        if row < 0 or col < 0 or row >= N_ROWS or col >= N_COLS:
            return False
        return data[row][col] == '.' or data[row][col] == 'S'
    # let's assert my observation
    assert(all([can_move_to(r, 0) for r in range(N_ROWS)]))
    assert(all([can_move_to(r, N_COLS-1) for r in range(N_ROWS)]))
    assert(all([can_move_to(0, c) for c in range(N_COLS)]))
    assert(all([can_move_to(N_ROWS-1, c) for c in range(N_COLS)]))
    
    def n_dots_in_board():
        ret = 0
        for row in range(N_ROWS):
            for col in range(N_COLS):
                if can_move_to(row, col):
                    ret += 1
        return ret
    
    cache_of_mini_search = dict()
    def search_mini_map(start_at, moves_left):
        if (start_at, moves_left) in cache_of_mini_search:
            return cache_of_mini_search[(start_at, moves_left)]
        if moves_left <= 0:
            return set()
        # apply bfs
        current_queue = []
        # (<pos>, <current dist>, parity)
        current_queue.append((start_at, 0, True))
        once_in_queue = set()
        once_in_queue.add(start_at)
        ret_set = set()
        while len(current_queue) > 0:
            current_node = current_queue.pop(0)
            current_pos, current_length, current_parity = current_node
            if moves_left % 2 == 0:
                if current_parity:
                    ret_set.add(current_pos)
            else:
                if not current_parity:
                    ret_set.add(current_pos)
            if current_length == moves_left:
                continue
            possible_neighbors = [
                (current_pos[0]-1, current_pos[1]),
                (current_pos[0]+1, current_pos[1]),
                (current_pos[0], current_pos[1]-1),
                (current_pos[0], current_pos[1]+1),
            ]
            valid_neighbors = [n for n in possible_neighbors if can_move_to(n[0], n[1])]
            valid_neighbors_to_explore = [n for n in valid_neighbors if n not in once_in_queue]
            for n in valid_neighbors_to_explore:
                current_queue.append((n, current_length + 1, not current_parity))
                once_in_queue.add(n)
        # print(once_in_queue)
        cache_of_mini_search[(start_at, moves_left)] = ret_set
        return ret_set
    # print(len(search_mini_map(POS_OF_S, 64))) # sanity check same as original answer
    
    # just for the first mini map
    shortest_path_to_each_corner = dict()
    # apply bfs
    current_queue = []
    # (<pos>, <current dist>, parity)
    current_queue.append((POS_OF_S, 0, True))
    once_in_queue = set()
    once_in_queue.add(POS_OF_S)
    while len(current_queue) > 0:
        current_node = current_queue.pop(0)
        current_pos, current_length, current_parity = current_node
        if current_pos == (0,0):
            shortest_path_to_each_corner['TL'] = current_length
        elif current_pos == (0,N_COLS-1):
            shortest_path_to_each_corner['TR'] = current_length
        elif current_pos == (N_ROWS-1,0):
            shortest_path_to_each_corner['BL'] = current_length
        elif current_pos == (N_ROWS-1,N_COLS-1):
            shortest_path_to_each_corner['BR'] = current_length
        possible_neighbors = [
            (current_pos[0]-1, current_pos[1]),
            (current_pos[0]+1, current_pos[1]),
            (current_pos[0], current_pos[1]-1),
            (current_pos[0], current_pos[1]+1),
        ]
        valid_neighbors = [n for n in possible_neighbors if can_move_to(n[0], n[1])]
        valid_neighbors_to_explore = [n for n in valid_neighbors if n not in once_in_queue]
        for n in valid_neighbors_to_explore:
            current_queue.append((n, current_length + 1, not current_parity))
            once_in_queue.add(n)
    # print(once_in_queue)
    # print(shortest_path_to_each_corner)

    # need to store metadata like remaining steps and starting point as well but ugh
    boundary_map_coords = dict()
    def add_to_boundary_map_coords(k, v):
        if k in boundary_map_coords:
            boundary_map_coords[k].add(v)
        else:
            boundary_map_coords[k] = set()
            boundary_map_coords[k].add(v)
    # even this needs parity too, let's approximate for now TODO
    counter_for_full_maps = dict()
    counter_for_full_maps['X'] = 0
    
    # main two axes need to be special handled and we assume they are the same?!??!!
    max_row_for_0 = dict()
    max_row_for_0[-1] = []
    max_row_for_0[1] = []
    max_col_for_0 = dict()
    max_col_for_0[-1] = []
    max_col_for_0[1] = []

    # GLOBAL_N_STEPS = 5000
    GLOBAL_N_STEPS = 26501365
    # let's now work in terms of macro map coordinates
    # first minimap is (0,0)
    # we can travel to other coordinated maps
    # 1 in each quadrant?
    # from TL get to other TLs all the way
    # then initiate from the BRs of all the partials
    def do_quadrant(quadrant):
        def get_last_complete_map_row_and_remaining_steps(map_col):
            if quadrant == 'TL' or quadrant == 'BL':
                assert(map_col <= 0)
            if quadrant == 'TR' or quadrant == 'BR':
                assert(map_col >= 0)
            to_first_corner = shortest_path_to_each_corner[quadrant]
            used_for_fixed = abs(map_col) * N_COLS
            if GLOBAL_N_STEPS - to_first_corner - used_for_fixed > 0:
                return ((GLOBAL_N_STEPS - to_first_corner - used_for_fixed) // N_ROWS, (GLOBAL_N_STEPS - to_first_corner - used_for_fixed) % N_ROWS)
            return None

        def swap_row(quadrant):
            if quadrant[0] == 'T':
                return 'B' + quadrant[1]
            elif quadrant[0] == 'B':
                return 'T' + quadrant[1]
            else:
                assert(False)
        def swap_col(quadrant):
            if quadrant[1] == 'L':
                return quadrant[0] + 'R'
            elif quadrant[1] == 'R':
                return quadrant[0] + 'L'
            else:
                assert(False)

        map_col = 0
        if quadrant == 'TL' or quadrant == 'BL':
            step_map_col = -1
        if quadrant == 'TR' or quadrant == 'BR':
            step_map_col = 1
        if quadrant == 'TL' or quadrant == 'TR':
            step_map_row = -1
        if quadrant == 'BL' or quadrant == 'BR':
            step_map_row = 1
        while True:
            map_row_and_remaining_steps = get_last_complete_map_row_and_remaining_steps(map_col)
            if map_row_and_remaining_steps == None:
                max_col_for_0[step_map_col].append(abs(map_col - step_map_col))
                break
            if map_col != 0:
                counter_for_full_maps['X'] += map_row_and_remaining_steps[0]
            else:
                max_row_for_0[step_map_row].append(map_row_and_remaining_steps[0])
            map_row = map_row_and_remaining_steps[0] * step_map_row
            # print(counter_for_full_maps['X'], map_row)
            remaining_steps = map_row_and_remaining_steps[1]
            # print(map_row, map_col, remaining_steps)
            add_to_boundary_map_coords((map_row+step_map_row, map_col), (swap_row(quadrant), remaining_steps-1))
            add_to_boundary_map_coords((map_row, map_col+step_map_col), (swap_col(quadrant), remaining_steps-1))
            add_to_boundary_map_coords((map_row+step_map_row, map_col+step_map_col), (swap_row(swap_col(quadrant)), remaining_steps-2))
            map_col += step_map_col
    
    # do_quadrant('TL')
    [do_quadrant(quadrant) for quadrant in ['TL', 'TR', 'BL', 'BR']]
    
    # for k in boundary_map_coords:
    #     print(k, boundary_map_coords[k])
    # print(counter_for_full_maps['X'])
    # these are 4 so large assumptions tbh
    # but the obstacles are sparse enough that this is fineeeeeee. i don't like needing so much domain knowledge...
    assert(max_col_for_0[-1][0] == max_col_for_0[-1][1])
    assert(max_col_for_0[1][0] == max_col_for_0[1][1])
    assert(max_row_for_0[-1][0] == max_row_for_0[-1][1])
    assert(max_row_for_0[1][0] == max_row_for_0[1][1])
    # print(max_col_for_0[-1][0])
    # print(max_col_for_0[1][0])
    # print(max_row_for_0[-1][0])
    # print(max_row_for_0[1][0])
    axes_power = max_col_for_0[-1][0] + max_col_for_0[1][0] + max_row_for_0[-1][0] + max_row_for_0[1][0] + 1 # the 1 is the (0,0)
    # print(axes_power + counter_for_full_maps['X'])
    full_boards = axes_power + counter_for_full_maps['X']
    # approximation
    # ok the order of magnitude is correct at least...... grahhhhh
    # print(full_boards * n_dots_in_board() // 2)
    dots_from_full_boards = full_boards * n_dots_in_board() // 2
    print('dots_from_full_boards', dots_from_full_boards)
    # and need to add the edges
    dots_from_edge_boards = 0
    for k in boundary_map_coords:
        # print(k, boundary_map_coords[k])
        for_this_one = set()
        for aa in boundary_map_coords[k]:
            quadrant, moves_left = aa
            if quadrant == 'TL':
                start_at = (0,0)
            elif quadrant == 'BL':
                start_at = (N_ROWS-1,0)
            elif quadrant == 'TR':
                start_at = (0,N_COLS-1)
            elif quadrant == 'BR':
                start_at = (N_ROWS-1,N_COLS-1)
            else:
                assert(False)
            search = search_mini_map(start_at, moves_left)
            for_this_one = for_this_one.union(search)
        # print(len(for_this_one))
        dots_from_edge_boards += len(for_this_one)
    print('dots_from_edge_boards', dots_from_edge_boards)
    print('total approx', dots_from_full_boards + dots_from_edge_boards)

if __name__ == '__main__':
    main()
    main2()
