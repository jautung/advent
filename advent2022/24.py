import sys 
sys.path.append('..')

import copy
import heapq
import math
import time
from collections import defaultdict
from helper import *

FILENAME = '24_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    arena = [dat[1:-1] for dat in data[1:-1]]
    # print_2d(arena)

    width = len(arena[0])
    height = len(arena)
    # print(data[0].index('.')-1)
    # print(data[-1].index('.')-1)
    start_pos = (data[0].index('.')-1, -1)
    end_pos = (data[-1].index('.')-1, height)
    # print(start_pos)
    # print(end_pos)

    repeating_interval = math.lcm(width, height)
    # print(repeating_interval)

    full_set = set()
    for i in range(height):
        for j in range(width):
            if arena[i][j] != '.':
                full_set.add(((j, i), arena[i][j]))
    # print(full_set)

    blizz_maps = dict()
    for step in range(repeating_interval):
        blizz_map = set()
        for init_pos, direction in full_set:
            if direction == '>':
                blizz_map.add(move_by_modulo(init_pos, (1,0), step, width, height))
            elif direction == '<':
                blizz_map.add(move_by_modulo(init_pos, (-1,0), step, width, height))
            elif direction == '^':
                blizz_map.add(move_by_modulo(init_pos, (0,-1), step, width, height))
            elif direction == 'v':
                blizz_map.add(move_by_modulo(init_pos, (0,1), step, width, height))
        blizz_maps[step] = blizz_map

    # for step in range(repeating_interval):
    #     print(step, blizz_maps[step])

    # bfs
    # paths = []
    # paths.append((0, start_pos)) # (time, current_pos)
    # seen_pairs = set()
    # seen_pairs.add((0, start_pos))
    # while len(paths) > 0:
    #     # print(len(paths))
    #     time, curr_pos = paths.pop(0)
    #     # print('checking out', curr_pos, 'at time', time)
    #     if (curr_pos[0], curr_pos[1]+1) == end_pos:
    #         print(time+1)
    #         return
    #     for possible_next in possible_nexts(blizz_maps[(time+1)%repeating_interval], curr_pos, width, height, start_pos, end_pos):
    #         if (time+1, possible_next) in seen_pairs:
    #             continue
    #         paths.append((time+1, possible_next))
    #         seen_pairs.add((time+1, possible_next))

    # a star
    frontier = []
    frontier.append((0, 0, start_pos))
    heapq.heapify(frontier)
    # cost_so_far = dict()
    # cost_so_far[(start_pos, 0)] = 0
    seen_pairs = set()
    seen_pairs.add((0, start_pos))
    while len(frontier) > 0:
        priority, time, curr_pos = heapq.heappop(frontier)
        # print('from', curr_pos, priority, time, len(frontier))
        # print('checking out', curr_pos, 'with tentative score of', priority, 'at time', time)
        if (curr_pos[0], curr_pos[1]+1) == end_pos:
            # print(cost_so_far[curr_pos]+1)
            print(time+1)
            return
        for possible_next in possible_nexts(blizz_maps[(time+1)%repeating_interval], curr_pos, width, height, start_pos, end_pos):
            if (time+1, possible_next) in seen_pairs:
                continue
            # print('>', possible_next)
            # new_cost = cost_so_far[curr_pos]+1
            # if possible_next not in cost_so_far or new_cost < cost_so_far[possible_next]:
            # cost_so_far[possible_next] = new_cost
            priority = time+1 + heuristic(possible_next, end_pos)
            # print('pushing', possible_next)
            heapq.heappush(frontier, (priority, time+1, possible_next))
            seen_pairs.add((time+1, possible_next))

def heuristic(possible_next, end_pos):
    return abs(possible_next[0]-end_pos[0]) + abs(possible_next[1]-end_pos[1])

def possible_nexts(blizz_map, curr_pos, width, height, start_pos, end_pos):
    res = []
    for cand in [(curr_pos[0],curr_pos[1]),(curr_pos[0]+1,curr_pos[1]),(curr_pos[0]-1,curr_pos[1]),(curr_pos[0],curr_pos[1]+1),(curr_pos[0],curr_pos[1]-1)]:
        if cand not in blizz_map and ((cand[0] >= 0 and cand[1] >= 0 and cand[0] < width and cand[1] < height) or cand == start_pos or cand == end_pos):
            res.append(cand)
    return res

def move_by_modulo(init_pos, direction, step, width, height):
    return ((init_pos[0]+direction[0]*step)%width, (init_pos[1]+direction[1]*step)%height)

def main2():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    arena = [dat[1:-1] for dat in data[1:-1]]
    # print_2d(arena)

    width = len(arena[0])
    height = len(arena)
    # print(data[0].index('.')-1)
    # print(data[-1].index('.')-1)
    start_pos = (data[0].index('.')-1, -1)
    end_pos = (data[-1].index('.')-1, height)
    # print(start_pos)
    # print(end_pos)

    repeating_interval = math.lcm(width, height)
    # print(repeating_interval)

    full_set = set()
    for i in range(height):
        for j in range(width):
            if arena[i][j] != '.':
                full_set.add(((j, i), arena[i][j]))
    # print(full_set)

    blizz_maps = dict()
    for step in range(repeating_interval):
        blizz_map = set()
        for init_pos, direction in full_set:
            if direction == '>':
                blizz_map.add(move_by_modulo(init_pos, (1,0), step, width, height))
            elif direction == '<':
                blizz_map.add(move_by_modulo(init_pos, (-1,0), step, width, height))
            elif direction == '^':
                blizz_map.add(move_by_modulo(init_pos, (0,-1), step, width, height))
            elif direction == 'v':
                blizz_map.add(move_by_modulo(init_pos, (0,1), step, width, height))
        blizz_maps[step] = blizz_map

    # for step in range(repeating_interval):
    #     print(step, blizz_maps[step])

    # bfs
    # paths = []
    # paths.append((0, start_pos)) # (time, current_pos)
    # while len(paths) > 0:
    #     # print(len(paths))
    #     time, curr_pos = paths.pop(0)
    #     # print('checking out', curr_pos, 'at time', time)
    #     if (curr_pos[0], curr_pos[1]+1) == end_pos:
    #         print(time+1)
    #         return
    #     for possible_next in possible_nexts(blizz_maps[(time+1)%repeating_interval], curr_pos, width, height, start_pos, end_pos):
    #         paths.append((time+1, possible_next))

    # a star
    frontier = []
    frontier.append((0, 0, start_pos))
    heapq.heapify(frontier)
    # cost_so_far = dict()
    # cost_so_far[(start_pos, 0)] = 0
    seen_pairs = set()
    seen_pairs.add((0, start_pos))
    while len(frontier) > 0:
        priority, time, curr_pos = heapq.heappop(frontier)
        # print('from', curr_pos, priority, time, len(frontier))
        # print('checking out', curr_pos, 'with tentative score of', priority, 'at time', time)
        if (curr_pos[0], curr_pos[1]+1) == end_pos:
            # print(cost_so_far[curr_pos]+1)
            end_time_ichi = time+1
            print('end_time_ichi', end_time_ichi)
            break
        for possible_next in possible_nexts(blizz_maps[(time+1)%repeating_interval], curr_pos, width, height, start_pos, end_pos):
            if (time+1, possible_next) in seen_pairs:
                continue
            # print('>', possible_next)
            # new_cost = cost_so_far[curr_pos]+1
            # if possible_next not in cost_so_far or new_cost < cost_so_far[possible_next]:
            # cost_so_far[possible_next] = new_cost
            priority = time+1 + heuristic(possible_next, end_pos)
            # print('pushing', possible_next)
            heapq.heappush(frontier, (priority, time+1, possible_next))
            seen_pairs.add((time+1, possible_next))

    frontier = []
    frontier.append((end_time_ichi, end_time_ichi, end_pos))
    heapq.heapify(frontier)
    # cost_so_far = dict()
    # cost_so_far[(start_pos, 0)] = 0
    seen_pairs = set()
    seen_pairs.add((end_time_ichi, end_pos))
    while len(frontier) > 0:
        priority, time, curr_pos = heapq.heappop(frontier)
        # print('from', curr_pos, priority, time, len(frontier))
        # print('checking out', curr_pos, 'with tentative score of', priority, 'at time', time)
        if (curr_pos[0], curr_pos[1]-1) == start_pos:
            # print(cost_so_far[curr_pos]+1)
            end_time_ni = time+1
            print('end_time_ni', end_time_ni)
            break
        for possible_next in possible_nexts(blizz_maps[(time+1)%repeating_interval], curr_pos, width, height, start_pos, end_pos):
            if (time+1, possible_next) in seen_pairs:
                continue
            # print('>', possible_next)
            # new_cost = cost_so_far[curr_pos]+1
            # if possible_next not in cost_so_far or new_cost < cost_so_far[possible_next]:
            # cost_so_far[possible_next] = new_cost
            priority = time+1 + heuristic(possible_next, end_pos)
            # print('pushing', possible_next)
            heapq.heappush(frontier, (priority, time+1, possible_next))
            seen_pairs.add((time+1, possible_next))

    frontier = []
    frontier.append((end_time_ni, end_time_ni, start_pos))
    heapq.heapify(frontier)
    # cost_so_far = dict()
    # cost_so_far[(start_pos, 0)] = 0
    seen_pairs = set()
    seen_pairs.add((end_time_ni, start_pos))
    while len(frontier) > 0:
        priority, time, curr_pos = heapq.heappop(frontier)
        # print('from', curr_pos, priority, time, len(frontier))
        # print('checking out', curr_pos, 'with tentative score of', priority, 'at time', time)
        if (curr_pos[0], curr_pos[1]+1) == end_pos:
            # print(cost_so_far[curr_pos]+1)
            end_time_san = time+1
            print('end_time_san', end_time_san)
            break
        for possible_next in possible_nexts(blizz_maps[(time+1)%repeating_interval], curr_pos, width, height, start_pos, end_pos):
            if (time+1, possible_next) in seen_pairs:
                continue
            # print('>', possible_next)
            # new_cost = cost_so_far[curr_pos]+1
            # if possible_next not in cost_so_far or new_cost < cost_so_far[possible_next]:
            # cost_so_far[possible_next] = new_cost
            priority = time+1 + heuristic(possible_next, end_pos)
            # print('pushing', possible_next)
            heapq.heappush(frontier, (priority, time+1, possible_next))
            seen_pairs.add((time+1, possible_next))

if __name__ == '__main__':
    s = time.time()
    main()
    print(time.time()-s) # 1.3609306812286377 for bfs & for 1.281069040298462 astar (full data)
    main2()
