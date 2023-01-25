import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '20_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]

    # db = dict() # indexed by ID, get val and rank
    # for i, val in enumerate(data):
    #     db[i] = (val, i)
    # print(db)

    # # mixing
    # for i in range(len(data)): # go through IDs
    #     val, rank = db[i]
    #     if val == 0:
    #         continue
    #     elif val > 0:
    #         for offset in range(val):
    #             db[i+offset] = (db[i+offset][0], db[i+offset][1])

    db = list(enumerate(data))
    # print(db)

    # print([d[1] for d in db])
    for i in range(len(data)):
        index = find_new_index_by_id(i, db)
        distance_to_move = db[index][1]
        # print('moving id', i, 'currently at index', index, 'distance', distance_to_move)
        move_item_at_index_by_distance(db, index, distance_to_move)
        # print(db)
        # print([d[1] for d in db])

    # print('final')
    # print([d[1] for d in db])
    mixed = [d[1] for d in db]
    offset = mixed.index(0)
    final = 0
    for res in range(1000,4000,1000):
        # print(mixed[(offset+res)%len(mixed)])
        final += mixed[(offset+res)%len(mixed)]
    print(final)

def find_new_index_by_id(i, db):
    # print('huh', i, db, next(idx for idx, val in enumerate(db) if val[0] == i))
    return next(idx for idx, val in enumerate(db) if val[0] == i)

def move_item_at_index_by_distance(db, index, distance_to_move):
    # distance_to_move = distance_to_move%len(db)
    popped_element = db.pop(index)
    new_index = (index+distance_to_move)%(len(db))
    # print('new_index', new_index, index, distance_to_move)
    if distance_to_move < 0 and new_index == 0:
        new_index = len(db)
    db.insert(new_index, popped_element)
    # L = 7
    # initial position = 3

    # d_to_move, insert_at
    # 1, 4
    # 2, 5
    # 3, 0
    # 4, 1
    # 5, 2
    # 6, 3
    # 7, 4
    # 8, 5
    # 9, 0
    # .
    # .
    # .
    # 0, 3
    # -1, 2
    # -2, 1
    # -3, 6
    # -4, 5
    # -5, 4
    # -6, 3
    # -7, 2
    # -8, 1
    # -9, 6

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]

    KEY = 811589153
    TIMES = 10

    data = [KEY*dat for dat in data]

    # db = dict() # indexed by ID, get val and rank
    # for i, val in enumerate(data):
    #     db[i] = (val, i)
    # print(db)

    # # mixing
    # for i in range(len(data)): # go through IDs
    #     val, rank = db[i]
    #     if val == 0:
    #         continue
    #     elif val > 0:
    #         for offset in range(val):
    #             db[i+offset] = (db[i+offset][0], db[i+offset][1])

    db = list(enumerate(data))
    # print(db)

    # print([d[1] for d in db])
    for _ in range(TIMES):
        for i in range(len(data)):
            index = find_new_index_by_id(i, db)
            distance_to_move = db[index][1]
            # print('moving id', i, 'currently at index', index, 'distance', distance_to_move)
            move_item_at_index_by_distance(db, index, distance_to_move)
            # print(db)
            # print([d[1] for d in db])

    # print('final')
    # print([d[1] for d in db])
    mixed = [d[1] for d in db]
    offset = mixed.index(0)
    final = 0
    for res in range(1000,4000,1000):
        # print(mixed[(offset+res)%len(mixed)])
        final += mixed[(offset+res)%len(mixed)]
    print(final)

if __name__ == '__main__':
    main()
    main2()
