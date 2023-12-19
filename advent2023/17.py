from heapq import heapify, heappush, heappop 
import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '17_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(c) for c in dat] for dat in data]
    
    # print_2d(data)
    # a node in this graph is a tuple [dir1, dir2, dir3, row, col]
    
    # # Creating empty heap 
    # heap = [] 
    # heapify(heap) 
    
    # # Adding items to the heap using heappush function 
    # heappush(heap, 10) 
    # heappush(heap, 30) 
    # heappush(heap, 20) 
    # heappush(heap, 400)
    
    # a = heappop(heap)
    # print(a)
    # a = heappop(heap)
    # print(a)
    # a = heappop(heap)
    # print(a)
    
    # SIMPLE DIJKSTRA WITH 4^3 the number of nodes
    
    def in_map(row, col):
        return row >= 0 and row < len(data) and col >= 0 and col < len(data[0])
    
    def get_valid_neighbors(node, seen_geographical_nodes):
        dir1, dir2, dir3, row, col = node
        valid_neighbors = []
        for new_row, new_col, new_step_dir in [(row+1, col, 'D'), (row-1, col, 'U'), (row, col+1, 'R'), (row, col-1, 'L')]:
            if not in_map(new_row, new_col):
                continue
            if (new_row, new_col) in seen_geographical_nodes:
                continue
            if dir1 == dir2 and dir1 == dir3 and dir1 == new_step_dir:
                continue
            valid_neighbors.append((dir2, dir3, new_step_dir, new_row, new_col))
        return valid_neighbors

    FIRST_NODE = ('X', 'X', 'X', 0, 0)
    frontier_to_explore_heap = []
    heapify(frontier_to_explore_heap)
    heappush(frontier_to_explore_heap, (0, FIRST_NODE, set([(0, 0)])))
    nodes_in_the_heap = set()
    nodes_in_the_heap.add(FIRST_NODE)
    # geographical_nodes_in_the_heap = set()
    # geographical_nodes_in_the_heap.add((0, 0))
    distances_known = dict()
    distances_known[FIRST_NODE] = 0
    while True:
        try:
            current_node = heappop(frontier_to_explore_heap)
        except IndexError:
            break
        nodes_in_the_heap.remove(current_node[1])
        current_cost = current_node[0]
        current_dir1, current_dir2, current_dir3, current_row, current_col = current_node[1]
        # print(f"Processing node {current_node[1]} with current cost {current_cost} and current seen set {current_node[2]}")
        next_nodes = get_valid_neighbors((current_dir1, current_dir2, current_dir3, current_row, current_col), current_node[2])
        for next_node in next_nodes:
            # print(f"  Valid neighbor: {next_node}")
            additional_cost = data[next_node[3]][next_node[4]]
            new_alt_cost = current_cost + additional_cost
            if next_node not in distances_known or distances_known[next_node] > new_alt_cost:
                distances_known[next_node] = new_alt_cost
                if next_node not in nodes_in_the_heap:
                    new_seen_set = current_node[2].copy()
                    new_seen_set.add((next_node[3], next_node[4]))
                    # print(f"  Adding neighbor at cost {new_alt_cost} and new seen set {new_seen_set}")
                    heappush(frontier_to_explore_heap, (new_alt_cost, next_node, new_seen_set))
                    nodes_in_the_heap.add(next_node)
                # DO WE NEED AN ELSE TO UPDATE THE PRIORITY OF THE NEXT_NODE IN THE HEAP?
    # print(distances_known)
    to_the_end = []
    for key in distances_known:
        if key[3] == len(data) - 1 and key[4] == len(data[0]) - 1:
            # print(key, distances_known[key])
            to_the_end.append(distances_known[key])
    print(min(to_the_end))
    
    # best_route_found_to_end = [[None for i in range(len(data[0]))] for j in range(len(data))]
    # the_steps = [[None for i in range(len(data[0]))] for j in range(len(data))]
    # print(data)
    # print(data)
    # print(best_route_found_to_end)
    # best_route_found_to_end[-1][-1] = data[-1][-1]
    # the_steps[-1][-1] = []
    # print_2d(data)
    # print()
    # print_2d(best_route_found_to_end)
    # print()
    # THIS IS THE BASIC ROUTE SECTION WITHOUT THE 3-MOVE-DIR RESTRICTION
    # UPPER_BOUND_ROUTE = len(data) * len(data[0])
    # print(UPPER_BOUND_ROUTE)
    # for i in range(UPPER_BOUND_ROUTE+1):
    #     if i % 100 == 0:
    #         print(i)
    #     iterate_on(best_route_found_to_end, data)
        # exit(1)
    # print_2d(best_route_found_to_end)
    # print()
    # ok we have the best case without the 3-move-dir restriction
    # now we astar the shit out of this with this heuristic?
    # apply_a_star(data, best_route_found_to_end)
    # THE PATH IS PART OF THE GRAPH, SO IT'S SUPER WEIRD TO FIND POSSIBLE NEIGHBORS
    # becaus hte same neighbor can be better with a different path even though the current cost is higher?!?!
    
    # HYPOTHETICALLY HOW BAD IS BRUTE FORCE?
    # brute(data)

# def brute(data):
#     START = (0,0)
#     GOAL = (len(data)-1, len(data[0])-1)
#     to_explore = [([], START, 0, set([START]))] # history of last 3 dirs, latest point, current cost, points on path
#     def in_map(coord):
#         row, col = coord
#         if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
#             return False
#         return True
#     counter = 0
#     incumbent = None
#     while len(to_explore) > 0:
#         # print(counter, to_explore) 
#         # if counter == 10:
#         #     break
#         if counter % 1000 == 0:
#             print(counter, len(to_explore))
#         explore = to_explore.pop(heuristic(to_explore)) # this technically goes dfs in a weird way
#         hist_dirs, latest_p, current_cost, points_already_in = explore
#         if latest_p == GOAL:
#             if incumbent == None:
#                 incumbent = current_cost
#                 print(f"OMG I GOT TO THE END, CURRENT MIN: {incumbent}, {''.join(hist_dirs)}")
#             else:
#                 if current_cost < incumbent:
#                     incumbent = current_cost
#                     print(f"OMG I GOT TO THE END BETTER, CURRENT MIN: {incumbent}, {''.join(hist_dirs)}")
#             # incumbent = min(incumbent, current_cost) if incumbent != None else current_cost
#             # print(f"OMG I GOT TO THE END, CURRENT MIN: {incumbent}")
#             # print(current_cost, points_already_in)
#             # print(current_cost)
#         blocked_dir = matching(hist_dirs)
#         next_points = []
#         if blocked_dir != 'L' and in_map((latest_p[0], latest_p[1]-1)) and (latest_p[0], latest_p[1]-1) not in points_already_in:
#             next_points.append(('L', (latest_p[0], latest_p[1]-1), data[latest_p[0]][latest_p[1]-1]))
#         if blocked_dir != 'U' and in_map((latest_p[0]-1, latest_p[1])) and (latest_p[0]-1, latest_p[1]) not in points_already_in:
#             next_points.append(('U', (latest_p[0]-1, latest_p[1]), data[latest_p[0]-1][latest_p[1]]))
#         if blocked_dir != 'R' and in_map((latest_p[0], latest_p[1]+1)) and (latest_p[0], latest_p[1]+1) not in points_already_in:
#             next_points.append(('R', (latest_p[0], latest_p[1]+1), data[latest_p[0]][latest_p[1]+1]))
#         if blocked_dir != 'D' and in_map((latest_p[0]+1, latest_p[1])) and (latest_p[0]+1, latest_p[1]) not in points_already_in:
#             next_points.append(('D', (latest_p[0]+1, latest_p[1]), data[latest_p[0]+1][latest_p[1]]))
#         for next_p in next_points:
#             to_explore.append((
#                 hist_dirs + [next_p[0]],
#                 next_p[1],
#                 current_cost + next_p[2],
#                 set(list(points_already_in) + [next_p[1]]),
#             ))
#         counter += 1
#         # exit(1)
#     print(to_explore) 

# def heuristic(explores):
#     ps = [e[1][0] + e[1][1] for e in explores]
#     a = max(ps)
#     return ps.index(a)
#     # return -1

# def matching(hist_dirs):
#     if len(hist_dirs) < 3:
#         return None
#     if hist_dirs[-3] == hist_dirs[-2] and hist_dirs[-3] == hist_dirs[-1]:
#         return hist_dirs[-3]
#     return None

# def apply_a_star(data, best_route_found_to_end):
#     open_set = set()
#     START = (0,0)
#     open_set.add(START)
#     # goal is (len(data)-1, len(data[0])-1)
#     GOAL = (len(data)-1, len(data[0])-1)
#     def h_score(coord):
#         return best_route_found_to_end[coord[0]][coord[1]]
#     came_from = dict()
#     g_score = dict()
#     g_score[START] = 0
#     f_score = dict()
#     f_score[START] = h_score(START)
#     while len(open_set) > 0:
#         lst = [(coord, f_score[coord]) for coord in open_set if coord in f_score]
#         current_coord, current_f_score = min(lst, key=lambda x: x[1])
#         if current_coord == GOAL:
#             print("YAY")
#             return
#         open_set.pop(current_coord)
#         potential_neighbors = [
#             (current_coord[0]-1, current_coord[1]),
#             (current_coord[0]+1, current_coord[1]),
#             (current_coord[0], current_coord[1]-1),
#             (current_coord[0], current_coord[1]+1),
#         ]
#         # need to do the 3-step filtering here
#         for neighbor in potential_neighbors:
#             tentative_g_score = g_score[current_coord] + data[neighbor[0]][neighbor[1]]
#             if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                 came_from[neighbor] = current_coord
#                 g_score

# def iterate_on(best_route_found_to_end, data):
#     for row in range(len(data)):
#         for col in range(len(data[0])):
#             options = []
#             if best_route_found_to_end[row][col] != None:
#                 # don't change the_steps
#                 options.append(best_route_found_to_end[row][col])
#             neighbors = [
#                 get_at(best_route_found_to_end, row-1, col), # the_steps needs to append a 'D'
#                 get_at(best_route_found_to_end, row+1, col), # the_steps needs to append a 'U'
#                 get_at(best_route_found_to_end, row, col-1), # the_steps needs to append a 'R'
#                 get_at(best_route_found_to_end, row, col+1), # the_steps needs to append a 'L'
#             ]
#             valid_neighbors = [n for n in neighbors if n != None]
#             if len(valid_neighbors) > 0:
#                 new_val = data[row][col] + min(valid_neighbors)
#                 options.append(new_val)
#             # print(options)
#             if len(options) > 0:
#                 best_route_found_to_end[row][col] = min(options)
#                 # print(row, col, neighbors, options, min(options))
#             else:
#                 # print(row, col, "Nothing")
#                 pass

# def get_at(data, row, col):
#     if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
#         return None
#     return data[row][col]

def main2():
    data = readlines(FILENAME)
    data = [[int(c) for c in dat] for dat in data]
    
    # print_2d(data)
    # a node in this graph is a tuple [dir1, dir2, dir3, row, col]
    
    # # Creating empty heap 
    # heap = [] 
    # heapify(heap) 
    
    # # Adding items to the heap using heappush function 
    # heappush(heap, 10) 
    # heappush(heap, 30) 
    # heappush(heap, 20) 
    # heappush(heap, 400)
    
    # a = heappop(heap)
    # print(a)
    # a = heappop(heap)
    # print(a)
    # a = heappop(heap)
    # print(a)
    
    # SIMPLE DIJKSTRA WITH 4^3 the number of nodes
    
    # def in_map(row, col):
    #     return row >= 0 and row < len(data) and col >= 0 and col < len(data[0])
    
    # def get_valid_neighbors(node, seen_geographical_nodes):
    #     prev_dir, row, col = node
    #     valid_neighbors = []
    #     def opposite_dir(dir1, dir2):
    #         if set([dir1, dir2]) == set(['L', 'R']):
    #             return True
    #         if set([dir1, dir2]) == set(['U', 'D']):
    #             return True
    #         return False
    #     for n_in_dir in range(4, 11):
    #         for new_row, new_col, new_step_dir in [(row+n_in_dir, col, 'D'), (row-n_in_dir, col, 'U'), (row, col+n_in_dir, 'R'), (row, col-n_in_dir, 'L')]:
    #             if not in_map(new_row, new_col):
    #                 continue
    #             if (new_row, new_col) in seen_geographical_nodes:
    #                 continue
    #             if prev_dir == new_step_dir or opposite_dir(prev_dir, new_step_dir):
    #                 continue
    #             valid_neighbors.append((new_step_dir, new_row, new_col))
    #     return valid_neighbors

    # FIRST_NODE = ('X', 0, 0)
    # frontier_to_explore_heap = []
    # heapify(frontier_to_explore_heap)
    # heappush(frontier_to_explore_heap, (0, FIRST_NODE, set([(0, 0)])))
    # nodes_in_the_heap = set()
    # nodes_in_the_heap.add(FIRST_NODE)
    # # geographical_nodes_in_the_heap = set()
    # # geographical_nodes_in_the_heap.add((0, 0))
    # distances_known = dict()
    # distances_known[FIRST_NODE] = 0
    # def all_geographical_nodes_between_excl_incl(coord1, coord2):
    #     if coord1[0] == coord2[0]:
    #         if coord2[1] > coord1[1]:
    #             return [(coord1[0], i) for i in range(coord1[1]+1, coord2[1]+1)]
    #         else:
    #             return [(coord1[0], i) for i in range(coord1[1]-1, coord2[1]-1, -1)]
    #     elif coord1[1] == coord2[1]:
    #         if coord2[0] > coord1[0]:
    #             return [(i, coord1[1]) for i in range(coord1[0]+1, coord2[0]+1)]
    #         else:
    #             return [(i, coord1[1]) for i in range(coord1[0]-1, coord2[0]-1, -1)]
    #     assert(False)
    # def cost_between_excl_incl(coord1, coord2):
    #     nodes = all_geographical_nodes_between_excl_incl(coord1, coord2)
    #     # print(nodes)
    #     # print([data[node[0]][node[1]] for node in nodes])
    #     return sum([data[node[0]][node[1]] for node in nodes])
    # counter = 0
    # while True:
    #     try:
    #         current_node = heappop(frontier_to_explore_heap)
    #     except IndexError:
    #         break
    #     nodes_in_the_heap.remove(current_node[1])
    #     current_cost = current_node[0]
    #     current_prev_dir, current_row, current_col = current_node[1]
    #     print(f"Processing node {current_node[1]} with current cost {current_cost} and current seen set {current_node[2]}")
    #     next_nodes = get_valid_neighbors((current_prev_dir, current_row, current_col), current_node[2])
    #     for next_node in next_nodes:
    #         print(f"  Valid neighbor: {next_node}")
    #         additional_cost = cost_between_excl_incl((current_row, current_col), (next_node[1], next_node[2]))
    #         new_alt_cost = current_cost + additional_cost
    #         if next_node not in distances_known or distances_known[next_node] > new_alt_cost:
    #             distances_known[next_node] = new_alt_cost
    #             if next_node not in nodes_in_the_heap:
    #                 new_seen_set = current_node[2].copy()
    #                 new_seen_set.update(all_geographical_nodes_between_excl_incl((current_row, current_col), (next_node[1], next_node[2])))
    #                 print(f"  Adding neighbor at cost {new_alt_cost} and new seen set {new_seen_set}")
    #                 heappush(frontier_to_explore_heap, (new_alt_cost, next_node, new_seen_set))
    #                 nodes_in_the_heap.add(next_node)
    #             # DO WE NEED AN ELSE TO UPDATE THE PRIORITY OF THE NEXT_NODE IN THE HEAP?
    #     # if counter == 1:
    #     #     exit(1)
    #     counter += 1
    # print(distances_known)
    # to_the_end = []
    # for key in distances_known:
    #     if key[1] == len(data) - 1 and key[2] == len(data[0]) - 1:
    #         print(key, distances_known[key])
    #         to_the_end.append(distances_known[key])
    # print(min(to_the_end))

    def in_map(row, col):
        return row >= 0 and row < len(data) and col >= 0 and col < len(data[0])
    
    def get_valid_neighbors(node, seen_geographical_nodes):
        prev_dir, prev_dir_streak, row, col = node
        valid_neighbors = []
        for new_row, new_col, new_step_dir in [(row+1, col, 'D'), (row-1, col, 'U'), (row, col+1, 'R'), (row, col-1, 'L')]:
            if not in_map(new_row, new_col):
                continue
            if (new_row, new_col) in seen_geographical_nodes:
                continue
            if prev_dir == 'X':
                new_dir_streak = 1
            elif prev_dir == new_step_dir:
                # valid iff `prev_dir_streak` < 10
                if prev_dir_streak >= 10:
                    continue
                new_dir_streak = prev_dir_streak + 1
            elif prev_dir != new_step_dir:
                # valid iff `prev_dir_streak` >= 4
                if prev_dir_streak < 4:
                    continue
                new_dir_streak = 1
            valid_neighbors.append((new_step_dir, new_dir_streak, new_row, new_col))
        return valid_neighbors

    FIRST_NODE = ('X', -1, 0, 0)
    frontier_to_explore_heap = []
    heapify(frontier_to_explore_heap)
    heappush(frontier_to_explore_heap, (0, FIRST_NODE, set([(0, 0)])))
    nodes_in_the_heap = set()
    nodes_in_the_heap.add(FIRST_NODE)
    # geographical_nodes_in_the_heap = set()
    # geographical_nodes_in_the_heap.add((0, 0))
    distances_known = dict()
    distances_known[FIRST_NODE] = 0
    while True:
        try:
            current_node = heappop(frontier_to_explore_heap)
        except IndexError:
            break
        nodes_in_the_heap.remove(current_node[1])
        current_cost = current_node[0]
        current_prev_dir, current_prev_dir_streak, current_row, current_col = current_node[1]
        # print(f"Processing node {current_node[1]} with current cost {current_cost} and current seen set {current_node[2]}")
        next_nodes = get_valid_neighbors((current_prev_dir, current_prev_dir_streak, current_row, current_col), current_node[2])
        for next_node in next_nodes:
            # print(f"  Valid neighbor: {next_node}")
            additional_cost = data[next_node[2]][next_node[3]]
            new_alt_cost = current_cost + additional_cost
            if next_node not in distances_known or distances_known[next_node] > new_alt_cost:
                distances_known[next_node] = new_alt_cost
                if next_node not in nodes_in_the_heap:
                    new_seen_set = current_node[2].copy()
                    new_seen_set.add((next_node[2], next_node[3]))
                    # print(f"  Adding neighbor at cost {new_alt_cost} and new seen set {new_seen_set}")
                    heappush(frontier_to_explore_heap, (new_alt_cost, next_node, new_seen_set))
                    nodes_in_the_heap.add(next_node)
                # DO WE NEED AN ELSE TO UPDATE THE PRIORITY OF THE NEXT_NODE IN THE HEAP?
    # print(distances_known)
    to_the_end = []
    for key in distances_known:
        if key[2] == len(data) - 1 and key[3] == len(data[0]) - 1 and key[1] >= 4:
            # print(key, distances_known[key])
            to_the_end.append(distances_known[key])
    print(min(to_the_end))


if __name__ == '__main__':
    main()
    main2()
