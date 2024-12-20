import sys 
sys.path.append('..')

import copy
from collections import defaultdict, Counter
from helper import *

FILENAME = '20_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[x for x in dat] for dat in data]
    # print_2d(data)

    HEIGHT = len(data)
    WIDTH = len(data[0])

    walls = set()
    start = None
    end = None
    for r in range(HEIGHT):
        for c in range(WIDTH):
            coord = (r,c)
            if data[r][c] == '#':
                walls.add(coord)
            elif data[r][c] == 'S':
                start = coord
            elif data[r][c] == 'E':
                end = coord
            else:
                assert data[r][c] == '.'
    # print(walls)

    def inside(c):
        return c[0] >= 0 and c[1] >= 0 and c[0] < HEIGHT and c[1] < WIDTH

    def bfs(walls, start, end, constrained_gl_1=None, constrained_gl_2=None):
        in_queue = set()
        in_queue.add(start)
        queue = [(start, 0)]
        while len(queue) > 0:
            curr = queue.pop(0)
            curr, curr_p = curr
            if curr == constrained_gl_1:
                neighs = [constrained_gl_2]
            else:
                n_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
                neighs = [add_tup(n, curr) for n in n_dirs]
                neighs = [n for n in neighs if inside(n) and n not in in_queue and (n not in walls or n == constrained_gl_1)]
            for n in neighs:
                if n == end:
                    # print('yay')
                    return curr_p + 1
                in_queue.add(n)
                queue.append((n, curr_p + 1))

    time = bfs(walls, start, end)
    # print(time)

    res = dict()

    for r in range(HEIGHT):
        # print(r, 'of', HEIGHT, 'horz')
        for c in range(WIDTH-1):
            if r == 0 or c == 0 or r == HEIGHT-1 or c+1 == WIDTH-1:
                continue # not going to help
            pair_left = (r,c)
            pair_right = (r,c+1)
            if pair_left in walls and pair_right not in walls:
                # left to right glitch
                res[(pair_left, pair_right)] = bfs(walls, start, end, pair_left, pair_right)
            elif pair_left not in walls and pair_right in walls:
                # right to right glitch
                res[(pair_right, pair_left)] = bfs(walls, start, end, pair_right, pair_left)

    for r in range(HEIGHT-1):
        # print(r, 'of', HEIGHT, 'col')
        for c in range(WIDTH):
            if r == 0 or c == 0 or r+1 == HEIGHT-1 or c == WIDTH-1:
                continue # not going to help
            pair_top = (r,c)
            pair_bot = (r+1,c)
            if pair_top in walls and pair_bot not in walls:
                # top to bot
                res[(pair_top, pair_bot)] = bfs(walls, start, end, pair_top, pair_bot)
            if pair_top not in walls and pair_bot in walls:
                # bot to top
                res[(pair_bot, pair_top)] = bfs(walls, start, end, pair_bot, pair_top)

    for k in res:
        print(k, res[k])
    print(sorted([time - res[k] for k in res if res[k] is not None]))

    # c = Counter()
    # for k in res:
    #     if res[k] is not None:
    #         c[time - res[k]] += 1
    # for k in c:
    #     print(c[k], k)

    # for k in res:
    #     if res[k] is not None and time - res[k] == 64:
    #         print(k, res[k])

    x = 0
    for k in res:
        if res[k] is not None and time - res[k] >= 100:
            x += 1
    print('end')
    print(x)


def main2(GLITCH_D):
    data = readlines(FILENAME)
    data = [[x for x in dat] for dat in data]
    # print_2d(data)

    HEIGHT = len(data)
    WIDTH = len(data[0])

    walls = set()
    start = None
    end = None
    for r in range(HEIGHT):
        for c in range(WIDTH):
            coord = (r,c)
            if data[r][c] == '#':
                walls.add(coord)
            elif data[r][c] == 'S':
                start = coord
            elif data[r][c] == 'E':
                end = coord
            else:
                assert data[r][c] == '.'
    # print(walls)

    def inside(c):
        return c[0] >= 0 and c[1] >= 0 and c[0] < HEIGHT and c[1] < WIDTH


    def bfs(walls, start, end, constrained_gl_1=None, constrained_gl_2=None):
        in_queue = set()
        in_queue.add(start)
        queue = [(start, 0)]
        while len(queue) > 0:
            curr = queue.pop(0)
            curr, curr_p = curr
            if curr == constrained_gl_1:
                neighs = [constrained_gl_2]
            else:
                n_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
                neighs = [add_tup(n, curr) for n in n_dirs]
                neighs = [n for n in neighs if inside(n) and n not in in_queue and (n not in walls or n == constrained_gl_1)]
            for n in neighs:
                if n == end:
                    # print('yay')
                    return curr_p + 1
                in_queue.add(n)
                queue.append((n, curr_p + 1))

    time = bfs(walls, start, end)

    def explore(walls, start):
        in_queue = set()
        in_queue.add(start)
        queue = [(start, 0)]
        distances = dict() # distance of each square from the start
        distances[start] = 0
        while len(queue) > 0:
            curr = queue.pop(0)
            curr, curr_p = curr
            n_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            neighs = [add_tup(n, curr) for n in n_dirs]
            neighs = [n for n in neighs if inside(n) and n not in in_queue and (n not in walls)]
            for n in neighs:
                in_queue.add(n)
                queue.append((n, curr_p + 1))
                distances[n] = curr_p + 1
        return distances

    # print(time)
    d_start = explore(walls, start)
    d_end = explore(walls, end)

    # print(d_start)
    # print(d_end)

    # GLITCH_D = 2
    # GLITCH_D = 20
    # SAVING = 50
    SAVING = 100
    target = time - SAVING

    c = 0
    kk = Counter()
    for i, teleport_start in enumerate(d_start):
        # if i % 100 == 0:
        #     print(i, 'of', len(d_start))
        incurred = d_start[teleport_start]
        if incurred > target:
            continue
        for e in d_end:
            m = manhattan(teleport_start, e)
            picos = incurred + m + d_end[e]
            if m <= GLITCH_D and picos <= target:
                c += 1
                kk[picos] += 1
        # c += len(eligible_ends)
    print(c)
    # print(kk)

    # NOT 891009

    # for key, value in sorted(kk.items(), reverse=True):
    #     print(value, time-key)


if __name__ == '__main__':
    # main()
    main2(GLITCH_D=2)
    main2(GLITCH_D=20)
