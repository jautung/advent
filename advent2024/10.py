import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '10_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(x) if x != '.' else '.' for x in dat] for dat in data]
    # print_2d(data)
    zero_pos = set()
    HEIGHT = len(data)
    WIDTH = len(data[0])
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if data[row][col] == 0:
                zero_pos.add((row, col))
    # print(zero_pos)

    def is_in_board(tup):
        return tup[0] >= 0 and tup[1] >= 0 and tup[0] < HEIGHT and tup[1] < WIDTH

    # number_of_ways_to_end = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]
    # # def number_of_ways_to_reach_end(row, col):

    # # print_2d(number_of_ways_to_end)
    # # filling_in_for_height = 9
    # for filling_in_for_height in range(9, -1, -1):
    #     print_2d(number_of_ways_to_end)
    #     for row in range(HEIGHT):
    #         for col in range(WIDTH):
    #             if data[row][col] == 9:
    #                 number_of_ways_to_end[row][col] = 1
    #                 continue
    #             else:
    #                 current_height = data[row][col]
    #                 if current_height != filling_in_for_height:
    #                     continue
    #                 neighbors_with_one_higher = [n for n in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)] if is_in_board(n) and data[n[0]][n[1]] == current_height+1]
    #                 ways = 0
    #                 for n in neighbors_with_one_higher:
    #                     next_num_ways = number_of_ways_to_end[n[0]][n[1]]
    #                     # print(n)
    #                     assert next_num_ways is not None
    #                     ways += next_num_ways
    #                 number_of_ways_to_end[row][col] = ways

    # print_2d(number_of_ways_to_end)
    def bfs_from_point(pos):
        seen = set()
        nine_pos = set()
        queue = [pos]
        while len(queue) > 0:
            curr = queue.pop()
            if curr in seen:
                continue
            seen.add(curr)
            row, col = curr
            curr_height = data[row][col]
            if curr_height == 9:
                nine_pos.add(curr)
            neighbors_with_one_higher = [n for n in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)] if is_in_board(n) and data[n[0]][n[1]] == curr_height+1]
            queue += neighbors_with_one_higher
        # print(seen)
        # print(nine_pos)
        return len(nine_pos)

    # for z in zero_pos:
    #     print(z, bfs_from_point(z))

    ret = 0
    for z in zero_pos:
        ret += bfs_from_point(z)
    print(ret)


def main2():
    data = readlines(FILENAME)
    data = [[int(x) if x != '.' else '.' for x in dat] for dat in data]
    # print_2d(data)
    zero_pos = set()
    HEIGHT = len(data)
    WIDTH = len(data[0])
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if data[row][col] == 0:
                zero_pos.add((row, col))
    # print(zero_pos)

    def is_in_board(tup):
        return tup[0] >= 0 and tup[1] >= 0 and tup[0] < HEIGHT and tup[1] < WIDTH

    number_of_ways_to_end = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]
    # def number_of_ways_to_reach_end(row, col):

    # print_2d(number_of_ways_to_end)
    # filling_in_for_height = 9
    for filling_in_for_height in range(9, -1, -1):
        # print_2d(number_of_ways_to_end)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if data[row][col] == 9:
                    number_of_ways_to_end[row][col] = 1
                    continue
                else:
                    current_height = data[row][col]
                    if current_height != filling_in_for_height:
                        continue
                    neighbors_with_one_higher = [n for n in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)] if is_in_board(n) and data[n[0]][n[1]] == current_height+1]
                    ways = 0
                    for n in neighbors_with_one_higher:
                        next_num_ways = number_of_ways_to_end[n[0]][n[1]]
                        # print(n)
                        assert next_num_ways is not None
                        ways += next_num_ways
                    number_of_ways_to_end[row][col] = ways

    # print_2d(number_of_ways_to_end)

    ret = 0
    for z in zero_pos:
        ret += number_of_ways_to_end[z[0]][z[1]]
    print(ret)

if __name__ == '__main__':
    main()
    main2()
