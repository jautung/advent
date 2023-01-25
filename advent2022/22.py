import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '22_dat.txt'
mapper = {}

DIRS = [ # forward is R, backward is L
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
]
DIR_TO_READABLE = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U',
}
READABLE_TO_DIR = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3,
}

def pad_row(row, max_len):
    return row + [' '] * (max_len - len(row))

def main():
    data = readlines_split_by_newlines(FILENAME)
    grid = [list(dat) for dat in data[0]]
    max_len = max([len(i) for i in grid])
    grid = [pad_row(row, max_len) for row in grid]
    instr = data[1][0]
    # print_2d(grid)
    # print(instr)

    curr_pos = find_start_pos(grid)
    curr_dir = 0
    while True:
        # print('curr_pos:', curr_pos, '; curr_dir:', DIRS[curr_dir])
        # print('curr_pos:', curr_pos, '; curr_dir:', curr_dir)
        step, instr = parse_instr(instr)
        if step == None and instr == None:
            break
        # print(step)
        curr_pos, curr_dir = conduct_step(step, curr_pos, curr_dir, grid)
    # print('curr_pos:', curr_pos, '; curr_dir:', DIRS[curr_dir])
    # print('curr_pos:', curr_pos, '; curr_dir:', curr_dir)
    row = curr_pos[1]+1
    col = curr_pos[0]+1
    # print(row,col,curr_dir)
    print(1000*row+4*col+curr_dir)

def conduct_step(step, curr_pos, curr_dir, grid):
    if step == 'L':
        return curr_pos, (curr_dir-1)%4
    if step == 'R':
        return curr_pos, (curr_dir+1)%4
    for _ in range(step):
        new_curr_pos = conduct_mini_step(curr_pos, curr_dir, grid)
        # print('> curr_pos:', curr_pos, '; curr_dir:', DIRS[curr_dir])
        # print('> curr_pos:', curr_pos, '; curr_dir:', curr_dir)
        if new_curr_pos == curr_pos:
            break
        curr_pos = new_curr_pos
    return curr_pos, curr_dir

def conduct_mini_step(curr_pos, curr_dir, grid):
    orig_pos = curr_pos
    while True:
        # print(len(grid[0]), len(grid))
        new_curr_pos = add_tup(curr_pos, DIRS[curr_dir], len(grid[0]), len(grid))
        # print(curr_pos, new_curr_pos)
        if grid[new_curr_pos[1]][new_curr_pos[0]] == '#':
            return orig_pos
        if grid[new_curr_pos[1]][new_curr_pos[0]] == '.':
            return new_curr_pos
        curr_pos = new_curr_pos

def add_tup(a, b, mod_x, mod_y):
    return ((a[0] + b[0]) % mod_x, (a[1] + b[1]) % mod_y)

def find_start_pos(grid):
    return (grid[0].index('.'), 0)

def parse_instr(i):
    if len(i) == 0:
        return None, None
    if i[0] == 'L':
        return 'L', i[1:]
    if i[0] == 'R':
        return 'R', i[1:]
    if len(i) == 1:
        return int(i[0]), ''
    for idx in range(1, len(i)):
        # print(idx)
        try:
            int(i[:idx])
        except:
            break
    return int(i[:idx-1]), i[idx-1:]

# def HARD_CODE_REGIONS_MINI(pos):
#     # print(pos)
#     sector = (int(pos[0]/4),int(pos[1]/4))
#     # print(sector)
#     match sector:
#         case 2,0:
#             return 1
#         case 0,1:
#             return 2
#         case 1,1:
#             return 3
#         case 2,1:
#             return 4
#         case 2,2:
#             return 5
#         case 3,2:
#             return 6
#     assert(False)
#     return None

# def HARD_CODE_JOINS_MINI(zone, curr_dir): # returns new region
#     match zone, curr_dir:
#         case 1,0: # right
#             return 6
#         case 1,1: # down
#             return 4
#         case 1,2: # left
#             return 3
#         case 1,3: # up
#             return 2

#         case 2,0: # right
#             return 3
#         case 2,1: # down
#             return 5
#         case 2,2: # left
#             return 6
#         case 2,3: # up
#             return 1

#         case 3,0: # right
#             return 4
#         case 3,1: # down
#             return 5
#         case 3,2: # left
#             return 2
#         case 3,3: # up
#             return 1

#         case 4,0: # right
#             return 6
#         case 4,1: # down
#             return 5
#         case 4,2: # left
#             return 3
#         case 4,3: # up
#             return 1

#         case 5,0: # right
#             return 6
#         case 5,1: # down
#             return 2
#         case 5,2: # left
#             return 3
#         case 5,3: # up
#             return 4

#         case 6,0: # right
#             return 1
#         case 6,1: # down
#             return 2
#         case 6,2: # left
#             return 5
#         case 6,3: # up
#             return 4

def main2():
    # USE_MINI = True

    data = readlines_split_by_newlines(FILENAME)
    grid = [list(dat) for dat in data[0]]
    max_len = max([len(i) for i in grid])
    grid = [pad_row(row, max_len) for row in grid]
    instr = data[1][0]
    # print_2d(grid)
    # print(instr)

    curr_pos = find_start_pos(grid)
    hard_code_cache = dict()
    hard_code_cache['SECTOR_SIZE'] = int(input('what is sector size: '))
    # print(HARD_CODE_REGIONS_MINI(curr_pos))
    curr_dir = 0
    while True:
        # print('curr_pos:', curr_pos, '; curr_dir:', DIRS[curr_dir])
        # print('curr_pos:', curr_pos, '; curr_dir:', DIR_TO_READABLE[curr_dir])
        step, instr = parse_instr(instr)
        if step == None and instr == None:
            break
        # print(step)
        curr_pos, curr_dir = conduct_step_2(step, curr_pos, curr_dir, grid, hard_code_cache)
    # print('curr_pos:', curr_pos, '; curr_dir:', DIRS[curr_dir])
    # print('curr_pos:', curr_pos, '; curr_dir:', curr_dir)
    row = curr_pos[1]+1
    col = curr_pos[0]+1
    # print(row,col,curr_dir)
    print(1000*row+4*col+curr_dir)

def conduct_step_2(step, curr_pos, curr_dir, grid, hard_code_cache):
    if step == 'L':
        return curr_pos, (curr_dir-1)%4
    if step == 'R':
        return curr_pos, (curr_dir+1)%4
    for _ in range(step):
        # print('> curr_pos:', curr_pos, '; curr_dir:', DIR_TO_READABLE[curr_dir])
        new_curr_pos, new_curr_dir = conduct_mini_step_2(curr_pos, curr_dir, grid, hard_code_cache)
        # print('> curr_pos:', curr_pos, '; curr_dir:', DIRS[curr_dir])
        if new_curr_pos == curr_pos:
            break
        curr_pos = new_curr_pos
        curr_dir = new_curr_dir
    return curr_pos, curr_dir

def conduct_mini_step_2(curr_pos, curr_dir, grid, hard_code_cache):
    SECTOR_SIZE = hard_code_cache['SECTOR_SIZE']

    orig_pos = curr_pos
    curr_sector = (int(curr_pos[0]/SECTOR_SIZE),int(curr_pos[1]/SECTOR_SIZE))
    new_maybe_curr_pos = add_tup_without_mod(curr_pos, DIRS[curr_dir])
    # new_maybe_sector = (int(new_maybe_curr_pos[0]/SECTOR_SIZE),int(new_maybe_curr_pos[1]/SECTOR_SIZE))
    in_grid = new_maybe_curr_pos[0] >= 0 and new_maybe_curr_pos[1] >= 0 and new_maybe_curr_pos[0] < len(grid[0]) and new_maybe_curr_pos[1] < len(grid)

    # def joins_inverse(new_region, old_region):
    #     for direction in range(4):
    #         if HARD_CODE_JOINS_MINI(new_region, direction) == old_region:
    #             return direction
    #     assert(False)

    # if curr_sector == new_maybe_sector:
    #     if grid[new_maybe_curr_pos[1]][new_maybe_curr_pos[0]] == '#':
    #         return orig_pos, curr_dir
    #     if grid[new_maybe_curr_pos[1]][new_maybe_curr_pos[0]] == '.':
    #         return new_maybe_curr_pos, curr_dir
    #     assert(False)
    if in_grid and grid[new_maybe_curr_pos[1]][new_maybe_curr_pos[0]] == '#':
        return orig_pos, curr_dir
    elif in_grid and grid[new_maybe_curr_pos[1]][new_maybe_curr_pos[0]] == '.':
        return new_maybe_curr_pos, curr_dir
    else:
        # assert(grid[new_maybe_curr_pos[1]][new_maybe_curr_pos[0]] == ' ')
        # region = HARD_CODE_REGIONS_MINI(curr_pos)
        # new_region = HARD_CODE_JOINS_MINI(region, curr_dir)
        if (curr_sector, curr_dir) in hard_code_cache:
            new_sector, new_direction, new_is_flipped = hard_code_cache[(curr_sector, curr_dir)]
        else:
            print('i am currently in sector', curr_sector, 'moving', DIR_TO_READABLE[curr_dir])
            raw_new_sector = input('which sector do i drop into (*,*): ')
            raw_new_direction = input('which direction (U/D/L/R): ')
            raw_new_is_flipped = input('is index flipped? (T/F): ')
            a = raw_new_sector.split(',')
            new_sector = (int(a[0]), int(a[1]))
            new_direction = READABLE_TO_DIR[raw_new_direction]
            new_is_flipped = raw_new_is_flipped.startswith('T') or raw_new_is_flipped.startswith('t')
            # print(new_is_flipped)
            hard_code_cache[(curr_sector, curr_dir)] = (new_sector, new_direction, new_is_flipped)
            hard_code_cache[(new_sector, (new_direction+2)%4)] = (curr_sector, (curr_dir+2)%4, new_is_flipped)
        # new_region_receiving_from_dir = joins_inverse(new_region, region)
        # new_dir = (new_region_receiving_from_dir+2)%2
        # print('receiving from', new_region_receiving_from_dir, 'new dir', new_dir)
        # assert(False)
        # ok this is wayyyy too annoying to deal with parity and i don't want to do this
        if curr_dir == 0 or curr_dir == 2: # L and R
            offset = curr_pos[1] - curr_sector[1]*SECTOR_SIZE
        elif curr_dir == 1 or curr_dir == 3: # U and D
            offset = curr_pos[0] - curr_sector[0]*SECTOR_SIZE

        if new_is_flipped:
            offset = SECTOR_SIZE-offset-1
            # print(offset)

        if new_direction == 0: # R
            new_pos_to_check = (new_sector[0]*SECTOR_SIZE, new_sector[1]*SECTOR_SIZE+offset)
        elif new_direction == 1: # D
            new_pos_to_check = (new_sector[0]*SECTOR_SIZE+offset, new_sector[1]*SECTOR_SIZE)
        elif new_direction == 2: # L
            new_pos_to_check = (new_sector[0]*SECTOR_SIZE+SECTOR_SIZE-1, new_sector[1]*SECTOR_SIZE+offset)
        elif new_direction == 3: # U
            new_pos_to_check = (new_sector[0]*SECTOR_SIZE+offset, new_sector[1]*SECTOR_SIZE+SECTOR_SIZE-1)
        if grid[new_pos_to_check[1]][new_pos_to_check[0]] == '#':
            return orig_pos, curr_dir
        if grid[new_pos_to_check[1]][new_pos_to_check[0]] == '.':
            return new_pos_to_check, new_direction
        assert(False)

def add_tup_without_mod(a, b):
    return ((a[0] + b[0]), (a[1] + b[1]))

if __name__ == '__main__':
    main()
    main2()
    # 27492
    # what is sector size: 50
    # i am currently in sector (1, 0) moving U
    # which sector do i drop into (*,*): 0,3
    # which direction (U/D/L/R): R
    # is index flipped? (T/F): F
    # i am currently in sector (1, 0) moving L
    # which sector do i drop into (*,*): 0,2
    # which direction (U/D/L/R): R
    # is index flipped? (T/F): T
    # i am currently in sector (1, 1) moving L
    # which sector do i drop into (*,*): 0,2
    # which direction (U/D/L/R): D
    # is index flipped? (T/F): F
    # i am currently in sector (2, 0) moving R
    # which sector do i drop into (*,*): 1,2
    # which direction (U/D/L/R): L
    # is index flipped? (T/F): T
    # i am currently in sector (2, 0) moving D
    # which sector do i drop into (*,*): 1,1
    # which direction (U/D/L/R): L
    # is index flipped? (T/F): F
    # i am currently in sector (2, 0) moving U
    # which sector do i drop into (*,*): 0,3
    # which direction (U/D/L/R): U
    # is index flipped? (T/F): F
    # i am currently in sector (0, 3) moving R
    # which sector do i drop into (*,*): 1,2
    # which direction (U/D/L/R): U
    # is index flipped? (T/F): F
    # 78291
