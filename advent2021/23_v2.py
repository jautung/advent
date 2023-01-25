import sys 
sys.path.append('..')

import copy
import heapq
from collections import defaultdict
from helper import *

FILENAME = '23_v2_dat.txt'
MAPPER = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

def main():
    data = readlines(FILENAME)
    data = data[2:-1]
    data = [[dat[i] for i in range(3, len(dat), 2) if dat[i] != '#'] for dat in data]
    data = transpose(reversed(data))
    clean_data = [[]]
    idx = 1
    out_idxs = set([0])
    in_idxs = set()
    for dat in data:
        clean_data.append([])
        out_idxs.add(idx)
        idx += 1
        clean_data.append(list(dat))
        in_idxs.add(idx)
        idx += 1
    clean_data.append([])
    out_idxs.add(idx)
    idx += 1
    clean_data.append([])
    out_idxs.add(idx)
    idx += 1
    max_size = len(data[0])

    # print(max_size)
    # print(out_idxs)
    # print(in_idxs)
    # print_2d(clean_data)
    # hash_pos(clean_data, max_size, out_idxs, in_idxs)

    dest_node = [[]]
    idx = 1
    for dat in data:
        dest_node.append([])
        idx += 1
        dest_node.append([correct_name(idx)] * max_size)
        idx += 1
    dest_node.append([])
    dest_node.append([])
    hashed_dest_node = hash_pos(dest_node, max_size, out_idxs, in_idxs)
    # print_2d(dest_node)

    # dijkstra
    visited_nodes = set()
    best_costs = dict()
    best_costs[hash_pos(clean_data, max_size, out_idxs, in_idxs)] = (0, clean_data)
    best_costs_heap = [(0, hash_pos(clean_data, max_size, out_idxs, in_idxs))]
    heapq.heapify(best_costs_heap)

    while True:
        # x, c, i = get_min_best_cost(best_costs, visited_nodes)
        c, i = heapq.heappop(best_costs_heap)
        if i == hashed_dest_node:
            # print(i, 'visited', len(visited_nodes), c)
            # print_best_costs(best_costs)
            # print()
            print('REACHED DEST!!!')
            print(c)
            break
        x = best_costs[i][1]
        # print(x, c)
        visit_node(x, i, c, max_size, out_idxs, in_idxs, visited_nodes, best_costs, best_costs_heap)
        # print(i, 'visited', len(visited_nodes), c)
        # print_best_costs(best_costs)
        # print()
        if len(visited_nodes) % 1000 == 0:
            print('visited', len(visited_nodes), len(best_costs))
    # print_best_costs(best_costs)
    # print(len(visited_nodes))

    # printing for fun
    i = hashed_dest_node
    blah = [i]
    while i != hash_pos(clean_data, max_size, out_idxs, in_idxs):
        i = best_costs[i][2]
        blah.append(i)
    print_2d(reversed(blah))

def visit_node(curr_node, hashed_curr_node, cost_to_curr_node, max_size, out_idxs, in_idxs, visited_nodes, best_costs, best_costs_heap):
    # curr_node = clean_data
    # cost_to_curr_node = 0
    # print(best_costs)

    neighbors = find_nexts(curr_node, max_size, out_idxs, in_idxs)
    # xd = [(hash_pos(i[0], max_size, out_idxs, in_idxs), i[1]) for i in neighbors]
    # print_2d(xd)

    for neighbor, edge_cost in neighbors:
        hashed = hash_pos(neighbor, max_size, out_idxs, in_idxs)
        if hashed not in best_costs or best_costs[hashed][0] > edge_cost + cost_to_curr_node:
            best_costs[hashed] = (edge_cost + cost_to_curr_node, neighbor, hashed_curr_node)
            heapq.heappush(best_costs_heap, (edge_cost + cost_to_curr_node, hashed))
    visited_nodes.add(hash_pos(curr_node, max_size, out_idxs, in_idxs))

    # print(best_costs)
    # print_best_costs(best_costs)
    # print(visited_nodes)
    # x, c = get_min_best_cost(best_costs, visited_nodes)
    # print(x, c)

# def get_min_best_cost(best_costs, visited_nodes):
#     do_this = None
#     do_this_cost = None
#     do_this_hash = None
#     for i in best_costs:
#         if i in visited_nodes:
#             continue
#         if do_this == None or best_costs[i][0] < do_this_cost:
#             do_this = best_costs[i][1]
#             do_this_cost = best_costs[i][0]
#             do_this_hash = i
#         # print(i, best_costs[i][0])
#     return do_this, do_this_cost, do_this_hash

def print_best_costs(best_costs):
    for i in best_costs:
        print(i, best_costs[i][0])

def hash_pos(pos, max_size, out_idxs, in_idxs):
    # pos[2].pop()
    # print_2d(pos)
    a = [''.join(i) for i in pos]
    b = [i.ljust(max_size, ' ') if n in in_idxs else i.ljust(1, ' ') for n, i in enumerate(a)]
    # print(''.join(b))
    return ''.join(b)

def find_nexts(pos, max_size, out_idxs, in_idxs):
    res = []
    for i in in_idxs:
        if len(pos[i]) > 0 and set(pos[i]) != set(correct_name(i)): # this means all ppl are at home alr
            move_out_spaces = max_size - len(pos[i]) + 1
            for move_back in range(i-1, -1, -1):
                if move_back in in_idxs:
                    continue
                assert(move_back in out_idxs)
                if len(pos[move_back]) == 0:
                    res.append(apply_move(pos, i, move_back, move_out_spaces + abs(i - move_back)))
                else:
                    break
            for move_forward in range(i+1, len(pos), 1):
                if move_forward in in_idxs:
                    continue
                assert(move_forward in out_idxs)
                if len(pos[move_forward]) == 0:
                    res.append(apply_move(pos, i, move_forward, move_out_spaces + abs(i - move_forward)))
                else:
                    break
    for i in out_idxs:
        if len(pos[i]) > 0:
            for move_back in range(i-1, -1, -1):
                if move_back in out_idxs:
                    if len(pos[move_back]) == 0:
                        continue
                    else:
                        break # cannot move anymore
                assert(move_back in in_idxs)
                if pos[i][0] == correct_name(move_back) and (len(pos[move_back]) == 0 or set(pos[move_back]) == set(correct_name(move_back))): # home is safe to join
                    move_in_spaces = max_size - len(pos[move_back])
                    res.append(apply_move(pos, i, move_back, move_in_spaces + abs(i - move_back)))
                    # print('XXX', pos, i, move_back, move_in_spaces + abs(i - move_back))
            for move_forward in range(i+1, len(pos), 1):
                if move_forward in out_idxs:
                    if len(pos[move_forward]) == 0:
                        continue
                    else:
                        break # cannot move anymore
                assert(move_forward in in_idxs)
                if pos[i][0] == correct_name(move_forward) and (len(pos[move_forward]) == 0 or set(pos[move_forward]) == set(correct_name(move_forward))): # home is safe to join
                    move_in_spaces = max_size - len(pos[move_forward])
                    res.append(apply_move(pos, i, move_forward, move_in_spaces + abs(i - move_forward)))
                    # print('XXX', pos, i, move_forward, move_in_spaces + abs(i - move_forward))
    return res

def correct_name(idx):
    return chr(65 + (idx-2)//2)

def apply_move(pos, frm, to, moves):
    pos_copy = [a[:] for a in pos]
    t = pos_copy[frm].pop()
    pos_copy[to].append(t)
    # MAPPER[t] * moves
    # print(frm, to)
    return pos_copy, MAPPER[t] * moves

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
