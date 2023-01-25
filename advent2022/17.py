import sys 
sys.path.append('..')

import copy
import time
from collections import defaultdict
from helper import *

FILENAME = '17_dat.txt'
mapper = {}

ROCK_1 = [(0,0),(1,0),(2,0),(3,0)]
ROCK_2 = [(0,1),(1,0),(1,1),(1,2),(2,1)]
ROCK_3 = [(0,0),(1,0),(2,0),(2,1),(2,2)]
ROCK_4 = [(0,0),(0,1),(0,2),(0,3)]
ROCK_5 = [(0,0),(0,1),(1,0),(1,1)]

ROCKS = [
    ROCK_1,
    ROCK_2,
    ROCK_3,
    ROCK_4,
    ROCK_5,
]

WIDTH = 7

def main():
    data = list(readlines(FILENAME)[0])

    curr_ground_height = 0
    curr_rock_type = 0
    curr_rock_pos = (2,3)
    # top_heights = dict()
    # for i in range(WIDTH):
    #     top_heights = 0
    stopped_poses = set()
    stopped_rock_count = 0

    N_ROCKS_STOPPED = 2022

    i = 0
    while True:
        # print('a', curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

        curr_rock = ROCKS[curr_rock_type]

        # JET
        jet = data[i%len(data)]
        if jet == '<':
            if curr_rock_pos[0] + rock_min_x(curr_rock) > 0:
                test_rock_pos = add_tup(curr_rock_pos,(-1,0))
        elif jet == '>':
            # print(curr_rock_pos[0])
            # print(curr_rock)
            # print(rock_max_x(curr_rock))
            # print(WIDTH-1)
            if curr_rock_pos[0] + rock_max_x(curr_rock) < WIDTH-1:
                test_rock_pos = add_tup(curr_rock_pos,(1,0))
        else:
            assert(False)
        test_poses = set([add_tup(test_rock_pos,s) for s in curr_rock])
        if len(test_poses.intersection(stopped_poses)) == 0:
            curr_rock_pos = test_rock_pos

        # print(jet, curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

        # FALL
        test_rock_pos = add_tup(curr_rock_pos,(0,-1))
        test_poses = set([add_tup(test_rock_pos,s) for s in curr_rock])
        if curr_rock_pos[1] > 0 and len(test_poses.intersection(stopped_poses)) == 0:
            curr_rock_pos = test_rock_pos
        else:
            stopped_rock = [(add_tup(curr_rock_pos,s)) for s in curr_rock]
            # print('stopped', stopped_rock)
            stopped_rock_count += 1
            stopped_poses = stopped_poses.union(stopped_rock)
            curr_ground_height = max(curr_ground_height, max([s[1] for s in stopped_rock]))
            if stopped_rock_count == N_ROCKS_STOPPED:
                print(curr_ground_height+1)
                return
            curr_rock_type = (curr_rock_type+1)%5
            curr_rock_pos = (2,curr_ground_height+4)

        i += 1
        # print('af', curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

    # print(data)

def add_tup(t1,t2):
    return (t1[0]+t2[0],t1[1]+t2[1])

def rock_min_x(r):
    return min([s[0] for s in r])

def rock_max_x(r):
    return max([s[0] for s in r])

# def main2():
#     data = list(readlines(FILENAME)[0])
    
#     curr_ground_height = 0
#     curr_rock_type = 0
#     curr_rock_pos = (2,3)
#     # top_heights = dict()
#     # for i in range(WIDTH):
#     #     top_heights = 0
#     stopped_poses = set()
#     stopped_rock_count = 0

#     # N_ROCKS_STOPPED = 10000
#     N_ROCKS_STOPPED = 200000
#     # N_ROCKS_STOPPED = 1000000000000

#     current_offset = 0

#     i = 0
#     while True:
#         # print('a', curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

#         curr_rock = ROCKS[curr_rock_type]

#         # JET
#         jet = data[i%len(data)]
#         if jet == '<':
#             if curr_rock_pos[0] + rock_min_x(curr_rock) > 0:
#                 test_rock_pos = add_tup(curr_rock_pos,(-1,0))
#         elif jet == '>':
#             # print(curr_rock_pos[0])
#             # print(curr_rock)
#             # print(rock_max_x(curr_rock))
#             # print(WIDTH-1)
#             if curr_rock_pos[0] + rock_max_x(curr_rock) < WIDTH-1:
#                 test_rock_pos = add_tup(curr_rock_pos,(1,0))
#         else:
#             assert(False)
#         test_poses = set([add_tup(test_rock_pos,s) for s in curr_rock])
#         if len(test_poses.intersection(stopped_poses)) == 0:
#             curr_rock_pos = test_rock_pos

#         # print(jet, curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

#         # FALL
#         test_rock_pos = add_tup(curr_rock_pos,(0,-1))
#         test_poses = set([add_tup(test_rock_pos,s) for s in curr_rock])
#         if curr_rock_pos[1] > 0 and len(test_poses.intersection(stopped_poses)) == 0:
#             curr_rock_pos = test_rock_pos
#         else:
#             stopped_rock = [(add_tup(curr_rock_pos,s)) for s in curr_rock]

#             if should_prune(stopped_rock_count):
#                 # print('stopped', stopped_rock, stopped_poses)
#                 peak_stopped_left = find_peak_left(stopped_poses)
#                 peak_stopped_right = find_peak_right(stopped_poses)
#                 # print(peak_stopped_left,peak_stopped_right)
#                 if peak_stopped_left and peak_stopped_right:
#                     top_edge = find_path((0,peak_stopped_left), (WIDTH-1,peak_stopped_right), stopped_poses)
#                     if top_edge:
#                         # print(top_edge)
#                         # prune(stopped_poses)
#                         # print('pruning')
#                         stopped_poses = prune_above_path(top_edge, stopped_poses)
#                         # print(stopped_poses)
#                         offset_by, stopped_poses = update_offset(stopped_poses)
#                         # print(stopped_poses)
#                         # print(offset_by)
#                         # exit(1)
#                         stopped_rock = [add_tup(p, (0,-offset_by)) for p in stopped_rock]
#                         curr_ground_height -= offset_by
#                         current_offset += offset_by

#             stopped_rock_count += 1
#             stopped_poses = stopped_poses.union(stopped_rock)
#             curr_ground_height = max(curr_ground_height, max([s[1] for s in stopped_rock]))

#             if stopped_rock_count % 10000 == 0:
#                 print(stopped_rock_count // 10000, 'of', N_ROCKS_STOPPED // 10000)
#             if stopped_rock_count == N_ROCKS_STOPPED:
#                 print(curr_ground_height+current_offset+1)
#                 # for y in range(4000):
#                 #     if sum([(x,y) in stopped_poses for x in range(WIDTH)]) == WIDTH:
#                 #         print('cutoff', y)
#                 # for y in range(17,-1,-1):
#                 #     for x in range(WIDTH):
#                 #         if (x,y) in stopped_poses:
#                 #             print('#',end='')
#                 #         else:
#                 #             print('.',end='')
#                 #     print()
#                 return

#             curr_rock_type = (curr_rock_type+1)%5
#             curr_rock_pos = (2,curr_ground_height+4)

#         i += 1
#         # print('af', curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

#     # print(data)

def main2():
    # ahhhh so i heard we should be looking for cycles with a full horizontal line
    data = list(readlines(FILENAME)[0])

    curr_ground_height = 0
    curr_rock_type = 0
    curr_rock_pos = (2,3)
    # top_heights = dict()
    # for i in range(WIDTH):
    #     top_heights = 0
    stopped_poses = set()
    stopped_rock_count = 0

    # N_ROCKS_STOPPED = 7000

    cache_ground_heights_until_cycle = dict()
    cycle_start = None
    cycle_end = None

    i = 0
    while True:
        # print('a', curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

        curr_rock = ROCKS[curr_rock_type]

        # JET
        jet = data[i%len(data)]
        if jet == '<':
            if curr_rock_pos[0] + rock_min_x(curr_rock) > 0:
                test_rock_pos = add_tup(curr_rock_pos,(-1,0))
        elif jet == '>':
            # print(curr_rock_pos[0])
            # print(curr_rock)
            # print(rock_max_x(curr_rock))
            # print(WIDTH-1)
            if curr_rock_pos[0] + rock_max_x(curr_rock) < WIDTH-1:
                test_rock_pos = add_tup(curr_rock_pos,(1,0))
        else:
            assert(False)
        test_poses = set([add_tup(test_rock_pos,s) for s in curr_rock])
        if len(test_poses.intersection(stopped_poses)) == 0:
            curr_rock_pos = test_rock_pos

        # print(jet, curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

        # FALL
        test_rock_pos = add_tup(curr_rock_pos,(0,-1))
        test_poses = set([add_tup(test_rock_pos,s) for s in curr_rock])
        if curr_rock_pos[1] > 0 and len(test_poses.intersection(stopped_poses)) == 0:
            curr_rock_pos = test_rock_pos
        else:
            stopped_rock = [(add_tup(curr_rock_pos,s)) for s in curr_rock]
            # print('stopped', stopped_rock)
            stopped_rock_count += 1
            stopped_poses = stopped_poses.union(stopped_rock)
            the_line = has_top_line(stopped_poses)
            if the_line != None and curr_rock_type == 0:
                if cycle_start == None:
                    cycle_start = stopped_rock_count, the_line
                else:
                    cycle_end = stopped_rock_count, the_line
                # print('muahaha', curr_rock_type)
                    break
            curr_ground_height = max(curr_ground_height, max([s[1] for s in stopped_rock]))
            # if stopped_rock_count == N_ROCKS_STOPPED:
            #     print(curr_ground_height+1)
            #     return
            cache_ground_heights_until_cycle[stopped_rock_count] = curr_ground_height+1
            curr_rock_type = (curr_rock_type+1)%5
            curr_rock_pos = (2,curr_ground_height+4)

        i += 1
        # print('af', curr_rock_type, curr_rock_pos, curr_ground_height, stopped_poses)

    # print(data)
    # print(cycle_start)
    # print(cycle_end)
    # print_2d(cache_ground_heights_until_cycle)
    # print(len(cache_ground_heights_until_cycle))
    # print(cache_ground_heights_until_cycle[2022])

    def get_for_target(TARGET):
        # TARGET = 2022
        period = cycle_end[0]-cycle_start[0]
        factor = cycle_end[1]-cycle_start[1]
        in_cycles = TARGET-cycle_start[0]
        # print('in_cycles', in_cycles)
        # print('period', period)
        # print('factor', factor)
        # print('int(in_cycles / period)', int(in_cycles / period))
        # print('(in_cycles % period)', (in_cycles % period))
        # print('(in_cycles % period) + cycle_start[1]', (in_cycles % period) + cycle_start[1])
        final_ans = int(in_cycles / period) * factor + cache_ground_heights_until_cycle[(in_cycles % period) + cycle_start[0]]
        return final_ans

    # confidence check to match with naive approach
    # for t in [2022, 3000, 3500, 7000]:
    #     print(t, get_for_target(t))
        # 2022 3102
        # 3000 4604
        # 3500 5389
        # 7000 10771

    print(get_for_target(1000000000000))

def has_top_line(poses):
    top_y = max([pos[1] for pos in poses])
    if len(list(filter(lambda pos: pos[1] == top_y, poses))) == WIDTH:
    # per_line = def_dict(0)
    # for pos in poses:
    #     per_line[pos[1]] += 1
    #     if per_line[pos[1]] == WIDTH:
    #         return pos[1]
    # return None
        return top_y
    return None

def should_prune(stopped_rock_count):
    # Timings for N_ROCKS_STOPPED = 10000 // 200000
    # return True # 2.789508104324341 # 17.979686975479126
    # return False # 5.7189459800720215
    # return stopped_rock_count % 100 == 0 # 0.5885708332061768 # 11.216840982437134
    # return stopped_rock_count % 1000 == 0 # 0.7668051719665527 # 14.962826251983643
    # return stopped_rock_count % 10 == 0 # 0.68961501121521 # 10.210892915725708
    return stopped_rock_count % 5 == 0 # 9.704250812530518
    # return stopped_rock_count % 3 == 0 # 12.220921039581299

def find_peak_left(poses):
    cand = list(filter(lambda x: x != None, [p[1] if p[0] == 0 else None for p in poses]))
    if len(cand) == 0:
        return None
    return max(cand)

def find_peak_right(poses):
    cand = list(filter(lambda x: x != None, [p[1] if p[0] == WIDTH-1 else None for p in poses]))
    if len(cand) == 0:
        return None
    return max(cand)

def find_path(a,b,poses):
    if a == None or b == None:
        return None
    # print(a,b)
    paths = [(set([a]),a)]
    in_paths = set([a])
    while len(paths)>0:
        margin, last = paths.pop(0)
        neighbors = [
            add_tup(last,(0,1)),
            add_tup(last,(1,0)),
            add_tup(last,(-1,0)),
            add_tup(last,(0,-1)),
        ]
        for n in neighbors:
            if n == b:
                return set([b]).union(margin)
            if n not in in_paths and n in poses:
                paths.append((set([n]).union(margin),n))
                in_paths.add(last)
    return None

def prune_above_path(path,poses):
    min_per_x = dict()
    for x in range(WIDTH):
        min_per_x[x] = min(filter(lambda x: x != None, [p[1] if p[0] == x else None for p in path]))
    return set(filter(lambda p: p[1] >= min_per_x[p[0]], poses))

def update_offset(poses):
    min_y = min([p[1] for p in poses])
    return min_y, set([add_tup(p, (0,-min_y)) for p in poses])

if __name__ == '__main__':
    # s = time.time()
    main()
    # print(time.time()-s)
    # s = time.time()
    main2()
    # print(time.time()-s)
