import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '19_dat.txt'
mapper = {}

def parse(dat):
    blueprint_id = int(dat[1][:-1])
    ore_robot_cost = int(dat[6])
    clay_robot_cost = int(dat[12])
    obsedian_robot_cost = (int(dat[18]), int(dat[21]))
    geode_robot_cost = (int(dat[27]), int(dat[30]))
    return blueprint_id, ore_robot_cost, clay_robot_cost, obsedian_robot_cost, geode_robot_cost

def main():
    data = readlines_split_each_line(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)
    MAX_TIME = 24

    blueprint_id, ore_robot_cost, clay_robot_cost, obsedian_robot_cost, geode_robot_cost = data[0]

    # PROBABLY A DUMB BFS IDEA
    # bounding_superior_paths = set()
    # def try_append(paths, path, bounding_superior_paths):
    #     for b in bounding_superior_paths:
    #         if geq_superior_path(b, path):
    #             # print('skipping!')
    #             return
    #     to_remove = set()
    #     for b in bounding_superior_paths:
    #         if geq_superior_path(path, b):
    #             to_remove.add(b)
    #     bounding_superior_paths.add(path)
    #     bounding_superior_paths = bounding_superior_paths - to_remove
    #     paths.append(path)

    # max_geodes_opened = None
    # MAX_TIME = 24
    # paths = [(0,(1,0,0,0),(0,0,0),0)] # time, robots, material, geode_count
    # bounding_superior_paths.add(paths[0])
    # while len(paths) > 0:
    #     t, robot_count, material_count, geode_count = paths.pop()
    #     # print(t, robot_count, material_count, geode_count)
    #     # print(len(paths))
    #     if t == MAX_TIME:
    #         # print('ended with', robot_count, material_count, geode_count)
    #         if max_geodes_opened == None or geode_count > max_geodes_opened:
    #             print('new found max', geode_count, len(paths), len(bounding_superior_paths))
    #             # if geode_count == 4:
    #             #     print_2d(sorted(bounding_superior_paths))
    #             #     exit()
    #             max_geodes_opened = geode_count
    #         continue
    #     ore_robot_count, clay_robot_count, obsedian_robot_count, geode_robot_count = robot_count

    #     ore_count, clay_count, obsedian_count = material_count
    #     for build in all_possible_builds(material_count, ore_robot_cost, clay_robot_cost, obsedian_robot_cost, geode_robot_cost):
    #         new_time = t+1
    #         new_robots_count = add_tup_robots(robot_count, build[0])
    #         new_mat_count = add_tup_mat(material_count, (ore_robot_count, clay_robot_count, obsedian_robot_count))
    #         new_mat_count = add_tup_mat(new_mat_count, scale_tup(build[1], -1))
    #         new_geode_count = geode_count+geode_robot_count
    #         new_path = (new_time, new_robots_count, new_mat_count, new_geode_count)
    #         try_append(paths, new_path, bounding_superior_paths)
    # # print('done!')
    # print(max_geodes_opened)

    # ANOTHER DUMB BFS IDEA?
    # so i hear this is a bfs problem with a lot of pruning / heuristics / optimization
    MAX_TIME = 24
    paths = []
    paths.append((0,(1,0,0,0),(0,0,0,0))) # time, robots, material
    while len(paths) > 0:
        t, robot_count, material_count = paths.pop()

        t_duration = step_until_can_create_ore_robot(robot_count, material_count, ore_robot_cost) # step enough times (maybe 0) to create ore robot
        # print(t_duration)
        new_material_count = (material_count[0]+robot_count[0]*t_duration, material_count[1]+robot_count[1]*t_duration, material_count[2]+robot_count[2]*t_duration, material_count[3]+robot_count[3]*t_duration)
        # print(new_material_count)
        new_material_count = (new_material_count[0]-ore_robot_cost, new_material_count[1], new_material_count[2], new_material_count[3])
        # print(new_material_count)
        # print()
        new_robot_count = (robot_count[0]+1, robot_count[1], robot_count[2], robot_count[3])
        if t+t_duration < MAX_TIME:
            paths.append((t+t_duration+1, new_robot_count, new_material_count))
            # print('a')
            print('added', t+t_duration+1, new_robot_count, new_material_count)
    # ok this is wrong and i really can't be bothered to correct it anymore byee

def step_until_can_create_ore_robot(robot_count, material_count, ore_robot_cost):
    if material_count[0] >= ore_robot_cost:
        return 0
    return math.ceil((ore_robot_cost - material_count[0]) / robot_count[0])

# def geq_superior_path(a, b):
#     return a[0]<=b[0] and tup_geq_robots(a[1],b[1]) and tup_geq(a[2],b[2]) and a[3]>=b[3]

# def add_tup_robots(a,b):
#     return (a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3])

# def add_tup_mat(a,b):
#     return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

# # returns (robot-4-tup, cost-3-tup)
# def all_possible_builds(material_count, ore_robot_cost, clay_robot_cost, obsedian_robot_cost, geode_robot_cost):
#     max_ore_robots_possible = max_copies(material_count, ore_robot_cost)
#     max_clay_robots_possible = max_copies(material_count, clay_robot_cost)
#     max_obsedian_robots_possible = max_copies(material_count, obsedian_robot_cost)
#     max_geode_robots_possible = max_copies(material_count, geode_robot_cost)
#     # print(max_ore_robots_possible, max_clay_robots_possible, max_obsedian_robots_possible, max_geode_robots_possible)

#     res = []
#     for o in range(max_ore_robots_possible+1):
#         for c in range(max_clay_robots_possible+1):
#             for ob in range(max_obsedian_robots_possible+1):
#                 for g in range(max_geode_robots_possible+1):
#                     x = scale_tup(ore_robot_cost, o)
#                     y = scale_tup(clay_robot_cost, c)
#                     z = scale_tup(obsedian_robot_cost, ob)
#                     w = scale_tup(geode_robot_cost, g)
#                     total_cost = add_tup_mat(x,add_tup_mat(y,add_tup_mat(z,w)))
#                     if tup_geq(material_count, total_cost):
#                         res.append(((o,c,ob,g),total_cost))
#     # print('all_possible_builds', res)
#     return res

# def max_copies(material_count, cost):
#     copies = 0
#     while True:
#         if not tup_geq(material_count, scale_tup(cost, copies)):
#             return copies-1
#         copies += 1

# def scale_tup(a, s):
#     return (s*a[0],s*a[1],s*a[2])

# def tup_geq_robots(a, b):
#     return a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2] and a[3] >= b[3]

# def tup_geq(a, b):
#     return a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2]

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

if __name__ == '__main__':
    main()
    main2()
