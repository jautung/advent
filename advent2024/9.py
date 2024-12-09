import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '9_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    data = data[0]
    data = [int(x) for x in data]
    # print(data)
    # assert(len(data)%2 == 0)
    full = []
    ID = 0
    for index, dat in enumerate(data):
        if index % 2 == 0:
            full += [ID] * dat
            ID += 1
        else:
            full += ["."] * dat
    # print(full)
    maybe_first_empty = 0
    maybe_last = len(full)-1
    while True:
        if maybe_first_empty == maybe_last:
            break
        while True:
            if maybe_first_empty == maybe_last or full[maybe_first_empty] == ".":
                break
            maybe_first_empty += 1
        if maybe_first_empty == maybe_last:
            break
        if full[maybe_last] == ".":
            # full = full[:-1]
            maybe_last -= 1
            continue
        to_move = full[maybe_last]
        assert full[maybe_first_empty] == "."
        full[maybe_first_empty] = to_move
        maybe_first_empty += 1
        full[maybe_last] = "."
        # full = full[:-1]
        maybe_last -= 1
    # print(full)
    checksum = 0
    all_zeros = False
    for i, x in enumerate(full):
        if all_zeros:
            assert x == "."
        if x == ".":
            all_zeros = True
            continue
            # break
        checksum += i * x
    print(checksum)


def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    data = data[0]
    data = [int(x) for x in data]
    # print(data)
    # assert(len(data)%2 == 0)
    full = []
    ID = 0
    mapper = {}
    for index, dat in enumerate(data):
        if dat == 0:
            continue
        if index % 2 == 0:
            full.append(("stuff", dat, ID))
            mapper[ID] = dat
            ID += 1
        else:
            full.append(("empty", dat))
    # print_2d(full)
    # print()
    last_id_not_tried = ID - 1
    while last_id_not_tried >= 0:
        needs_space_of_length = mapper[last_id_not_tried]
        # print(last_id_not_tried)
        new_full = []
        made_move = False
        for index, k in enumerate(full):
            if k[0] == "empty" and k[1] >= needs_space_of_length:
                new_full.append(("stuff", needs_space_of_length, last_id_not_tried))
                if (k[1] > needs_space_of_length):
                    new_full.append(("empty", k[1] - needs_space_of_length))
                new_full += full[index+1:]
                made_move = True
                break
            new_full.append(k)
        if made_move:
            full = new_full
            last_id_not_tried -= 1
            continue
        last_id_not_tried -= 1
        # else:
        #     break
    # print_2d(full)

    def sum_of(starting_from, id, length):
        # print(starting_from, id, length)
        return id * ((starting_from + starting_from + length - 1) * length)//2
        # return 0

    checksum = 0
    running_index = 0
    seen_ids = set()
    for item in full:
        if item[0] == "stuff":
            if item[2] in seen_ids:
                running_index += item[1]
                continue # moved from already
            seen_ids.add(item[2])
            checksum += sum_of(starting_from=running_index, id=item[2], length=item[1])
            running_index += item[1]
            continue
        elif item[0] == "empty":
            running_index += item[1]
        else:
            assert False
    print(checksum)

    # maybe_first_empty = 0
    # maybe_last = len(full)-1
    # while True:
    #     if maybe_first_empty == maybe_last:
    #         break
    #     while True:
    #         if maybe_first_empty == maybe_last or full[maybe_first_empty] == ".":
    #             break
    #         maybe_first_empty += 1
    #     if maybe_first_empty == maybe_last:
    #         break
    #     if full[maybe_last] == ".":
    #         # full = full[:-1]
    #         maybe_last -= 1
    #         continue
    #     to_move = full[maybe_last]
    #     assert full[maybe_first_empty] == "."
    #     full[maybe_first_empty] = to_move
    #     maybe_first_empty += 1
    #     full[maybe_last] = "."
    #     # full = full[:-1]
    #     maybe_last -= 1
    # # print(full)
    # checksum = 0
    # all_zeros = False
    # for i, x in enumerate(full):
    #     if all_zeros:
    #         assert x == "."
    #     if x == ".":
    #         all_zeros = True
    #         continue
    #         # break
    #     checksum += i * x
    # print(checksum)


if __name__ == '__main__':
    main()
    main2()
