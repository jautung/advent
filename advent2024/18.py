import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '18_dat.txt'
mapper = {}

def main():
    # GRID_SIZE = 6
    GRID_SIZE = 70

    def in_grid(x):
        return x[0] >= 0 and x[1] >= 0 and x[0] <= GRID_SIZE and x[1] <= GRID_SIZE

    data = readlines(FILENAME)
    data = [[int(f) for f in dat.split(',')] for dat in data]
    # print_2d(data)

    # DROPPED = 12
    DROPPED = 1024

    walls = [(x[0], x[1]) for x in data[:DROPPED]]
    # print_2d(walls)

    START = (0,0)
    END = (GRID_SIZE,GRID_SIZE)

    # bfs it
    dists = dict()
    dists[START] = 0
    queue = [START]
    in_queue = set()
    in_queue.add(START)
    while len(queue) > 0:
        curr = queue.pop(0)
        curr_dist = dists[curr]
        # if (curr[0] == 1 or curr[1] == 1) and curr_dist == 3:
        # print('curr', curr, curr_dist, queue)
        if curr == END:
            break
        neighbor_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        a = [add_tup(n,curr) for n in neighbor_dirs]
        a = [x for x in a if in_grid(x) and x not in walls and x not in in_queue]
        for x in a:
            in_queue.add(x)
            # print('- add', x)
            queue.append(x)
            dists[x] = curr_dist + 1
    # print_2d(dists)
    # for k in dists:
    #     print(k, dists[k])
    # for c in range(GRID_SIZE+1):
    #     for r in range(GRID_SIZE+1):
    #         if (r,c) in dists:
    #             assert (r,c) not in walls
    #             print(f"{dists[(r,c)]:3d}", end='')
    #         elif (r,c) in walls:
    #             print('  #', end='')
    #         else:
    #             print('  .', end='')
    #     print('\n', end='')
    print(dists[END])


def main2():
    # GRID_SIZE = 6
    GRID_SIZE = 70

    def in_grid(x):
        return x[0] >= 0 and x[1] >= 0 and x[0] <= GRID_SIZE and x[1] <= GRID_SIZE

    data = readlines(FILENAME)
    data = [[int(f) for f in dat.split(',')] for dat in data]
    # print_2d(data)

    # DROPPED = 12
    # DROPPED = 1024

    START = (0,0)
    END = (GRID_SIZE,GRID_SIZE)

    def have_path(DROPPED):
        walls = [(x[0], x[1]) for x in data[:DROPPED]]
        dists = dict()
        dists[START] = 0
        queue = [START]
        in_queue = set()
        in_queue.add(START)
        while len(queue) > 0:
            curr = queue.pop(0)
            curr_dist = dists[curr]
            # if (curr[0] == 1 or curr[1] == 1) and curr_dist == 3:
            # print('curr', curr, curr_dist, queue)
            if curr == END:
                return True
            neighbor_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            a = [add_tup(n,curr) for n in neighbor_dirs]
            a = [x for x in a if in_grid(x) and x not in walls and x not in in_queue]
            for x in a:
                in_queue.add(x)
                # print('- add', x)
                queue.append(x)
                dists[x] = curr_dist + 1
        return False
        # print_2d(dists)
        # for k in dists:
        #     print(k, dists[k])
        # for c in range(GRID_SIZE+1):
        #     for r in range(GRID_SIZE+1):
        #         if (r,c) in dists:
        #             assert (r,c) not in walls
        #             print(f"{dists[(r,c)]:3d}", end='')
        #         elif (r,c) in walls:
        #             print('  #', end='')
        #         else:
        #             print('  .', end='')
        #     print('\n', end='')
        # print(dists[END])

    # print(have_path(20))
    # print(have_path(21))

    # both inclusive
    assert have_path(0) == True
    assert have_path(len(data)) == False

    known_true = 0 
    known_false = len(data)
    while True:
        if known_true + 1 == known_false:
            last_true = known_true
            break
        middle = (known_true + known_false) // 2
        if have_path(middle):
            known_true = middle
        else:
            known_false = middle
    # print(last_true)
    print(','.join([str(i) for i in data[last_true]]))


if __name__ == '__main__':
    main()
    main2()
