import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '9_dat.txt'
mapper = {}

def main():
    data = readlines_split_each_line(FILENAME)
    # data = [dat.split() for dat in data]
    # print_2d(data)

    head_pos = (0,0)
    tail_pos = (0,0)

    def move_tail(head_pos, tail_pos):
        if tail_pos[0] == head_pos[0]:
            if abs(head_pos[1] - tail_pos[1]) == 2:
                direction = (head_pos[1] - tail_pos[1]) // abs(head_pos[1] - tail_pos[1])
                new_tail_pos_1 = tail_pos[1] + direction
                tail_pos = (tail_pos[0], new_tail_pos_1)
            else:
                return head_pos, tail_pos
        elif tail_pos[1] == head_pos[1]:
            if abs(head_pos[0] - tail_pos[0]) == 2:
                direction = (head_pos[0] - tail_pos[0]) // abs(head_pos[0] - tail_pos[0])
                new_tail_pos_0 = tail_pos[0] + direction
                tail_pos = (new_tail_pos_0, tail_pos[1])
            else:
                return head_pos, tail_pos
        else:
            if abs(head_pos[0] - tail_pos[0]) == 2 and abs(head_pos[1] - tail_pos[1]) == 2:
                direction_0 = (head_pos[0] - tail_pos[0]) // abs(head_pos[0] - tail_pos[0])
                new_tail_pos_0 = tail_pos[0] + direction_0
                direction_1 = (head_pos[1] - tail_pos[1]) // abs(head_pos[1] - tail_pos[1])
                new_tail_pos_1 = tail_pos[1] + direction_1
            if abs(head_pos[0] - tail_pos[0]) == 2:
                direction = (head_pos[0] - tail_pos[0]) // abs(head_pos[0] - tail_pos[0])
                new_tail_pos_0 = tail_pos[0] + direction
                new_tail_pos_1 = head_pos[1]
            elif abs(head_pos[1] - tail_pos[1]) == 2:
                direction = (head_pos[1] - tail_pos[1]) // abs(head_pos[1] - tail_pos[1])
                new_tail_pos_1 = tail_pos[1] + direction
                new_tail_pos_0 = head_pos[0]
            else:
                new_tail_pos_0, new_tail_pos_1 = tail_pos
            tail_pos = new_tail_pos_0, new_tail_pos_1
        return head_pos, tail_pos

    tail_poses = set()
    tail_poses.add(tail_pos)
    # print(head_pos, tail_pos)
    for dat in data:
        if dat[0] == 'L':
            for i in range(int(dat[1])):
                head_pos = add_tup(head_pos, (-1, 0))
                head_pos, tail_pos = move_tail(head_pos, tail_pos)
                tail_poses.add(tail_pos)
                # print(head_pos, tail_pos)
        elif dat[0] == 'R':
            for i in range(int(dat[1])):
                head_pos = add_tup(head_pos, (1, 0))
                head_pos, tail_pos = move_tail(head_pos, tail_pos)
                tail_poses.add(tail_pos)
                # print(head_pos, tail_pos)
        elif dat[0] == 'U':
            for i in range(int(dat[1])):
                head_pos = add_tup(head_pos, (0, 1))
                head_pos, tail_pos = move_tail(head_pos, tail_pos)
                tail_poses.add(tail_pos)
                # print(head_pos, tail_pos)
        elif dat[0] == 'D':
            for i in range(int(dat[1])):
                head_pos = add_tup(head_pos, (0, -1))
                head_pos, tail_pos = move_tail(head_pos, tail_pos)
                tail_poses.add(tail_pos)
                # print(head_pos, tail_pos)

    # print(tail_pos)
    # print(tail_poses)
    print(len(tail_poses))

def add_tup(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

def main2():
    data = readlines_split_each_line(FILENAME)
    # data = [dat.split() for dat in data]
    # print_2d(data)

    map_of_pos = {
        0: (0,0),
        1: (0,0),
        2: (0,0),
        3: (0,0),
        4: (0,0),
        5: (0,0),
        6: (0,0),
        7: (0,0),
        8: (0,0),
        9: (0,0),
    }

    def move_tail(head_pos, tail_pos):
        if tail_pos[0] == head_pos[0]:
            if abs(head_pos[1] - tail_pos[1]) == 2:
                direction = (head_pos[1] - tail_pos[1]) // abs(head_pos[1] - tail_pos[1])
                new_tail_pos_1 = tail_pos[1] + direction
                tail_pos = (tail_pos[0], new_tail_pos_1)
            else:
                return head_pos, tail_pos
        elif tail_pos[1] == head_pos[1]:
            if abs(head_pos[0] - tail_pos[0]) == 2:
                direction = (head_pos[0] - tail_pos[0]) // abs(head_pos[0] - tail_pos[0])
                new_tail_pos_0 = tail_pos[0] + direction
                tail_pos = (new_tail_pos_0, tail_pos[1])
            else:
                return head_pos, tail_pos
        else:
            if abs(head_pos[0] - tail_pos[0]) == 2 and abs(head_pos[1] - tail_pos[1]) == 2:
                direction_0 = (head_pos[0] - tail_pos[0]) // abs(head_pos[0] - tail_pos[0])
                new_tail_pos_0 = tail_pos[0] + direction_0
                direction_1 = (head_pos[1] - tail_pos[1]) // abs(head_pos[1] - tail_pos[1])
                new_tail_pos_1 = tail_pos[1] + direction_1
            elif abs(head_pos[0] - tail_pos[0]) == 2:
                direction = (head_pos[0] - tail_pos[0]) // abs(head_pos[0] - tail_pos[0])
                new_tail_pos_0 = tail_pos[0] + direction
                new_tail_pos_1 = head_pos[1]
            elif abs(head_pos[1] - tail_pos[1]) == 2:
                direction = (head_pos[1] - tail_pos[1]) // abs(head_pos[1] - tail_pos[1])
                new_tail_pos_1 = tail_pos[1] + direction
                new_tail_pos_0 = head_pos[0]
            else:
                new_tail_pos_0, new_tail_pos_1 = tail_pos
            tail_pos = new_tail_pos_0, new_tail_pos_1
        return head_pos, tail_pos

    tail_poses = set()
    tail_poses.add(map_of_pos[9])
    # print_with_grid(map_of_pos, 6)
    # print(map_of_pos[9])
    for dat in data:
        if dat[0] == 'L':
            for i in range(int(dat[1])):
                map_of_pos[0] = add_tup(map_of_pos[0], (-1, 0))
                for i in range(0, 9):
                    map_of_pos[i], map_of_pos[i+1] = move_tail(map_of_pos[i], map_of_pos[i+1])
                tail_poses.add(map_of_pos[9])
                # print_with_grid(map_of_pos, 6)
                # print(map_of_pos[9])
        elif dat[0] == 'R':
            for i in range(int(dat[1])):
                map_of_pos[0] = add_tup(map_of_pos[0], (1, 0))
                for i in range(0, 9):
                    map_of_pos[i], map_of_pos[i+1] = move_tail(map_of_pos[i], map_of_pos[i+1])
                tail_poses.add(map_of_pos[9])
                # print_with_grid(map_of_pos, 6)
                # print(map_of_pos[9])
        elif dat[0] == 'U':
            for i in range(int(dat[1])):
                map_of_pos[0] = add_tup(map_of_pos[0], (0, 1))
                for i in range(0, 9):
                    map_of_pos[i], map_of_pos[i+1] = move_tail(map_of_pos[i], map_of_pos[i+1])
                tail_poses.add(map_of_pos[9])
                # print_with_grid(map_of_pos, 6)
                # print(map_of_pos[9])
        elif dat[0] == 'D':
            for i in range(int(dat[1])):
                map_of_pos[0] = add_tup(map_of_pos[0], (0, -1))
                for i in range(0, 9):
                    map_of_pos[i], map_of_pos[i+1] = move_tail(map_of_pos[i], map_of_pos[i+1])
                tail_poses.add(map_of_pos[9])
                # print_with_grid(map_of_pos, 6)
                # print(map_of_pos[9])

    # print(tail_pos)
    # print(tail_poses)
    print(len(tail_poses))

def print_with_grid(map_of_pos, size):
    grid = [['.' for i in range(size)] for j in range(size)]
    for i in range(9, -1, -1):
        pos = map_of_pos[i]
        grid[pos[0]][pos[1]] = str(i) if i != 0 else 'H'
    print_2d(transpose(grid))

if __name__ == '__main__':
    main()
    main2()
