import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '15_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)
    assert len(data) == 2
    grid = [[x for x in r] for r in data[0]]
    # print_2d(grid)
    moves = [a for a in ''.join(data[1])]
    # print(moves)

    robot = None
    walls = set()
    boxes = set()
    HEIGHT = len(grid)
    WIDTH = len(grid[0])
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid[row][col] == '@':
                assert robot is None
                robot = (row, col)
            elif grid[row][col] == '#':
                walls.add((row, col))
            elif grid[row][col] == 'O': 
                boxes.add((row, col))
            else:
                assert grid[row][col] == '.'
    assert robot is not None
    # print(robot)

    def make_move(robot, walls, boxes, movement):
        move_tup = None
        if movement == '<':
            move_tup = (0, -1)
        elif movement == '>':
            move_tup = (0, 1)
        elif movement == '^':
            move_tup = (-1, 0)
        elif movement == 'v':
            move_tup = (1, 0)
        else:
            assert False

        curr_pos = robot
        move_to = None
        while True:
            curr_pos = add_tup(curr_pos, move_tup)
            if curr_pos in walls:
                break # can't push
            elif curr_pos in boxes:
                continue # push starts, and may or may not complete
            else: # this means an empty space, so the push will complete, overflowing at 'curr_pos'
                move_to = curr_pos
                break
        if move_to is not None:
            initial_spot = add_tup(robot, move_tup)
            robot = initial_spot
            if move_to != robot: # a box was pushed to that spot
                boxes.remove(initial_spot)
                boxes.add(move_to)
        return robot, walls, boxes

    r = robot
    w = walls
    b = boxes
    for m in moves:
        # print(m)
        r, w, b = make_move(r, w, b, m)
        # print(r)
    # print('end')
    # print(r, w, b)
    def pretty_print(robot, walls, boxes):
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if (row, col) == robot:
                    print('@', end='')
                elif (row, col) in walls:
                    print('#', end='')
                elif (row, col) in boxes:
                    print('O', end='')
                else:
                    print('.', end='')
            print('\n', end='')


    # pretty_print(r, w, b)
    res = 0
    for b_i in b:
        res += b_i[0] * 100 + b_i[1]
    print(res)


def main2():
    data = readlines_split_by_newlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)
    assert len(data) == 2
    grid = [[x for x in r] for r in data[0]]
    # print_2d(grid)
    moves = [a for a in ''.join(data[1])]
    # print(moves)

    robot = None
    walls = set()
    boxes = set()
    HEIGHT = len(grid)
    WIDTH = len(grid[0])
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid[row][col] == '@':
                assert robot is None
                robot = (row, col * 2)
            elif grid[row][col] == '#':
                walls.add((row, col * 2))
                walls.add((row, col * 2 + 1))
            elif grid[row][col] == 'O': 
                boxes.add((row, col * 2)) # now always just stores the left side of the box
            else:
                assert grid[row][col] == '.'
    assert robot is not None
    def pretty_print(robot, walls, boxes):
        for row in range(HEIGHT):
            for col in range(WIDTH * 2):
                if (row, col) == robot:
                    print('@', end='')
                elif (row, col) in walls:
                    print('#', end='')
                elif (row, col) in boxes:
                    print('[', end='')
                elif (row, col-1) in boxes:
                    print(']', end='')
                else:
                    print('.', end='')
            print('\n', end='')
    # pretty_print(robot, walls, boxes)
    # print(walls)
    # print(boxes)

    def make_move(robot, walls, boxes, movement):
        move_tup = None
        if movement == '<':
            move_tup = (0, -1)
        elif movement == '>':
            move_tup = (0, 1)
        elif movement == '^':
            move_tup = (-1, 0)
        elif movement == 'v':
            move_tup = (1, 0)
        else:
            assert False

        # curr_pos = robot
        # move_to = None
        # while True:
        #     curr_pos = add_tup(curr_pos, move_tup)
        #     if curr_pos in walls:
        #         break # can't push
        #     elif curr_pos in boxes:
        #         continue # push starts, and may or may not complete
        #     else: # this means an empty space, so the push will complete, overflowing at 'curr_pos'
        #         move_to = curr_pos
        #         break
        # if move_to is not None:
        #     initial_spot = add_tup(robot, move_tup)
        #     robot = initial_spot
        #     if move_to != robot: # a box was pushed to that spot
        #         boxes.remove(initial_spot)
        #         boxes.add(move_to)
        potential_next = add_tup(robot, move_tup)
        if potential_next in walls:
            return robot, walls, boxes
        if potential_next not in walls and potential_next not in boxes and add_tup(potential_next, (0, -1)) not in boxes:
            # simple move to the spot, it's wide open!
            robot = potential_next
            return robot, walls, boxes
        
        all_checked_b_pos_ls = [] # needs to be ordered from root to leaf
        def can_move(b_pos_l, b_pos_r):
            # print(b_pos_l, b_pos_r)
            # exit(1)
            if b_pos_l in all_checked_b_pos_ls:
                return True # not strictly accurate, but not worth checking...
            all_checked_b_pos_ls.append(b_pos_l)
            new_l = add_tup(b_pos_l, move_tup)
            new_r = add_tup(b_pos_r, move_tup)
            if new_l in walls or new_r in walls:
                return False
            cascades = []
            if new_l in boxes:
                # print('a')
                cascades.append((new_l, add_tup(new_l, (0, 1))))
            elif (movement != '>') and add_tup(new_l, (0, -1)) in boxes:
                # print('b')
                cascades.append((add_tup(new_l, (0, -1)), new_l))
            if (movement != '<') and new_r in boxes:
                # print('c')
                cascades.append((new_r, add_tup(new_r, (0, 1))))
            elif add_tup(new_r, (0, -1)) in boxes:
                # print('d')
                cascades.append((add_tup(new_r, (0, -1)), new_r))
            assert len(cascades) >= 0 and len(cascades) <= 2
            if len(cascades) == 0:
                return True
            # print(cascades)
            # return False
            cascaded = [can_move(c[0], c[1]) for c in cascades]
            return all(cascaded)

        if potential_next in boxes:
            b_pos_l, b_pos_r = potential_next, add_tup(potential_next, (0, 1))
        elif add_tup(potential_next, (0, -1)) in boxes:
            b_pos_l, b_pos_r = add_tup(potential_next, (0, -1)), potential_next
        else:
            assert False
        if not can_move(b_pos_l, b_pos_r):
            return robot, walls, boxes

        robot = potential_next
        # print(boxes, all_checked_b_pos_ls)
        # print(all_checked_b_pos_ls, move_tup)
        for b_pos_l in reversed(all_checked_b_pos_ls): # needs to be ordered from leaf to root
            boxes.remove(b_pos_l)
            boxes.add(add_tup(b_pos_l, move_tup))
        return robot, walls, boxes

    r = robot
    w = walls
    b = boxes
    # assert len(b) == 21
    for m in moves:
        # print(m)
        r, w, b = make_move(r, w, b, m)
        # print(r)
        # pretty_print(r, w, b)
        # assert len(b) == 21
    # print('end')
    # print(r, w, b)


    # pretty_print(r, w, b)
    res = 0
    for b_i in b:
        res += b_i[0] * 100 + b_i[1]
    print(res)

if __name__ == '__main__':
    main()
    main2()
