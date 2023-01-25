import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '19_dat.txt'
mapper = {
    0: 13,
    1: 20,
    2: 2,
    3: 7,
    4: 4,
    5: 14,
    6: 21,
    7: 3,
    8: 10,
    9: 9,
    10: 8,
    11: 11,
    12: 22,
    13: 0,
    14: 5,
    15: 15,
    16: 16,
    17: 17,
    18: 18,
    19: 19,
    20: 1,
    21: 6,
    22: 12,
    23: 23,
}

# https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR

# p = sequence(( 1, 1, 1))
# q = sequence((-1,-1, 1))
# for i in sorted(zip(p,q)):
#     print (i)

def main():
    data = readlines_split_by_newlines(FILENAME)
    data = [parse_report(dat) for dat in data]
    reports = []
    for i in data:
        reports.append([(coord[0], coord[1], coord[2]) for coord in i[1]])
    # print(data)
    # print()
    # for i in reports:
    #     print(i)
    #     print()
    # print()
    # print(add_tups((1,2,3),(4,5,6)))
    # for i in range(24):
    #     print(i, transform_coord((5,6,-4),i))
    # print(reports[0])

    # for i in reports[1]:
    #     print(i)
    # print()

    # GENERATE PARTIALS
    # for i in range(len(reports)):
    #     for j in range(i+1,len(reports)):
    #         rel = determine_relative(reports[i], reports[j])
    #         if rel:
    #             print(i,j, rel)

    partial = readlines('19_partial.txt')
    # partial = readlines('19_partial_mini.txt')
    partial = [dat.split('|') for dat in partial]
    good_stuff = []
    for dat in partial:
        fixed = int(dat[0])
        moveable = int(dat[1])
        rel = dat[2].split(',')
        rel_rot = int(rel[0])
        rel_offset = (int(rel[1]), int(rel[2]), int(rel[3]))
        good_stuff.append((fixed, moveable, rel_rot, rel_offset))

    def find_dfs_path_to_report_0(report_num):
        paths = [([report_num], [])]
        while len(paths) > 0:
            path = paths.pop()
            seen_reports = set(path[0])
            latest_report = path[0][-1]
            for good_stuffie in good_stuff:
                if good_stuffie[0] == latest_report and good_stuffie[1] not in seen_reports:
                    paths.append((path[0]+[good_stuffie[1]], path[1]+[inverse_transform(good_stuffie[2], good_stuffie[3])]))
                    if good_stuffie[1] == 0:
                        return paths.pop()
                elif good_stuffie[1] == latest_report and good_stuffie[0] not in seen_reports:
                    paths.append((path[0]+[good_stuffie[0]], path[1]+[the_transform(good_stuffie[2], good_stuffie[3])]))
                    if good_stuffie[0] == 0:
                        return paths.pop()

    def inverse_transform(rot, offset):
        # for rot, i in enumerate(sequence((1, -2, 13))):
        #     # print(rot, i)
        #     for rot_inv, j in enumerate(sequence(i)):
        #         if j == (1, -2, 13):
        #             print(rot, rot_inv)
        #             break
        def f_this(report):
            unmove = [sub_tups(c, offset) for c in report]
            inv_rot = mapper[rot]
            return list(zip(*[sequence(c) for c in unmove]))[inv_rot]
        return f_this

    def the_transform(rot, offset):
        def yes_this(report):
            return [add_tups(c, offset) for c in list(zip(*[sequence(c) for c in report]))[rot]]
        return yes_this

    new_reports = []
    for report_num in range(len(reports)):
        ugh = find_dfs_path_to_report_0(report_num)
        if report_num == 0:
            new_reports.append(copy.deepcopy(reports[report_num]))
            continue
        assert(ugh)
        path, transforms = ugh
        # print(report_num, path)
        res = reports[report_num]
        for transform in transforms:
            res = transform(res)
        new_reports.append(res)

    # print(len(new_reports))
    uniquify = set().union(*new_reports)
    # for i in sorted(uniquify):
    #     print(i)
    print(len(uniquify))

    # PART 2
    scanner_pos = []
    for report_num in range(len(reports)):
        ugh = find_dfs_path_to_report_0(report_num)
        if report_num == 0:
            scanner_pos.append((0,0,0))
            continue
        assert(ugh)
        path, transforms = ugh
        # print(report_num, path)
        res = [(0,0,0)]
        for transform in transforms:
            res = transform(res)
        scanner_pos.append(res[0])

    # print(len(scanner_pos))
    # uniquify = set().union(*scanner_pos)
    # for i in scanner_pos:
    #     print(i)
    # print(len(uniquify))
    max_dist = None
    for i in scanner_pos:
        for j in scanner_pos:
            dist = manhatten(i,j)
            if max_dist == None or dist > max_dist:
                max_dist = dist
    print(max_dist)

    # for report_num in range(len(reports)):
    #     report = reports[report_num]
    #     in_coords = report_num
    #     while in_coords != 0:
    #         print(in_coords)
    #         for good_stuffie in good_stuff:
    #             if good_stuffie[1] != report_num:
    #                 continue
    #             report = [add_tups(c, good_stuffie[3]) for c in list(zip(*[sequence(c) for c in report]))[good_stuffie[2]]]
    #             in_coords = good_stuffie[0]
    #             break
    #     print(len(report))

    # idk what's wrong with this UGH it doesn't capture everything
    # while True:
    #     on_first = set()
    #     on_second = set()
    #     for good_stuffie in good_stuff:
    #         on_first.add(good_stuffie[0])
    #         on_second.add(good_stuffie[1])
    #     reports_to_move = on_second.difference(on_first)
    #     if len(reports_to_move) == 0:
    #         break
    #     for good_stuffie in good_stuff:
    #         if good_stuffie[1] not in reports_to_move:
    #             continue
    #         fixed_report = reports[good_stuffie[0]]
    #         movable_report = reports[good_stuffie[1]]
    #         rotated = list(zip(*[sequence(c) for c in movable_report]))
    #         rotated_movable_report = rotated[good_stuffie[2]]
    #         final_movable_report = [add_tups(c, good_stuffie[3]) for c in rotated_movable_report]

    #         # for i in fixed_report:
    #         #     print(i)
    #         # print()
    #         # for i in rotated_movable_report:
    #         #     print(i)
    #         # print()
    #         # for i in final_movable_report:
    #         #     print(i)
    #         # print()

    #         common = set(fixed_report).intersection(set(final_movable_report))
    #         print('moving', good_stuffie[1], '->', good_stuffie[0])
    #         print('  length', good_stuffie[1], ':', len(reports[good_stuffie[1]]), len(movable_report), len(final_movable_report), len(set(final_movable_report)))
    #         print('  length', good_stuffie[0], ':', len(reports[good_stuffie[0]]), len(fixed_report), len(set(fixed_report)))
    #         assert(len(common) >= 12)
    #         # exit(1)

    #         # print(len(set(fixed_report).union(set(final_movable_report))))
    #         reports[good_stuffie[0]] = list(set(fixed_report).union(set(final_movable_report)))
    #         print('  length', good_stuffie[0], 'after :', len(reports[good_stuffie[0]]))
    #         # print(good_stuffie[0], reports[good_stuffie[0]])
    #         # if (1994,-1805,1792) in final_movable_report or (1994,-1805,1792) in fixed_report:
    #         #     assert(False)

    #     good_stuff = list(filter(lambda x: x[1] not in reports_to_move, good_stuff))
    #     # exit(1)
    # assert(len(good_stuff) == 0)
    # # for i in sorted(reports[0]):
    # #     print(i)

    # # print(len(reports[0]))

def determine_relative(fixed_report, movable_report):
    feasible_rotation_offsets = set()
    # feasible_offsets = []
    rotated = zip(*[sequence(c) for c in movable_report])
    for rot, lst in enumerate(rotated):
        # print(rot)
        # for i in lst:
        #     print(i)
        # print()
        for true_coord in fixed_report:
            for curr_report_coord in lst:
                offset = sub_tups(true_coord, curr_report_coord)
                new_lst = [add_tups(c, offset) for c in lst]
                # for i in fixed_report:
                #     print(i)
                # print()
                # for i in new_lst:
                #     print(i)
                # print()
                common = set(fixed_report).intersection(set(new_lst))
                if len(common) >= 12:
                    # print(len(common), rot, offset)
                    feasible_rotation_offsets.add((rot, offset))
                # exit(1)
    assert(len(feasible_rotation_offsets) <= 1)
    if len(feasible_rotation_offsets) == 0:
        return None
    else:
        return feasible_rotation_offsets.pop()


def transform_coord(coord, rotation): # rotation from 0 to 23
    return list(sequence(coord))[rotation]

def add_tups(a, b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

def sub_tups(a, b):
    return (a[0]-b[0],a[1]-b[1],a[2]-b[2])

def parse_report(data):
    coords = [[int(i) for i in dat.split(',')] for dat in data[1:]]
    return (int(data[0].split()[2]), coords)

# Time: 2:03:42

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

def manhatten(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

# Time: 2:10:16

if __name__ == '__main__':
    main()
    main2()
