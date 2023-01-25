import sys 
sys.path.append('..')

import copy
import itertools
import time
from collections import defaultdict
from helper import *

FILENAME = '16_dat.txt'
mapper = {}

def parse(dat):
    name = dat[1]
    flow_rate = int(dat[4].split('=')[1][:-1])
    leads = [line.strip(',') for line in dat[9:]]

    return name, flow_rate, leads

def main():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    neighbor_map = dict()
    for d in data:
        neighbor_map[d[0]] = d[2]
    # print(neighbor_map)

    pressure_map = dict()
    for d in data:
        pressure_map[d[0]] = d[1]

    assert(len(pressure_map) == len(neighbor_map))
    assert(len(pressure_map) == len(data))
    NUM_TOT = sum([dat[1] > 0 for dat in data])

    # print(NUM_TOT)
    # print(len(data))
    # print(len(data) * (2**NUM_TOT))

    relevant_nodes = list(filter(lambda x: x != None, [dat[0] if dat[1] > 0 else None for dat in data]))
    # print(relevant_nodes)
    shortest_paths = dict()

    # print(relevant_nodes[0])
    # search_from(relevant_nodes[0], neighbor_map)
    for na in relevant_nodes + ['AA']:
        distances = search_from(na, neighbor_map)
        for nb in relevant_nodes:
            shortest_paths[(na, nb)] = distances[nb]
    # for i in shortest_paths.items():
    #     print(i)
    # print(len(relevant_nodes))

    TIME = 30
    # print(len(relevant_nodes))


    # GREEDY
    # def next_node_usefulness(curr_time, curr_pos, next_pos):
    #     new_time = curr_time + shortest_paths[(curr_pos, next_pos)] + 1
    #     potential = (TIME-new_time) * pressure_map[next_pos]
    #     return potential

    # curr_time = 0
    # curr_pos = 'AA'
    # rel_nodes_left = set(relevant_nodes)
    # score = 0
    # # real = ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']
    # while len(rel_nodes_left) > 0:
    #     choice = sorted([(next_node_usefulness(curr_time, curr_pos, n), n) for n in rel_nodes_left], reverse=True)[0][1]
    #     # choice = real[6-len(rel_nodes_left)]
    #     curr_time += shortest_paths[(curr_pos, choice)] + 1
    #     if curr_time >= TIME:
    #         break
    #     curr_pos = choice
    #     # print(rel_nodes_left, choice)
    #     rel_nodes_left = rel_nodes_left.difference([choice])
    #     score += (TIME-curr_time) * pressure_map[choice]
    # print(score)


    # EXHAUSTIVE
    # curr_max = None
    # # step = 0
    # for perm in itertools.permutations(relevant_nodes):
    #     # if step % 100000 == 0:
    #     #     print(step, 'out of 130767436800')
    #     order = ['AA'] + list(perm)
    #     pairs = [tuple(order[i:i+2]) for i in range(len(order)-1)]
    #     # print(order)
    #     # print(pairs)
    #     costs = [shortest_paths[pair] for pair in pairs]
    #     # print(costs)
    #     cum_costs = [sum(costs[:i+1])+i for i in range(len(costs))]
    #     # print(cum_costs)
    #     open_time = [TIME-i-1 for i in cum_costs]
    #     efficiency = [pressure_map[i] for i in perm]
    #     # print(perm)
    #     # print(efficiency)
    #     # print(open_time)
    #     assert(len(efficiency) == len(open_time))
    #     total = sum([efficiency[i]*open_time[i] for i in range(len(efficiency))])
    #     if curr_max == None or total > curr_max:
    #         # print(curr_max)
    #         curr_max = total
    #     # step += 1
    #     # exit()
    # print(curr_max)


    # DUMB
    # paths = [(0, 'AA', set(), 0)]
    # curr_max = None
    # i = 0
    # while len(paths) > 0:
    #     # if i % 10000 == 0:
    #     #     print(i, len(paths))
    #     curr_time, curr_pos, curr_opened, curr_score = paths.pop()
    #     if curr_time == TIME or len(curr_opened) == NUM_TOT:
    #         if curr_max == None or curr_score > curr_max:
    #             print(curr_max)
    #             curr_max = curr_score
    #     else:
    #         if curr_pos not in curr_opened and pressure_map[curr_pos] > 0: # open this one
    #             paths.append((curr_time+1, curr_pos, set().union(curr_opened).union([curr_pos]), curr_score+pressure_map[curr_pos]*(TIME-curr_time-1)))
    #         for n in neighbor_map[curr_pos]:
    #             paths.append((curr_time+1, n, set().union(curr_opened), curr_score))
    #     i += 1
    #     # print(paths)
    #     # exit()
    # print(curr_max)


    # DP
    dp_res = dict() # keyed by (frozenset_rel_nodes_left, current_pos, current_time) -> best score that can be gained from this point forward
    for n_rel_nodes_left in range(len(relevant_nodes)+1):
        # print(n_rel_nodes_left)
        for rel_nodes_left in itertools.combinations(relevant_nodes, n_rel_nodes_left):
            for curr_pos in ['AA'] + relevant_nodes:
                for curr_time in range(TIME, -1, -1):
                    if curr_pos in rel_nodes_left:
                        continue
                    this_key = (frozenset(rel_nodes_left), curr_pos, curr_time)
                    # print(n_rel_nodes_left, this_key)
                    if len(rel_nodes_left) == 0:
                        this_val = 0
                    else:
                        this_val = 0
                        for next_node in rel_nodes_left:
                            new_time = curr_time+shortest_paths[(curr_pos, next_node)]+1
                            if new_time > TIME:
                                continue
                            # print(set(rel_nodes_left)-set([next_node]), set(rel_nodes_left), set([next_node]))
                            choice = (frozenset(set(rel_nodes_left)-set([next_node])), next_node, new_time)
                            score_for_single_move = (TIME-new_time)*pressure_map[next_node]
                            candidate = score_for_single_move + dp_res[choice]
                            if candidate > this_val:
                                this_val = candidate
                    dp_res[this_key] = this_val
                    # print(this_val)
                    # print(this_key, this_val)
    print(dp_res[frozenset(relevant_nodes), 'AA', 0])

def search_from(node, neighbor_map):
    paths = [(node, 0)]
    nodes_seen = dict()
    # nodes_seen[node] = 0
    while len(paths) > 0:
        curr_node, curr_dist = paths.pop(0)
        nodes_seen[curr_node] = curr_dist
        for neighbor in neighbor_map[curr_node]:
            if neighbor in nodes_seen:
                continue
            paths.append((neighbor, curr_dist+1))
    return nodes_seen

def main2():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)

    neighbor_map = dict()
    for d in data:
        neighbor_map[d[0]] = d[2]
    # print(neighbor_map)

    pressure_map = dict()
    for d in data:
        pressure_map[d[0]] = d[1]

    assert(len(pressure_map) == len(neighbor_map))
    assert(len(pressure_map) == len(data))
    NUM_TOT = sum([dat[1] > 0 for dat in data])

    # print(NUM_TOT)
    # print(len(data))
    # print(len(data) * (2**NUM_TOT))

    relevant_nodes = list(filter(lambda x: x != None, [dat[0] if dat[1] > 0 else None for dat in data]))
    # print(relevant_nodes)
    shortest_paths = dict()

    # print(relevant_nodes[0])
    # search_from(relevant_nodes[0], neighbor_map)
    for na in relevant_nodes + ['AA']:
        distances = search_from(na, neighbor_map)
        for nb in relevant_nodes:
            shortest_paths[(na, nb)] = distances[nb]
    # for i in shortest_paths.items():
    #     print(i)
    # print(len(relevant_nodes))

    TIME = 26
    # print(len(relevant_nodes))

    you_and_elephant = []
    for pattern in itertools.product([True,False], repeat=len(relevant_nodes)):
        you_and_elephant.append(([x[1] for x in zip(pattern,relevant_nodes) if x[0]], [x[1] for x in zip(pattern,relevant_nodes) if not x[0]]))
    # print_2d(you_and_elephant)

    # DP
    # cached_answers = dict()
    # def do_sub_dp(relevant_nodes):
    #     # print(relevant_nodes)
    #     if frozenset(relevant_nodes) in cached_answers:
    #         return cached_answers[frozenset(relevant_nodes)]
    dp_res = dict() # keyed by (frozenset_rel_nodes_left, current_pos, current_time) -> best score that can be gained from this point forward
    for n_rel_nodes_left in range(len(relevant_nodes)+1):
        # print(n_rel_nodes_left)
        for rel_nodes_left in itertools.combinations(relevant_nodes, n_rel_nodes_left):
            for curr_pos in ['AA'] + relevant_nodes:
                for curr_time in range(TIME, -1, -1):
                    if curr_pos in rel_nodes_left:
                        continue
                    this_key = (frozenset(rel_nodes_left), curr_pos, curr_time)
                    # print(n_rel_nodes_left, this_key)
                    if len(rel_nodes_left) == 0:
                        this_val = 0
                    else:
                        this_val = 0
                        for next_node in rel_nodes_left:
                            new_time = curr_time+shortest_paths[(curr_pos, next_node)]+1
                            if new_time > TIME:
                                continue
                            # print(set(rel_nodes_left)-set([next_node]), set(rel_nodes_left), set([next_node]))
                            choice = (frozenset(set(rel_nodes_left)-set([next_node])), next_node, new_time)
                            score_for_single_move = (TIME-new_time)*pressure_map[next_node]
                            candidate = score_for_single_move + dp_res[choice]
                            if candidate > this_val:
                                this_val = candidate
                    dp_res[this_key] = this_val
                    # print(this_val)
                    # print(this_key, this_val)
        # print(dp_res[frozenset(relevant_nodes), 'AA', 0])
        # cached_answers[frozenset(relevant_nodes)] = dp_res[frozenset(relevant_nodes), 'AA', 0]
        # return dp_res[frozenset(relevant_nodes), 'AA', 0]

    ans = 0
    for partition in you_and_elephant:
        cand = dp_res[frozenset(partition[0]), 'AA', 0] + dp_res[frozenset(partition[1]), 'AA', 0]
        # print(partition, cand)
        if cand > ans:
            ans = cand
    print(ans)

if __name__ == '__main__':
    # s = time.time()
    main()
    # print(time.time() - s)
    # for small input
    # greedy is 0.00030803680419921875 (but wrong)
    # exhaustive is 0.004755258560180664
    # DP is 0.024801015853881836

    # for real input
    # exhaustive never finishes...
    # DP is 79.2490770816803

    # s = time.time()
    main2()
    # print(time.time() - s)
    # for small input
    # DP is 0.028126001358032227
    # for real input
    # DP is 63.39560413360596
