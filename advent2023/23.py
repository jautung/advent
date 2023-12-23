import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '23_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print_2d(data)
    N_ROWS = len(data)
    N_COLS = len(data[0])
    START = None
    END = None
    for col in range(N_COLS):
        if data[0][col] == '.':
            assert(START == None)
            START = (0, col)
    for col in range(N_COLS):
        if data[N_ROWS-1][col] == '.':
            assert(END == None)
            END = (N_ROWS-1, col)
    # print(START)
    # print(END)

    # just dfs this?
    # no cannot we need to fully explore branches
    def can_step_on(coord):
        row, col = coord
        if row < 0 or col < 0 or row >= N_ROWS or col >= N_COLS:
            return False
        return data[row][col] != '#'

    def apply_all_forced_moves(coord):
        # print(coord)
        row, col = coord
        assert(data[row][col] != '#')
        collected_pos = set([coord])
        def iter(inner_coord):
            inner_row, inner_col = inner_coord
            if data[inner_row][inner_col] == '.':
                return inner_coord
            elif data[inner_row][inner_col] == '<':
                collected_pos.update([(inner_row, inner_col-1)])
                return iter((inner_row, inner_col-1))
            elif data[inner_row][inner_col] == '>':
                collected_pos.update([(inner_row, inner_col+1)])
                return iter((inner_row, inner_col+1))
            elif data[inner_row][inner_col] == 'v':
                collected_pos.update([(inner_row+1, inner_col)])
                return iter((inner_row+1, inner_col))
            elif data[inner_row][inner_col] == '^':
                collected_pos.update([(inner_row-1, inner_col)])
                return iter((inner_row-1, inner_col))
            elif data[inner_row][inner_col] == '#':
                assert(False)
            else:
                assert(False)
        final_pos = iter(coord)
        return final_pos, collected_pos

    branches = []
    branches.append((START, set([START])))
    hike_lengths = []
    while len(branches) > 0:
        current_branch = branches.pop()
        current_pos, current_history = current_branch
        # print(current_pos, len(branches))
        if current_pos == END:
            # print(f"END with {len(current_history)-1}")
            hike_lengths.append(len(current_history)-1)
        neighbors = [
            (current_pos[0]-1, current_pos[1]),
            (current_pos[0]+1, current_pos[1]),
            (current_pos[0], current_pos[1]-1),
            (current_pos[0], current_pos[1]+1),
        ]
        valid_neighbors = [n for n in neighbors if can_step_on(n) and n not in current_history]
        for valid_neighbor in valid_neighbors:
            final_pos, travelled_pos = apply_all_forced_moves(valid_neighbor)
            if len(travelled_pos.intersection(current_history)) > 0:
                continue # we went down a uno reverse LOL
            branches.append((final_pos, current_history.union(travelled_pos)))
    print(max(hike_lengths))

def main2():
    data = readlines(FILENAME)
    data = [[c for c in dat] for dat in data]
    # print_2d(data)
    N_ROWS = len(data)
    N_COLS = len(data[0])
    START = None
    END = None
    for col in range(N_COLS):
        if data[0][col] == '.':
            assert(START == None)
            START = (0, col)
    for col in range(N_COLS):
        if data[N_ROWS-1][col] == '.':
            assert(END == None)
            END = (N_ROWS-1, col)
    # print(START)
    # print(END)

    # just dfs this?
    # no cannot we need to fully explore branches
    def can_step_on(coord):
        row, col = coord
        if row < 0 or col < 0 or row >= N_ROWS or col >= N_COLS:
            return False
        return data[row][col] != '#'
    
    # the wasteful part is travelling the same mazes
    # assuming this is always a maze, we need to transform this into a graph with lengths
    # longest path graph but still more efficient at least
    # let's verify this first
    
    for row in range(N_ROWS-1):
        for col in range(N_COLS-1):
            if can_step_on((row, col)) and \
                can_step_on((row+1, col)) and \
                can_step_on((row, col+1)) and \
                can_step_on((row+1, col+1)):
                    assert(False)
    # as long as there are no squares, we can assert that there is always a uni-width path
    # cool this is true
    
    GLOB_ID = [0]
    def get_node_id():
        GLOB_ID[0] += 1
        return GLOB_ID[0]

    nodes = [] # just a list of node ids
    coordinates_to_nodes = dict() # from real life coordinate to node_id
    set_of_coordinates_with_nodes = set()
    edges = [] # tuples of (<node_id>, <node_id>, distance)
    
    def update_with_node(coord):
        idd = get_node_id()
        nodes.append(idd)
        coordinates_to_nodes[coord] = idd
        set_of_coordinates_with_nodes.add(coord)

    update_with_node(START)
    update_with_node(END)
    
    # so we do a preliminary dfs to explore all tiles and that should populate our meta graph?
    START_NEXT = (START[0]+1, START[1]) # the first step is always downwards by the setup
    queue = []
    queue.append((START, START_NEXT))
    seen = set([START])
    while len(queue) > 0:
        current_thing = queue.pop()
        node_anchor, current_pos = current_thing
        seen.add(current_pos)
        path_counter = 1 # we are already starting from the next
        while True:
            neighbors_and_dists = [
                (current_pos[0]-1, current_pos[1]),
                (current_pos[0]+1, current_pos[1]),
                (current_pos[0], current_pos[1]-1),
                (current_pos[0], current_pos[1]+1),
            ]
            for n in neighbors_and_dists:
                if n == END and n != node_anchor:
                    edges.append((coordinates_to_nodes[node_anchor], coordinates_to_nodes[n], path_counter+1)) # last step
                if n in coordinates_to_nodes.keys() and n in seen and n != node_anchor:
                    edges.append((coordinates_to_nodes[node_anchor], coordinates_to_nodes[n], path_counter+1)) # last step
            valid_neighbors_and_dists = [n for n in neighbors_and_dists if can_step_on(n) and n not in seen]
            if len(valid_neighbors_and_dists) == 0:
                break # we are at a deadge end
            if len(valid_neighbors_and_dists) > 1:
                update_with_node(current_pos)
                # get the edges too
                edges.append((coordinates_to_nodes[node_anchor], coordinates_to_nodes[current_pos], path_counter))
                for valid_neighbor_and_dist in valid_neighbors_and_dists:
                    queue.append((current_pos, valid_neighbor_and_dist))
                break
            current_pos = valid_neighbors_and_dists[0]
            seen.add(current_pos)
            path_counter += 1
    # print(len(seen))
    # print(coordinates_to_nodes)
    # print()
    # print(nodes)
    # print(edges)
    START_NODE = 1
    END_NODE = 2
    cached_neighbors = dict()
    def find_neighbors(node):
        if node in cached_neighbors:
            return cached_neighbors[node]
        ret = []
        for e in edges:
            if e[0] == node:
                ret.append((e[1], e[2]))
            if e[1] == node:
                ret.append((e[0], e[2]))
        cached_neighbors[node] = ret
        return ret

    # ok now we just need to find the longest path from 1 to 2 that doesn't repeat any noes
    branches = []
    branches.append((START_NODE, set([START_NODE]), 0))
    hike_lengths = []
    while len(branches) > 0:
        current_branch = branches.pop()
        current_node, current_history, current_hike_length = current_branch
        # print(len(branches))
        # print(current_node, len(branches))
        if current_node == END_NODE:
            # print(f"END with {len(current_history)-1}")
            hike_lengths.append(current_hike_length)
        neighbors_and_dists = find_neighbors(current_node)
        valid_neighbors_and_dists = [n for n in neighbors_and_dists if n[0] not in current_history]
        for valid_neighbor_and_dist in valid_neighbors_and_dists:
            branches.append((valid_neighbor_and_dist[0], current_history.union([valid_neighbor_and_dist[0]]), current_hike_length + valid_neighbor_and_dist[1]))
    print(max(hike_lengths))

if __name__ == '__main__':
    main()
    main2()
