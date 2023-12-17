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
    brute(data)

def brute(data):
    START = (0,0)
    GOAL = (len(data)-1, len(data[0])-1)
    to_explore = [([], START, 0, set([START]))] # history of last 3 dirs, latest point, current cost, points on path
    def in_map(coord):
        row, col = coord
        if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
            return False
        return True
    counter = 0
    incumbent = None
    while len(to_explore) > 0:
        # print(counter, to_explore) 
        # if counter == 10:
        #     break
        if counter % 1000 == 0:
            print(counter, len(to_explore))
        explore = to_explore.pop(heuristic(to_explore)) # this technically goes dfs in a weird way
        hist_dirs, latest_p, current_cost, points_already_in = explore
        if latest_p == GOAL:
            if incumbent == None:
                incumbent = current_cost
                print(f"OMG I GOT TO THE END, CURRENT MIN: {incumbent}, {''.join(hist_dirs)}")
            else:
                if current_cost < incumbent:
                    incumbent = current_cost
                    print(f"OMG I GOT TO THE END BETTER, CURRENT MIN: {incumbent}, {''.join(hist_dirs)}")
            # incumbent = min(incumbent, current_cost) if incumbent != None else current_cost
            # print(f"OMG I GOT TO THE END, CURRENT MIN: {incumbent}")
            # print(current_cost, points_already_in)
            # print(current_cost)
        blocked_dir = matching(hist_dirs)
        next_points = []
        if blocked_dir != 'L' and in_map((latest_p[0], latest_p[1]-1)) and (latest_p[0], latest_p[1]-1) not in points_already_in:
            next_points.append(('L', (latest_p[0], latest_p[1]-1), data[latest_p[0]][latest_p[1]-1]))
        if blocked_dir != 'U' and in_map((latest_p[0]-1, latest_p[1])) and (latest_p[0]-1, latest_p[1]) not in points_already_in:
            next_points.append(('U', (latest_p[0]-1, latest_p[1]), data[latest_p[0]-1][latest_p[1]]))
        if blocked_dir != 'R' and in_map((latest_p[0], latest_p[1]+1)) and (latest_p[0], latest_p[1]+1) not in points_already_in:
            next_points.append(('R', (latest_p[0], latest_p[1]+1), data[latest_p[0]][latest_p[1]+1]))
        if blocked_dir != 'D' and in_map((latest_p[0]+1, latest_p[1])) and (latest_p[0]+1, latest_p[1]) not in points_already_in:
            next_points.append(('D', (latest_p[0]+1, latest_p[1]), data[latest_p[0]+1][latest_p[1]]))
        for next_p in next_points:
            to_explore.append((
                hist_dirs + [next_p[0]],
                next_p[1],
                current_cost + next_p[2],
                set(list(points_already_in) + [next_p[1]]),
            ))
        counter += 1
        # exit(1)
    print(to_explore) 

def heuristic(explores):
    ps = [e[1][0] + e[1][1] for e in explores]
    a = max(ps)
    return ps.index(a)
    # return -1

def matching(hist_dirs):
    if len(hist_dirs) < 3:
        return None
    if hist_dirs[-3] == hist_dirs[-2] and hist_dirs[-3] == hist_dirs[-1]:
        return hist_dirs[-3]
    return None

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

def get_at(data, row, col):
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
        return None
    return data[row][col]

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
