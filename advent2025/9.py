import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '9_dat.txt'
mapper = {}

def top_left_cands(lst):
    sorted_by_x = sorted(lst)
    cands = []
    for pt in sorted_by_x:
        if len(cands) == 0:
            cands.append(pt)
            continue
        last_cand = cands[-1]
        if pt[1] >= last_cand[1]:
            continue
        cands.append(pt)
    return cands

def top_right_cands(lst):
    new_lst = [[-pt[0], pt[1]] for pt in lst]
    res = top_left_cands(new_lst)
    return [[-pt[0], pt[1]] for pt in res]

def bot_left_cands(lst):
    new_lst = [[pt[0], -pt[1]] for pt in lst]
    res = top_left_cands(new_lst)
    return [[pt[0], -pt[1]] for pt in res]

def bot_right_cands(lst):
    new_lst = [[-pt[0], -pt[1]] for pt in lst]
    res = top_left_cands(new_lst)
    return [[-pt[0], -pt[1]] for pt in res]

def find_area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def main():
    data = readlines(FILENAME)
    data = [[int(x) for x in dat.split(',')] for dat in data]

    # print(data)
    top_lefts = top_left_cands(data)
    top_rights = top_right_cands(data)
    bot_lefts = bot_left_cands(data)
    bot_rights = bot_right_cands(data)
    # print(top_lefts)
    # print(top_rights)
    # print(bot_lefts)
    # print(bot_rights)

    max_area = None
    for tl in top_lefts:
        for br in bot_rights:
            area = find_area(tl, br)
            if max_area is None or area > max_area:
                max_area = area
    for tr in top_rights:
        for bl in bot_lefts:
            area = find_area(tr, bl)
            if max_area is None or area > max_area:
                max_area = area
    print(max_area)

def bounds(lst):
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    for pt in lst:
        if min_x is None or pt[0] < min_x:
            min_x = pt[0]
        if max_x is None or pt[0] > max_x:
            max_x = pt[0]
        if min_y is None or pt[1] < min_y:
            min_y = pt[1]
        if max_y is None or pt[1] > max_y:
            max_y = pt[1]
    return (min_x, max_x, min_y, max_y)

def main2():
    data = readlines(FILENAME)
    data = [[int(x) for x in dat.split(',')] for dat in data]
    # print(data)
    # print(bounds(data))

    # max_area = None
    # for tl in data:
    #     for br in data:
    #         area = find_area(tl, br)
    #         if max_area is None or area > max_area:
    #             max_area = area
    # print(max_area)

    # min_x, max_x, min_y, max_y = bounds(data)
    # c = 0
    # for x in range(min_x, max_x+1):
    #     for y in range(min_y, max_y+1):
    #         c += 1
    # print(c)

    all_x = sorted(list(set([pt[0] for pt in data])))
    all_y = sorted(list(set([pt[1] for pt in data])))
    # print(all_x, len(all_x))
    # print(all_y, len(all_y))

    x_proj_to_real_map = dict()
    x_real_to_proj_map = dict()
    y_proj_to_real_map = dict()
    y_real_to_proj_map = dict()

    for i, x in enumerate(all_x):
        x_proj_to_real_map[i] = x
        x_real_to_proj_map[x] = i
    for i, y in enumerate(all_y):
        y_proj_to_real_map[i] = y
        y_real_to_proj_map[y] = i


    projected_x_len = len(all_x)
    projected_y_len = len(all_y)
    projected_data = [(x_real_to_proj_map[pt[0]], y_real_to_proj_map[pt[1]]) for pt in data]
    # print(projected_x_len, projected_y_len, projected_data)

    # c = 0
    # for x in range(projected_x_len):
    #     for y in range(projected_y_len):
    #         c += 1
    # print(c)

    horz_segments = dict()
    vert_segments = dict()
    for i in range(len(projected_data)):
        start = projected_data[i]
        end = projected_data[(i+1) % len(projected_data)]
        if start[0] == end[0]: # same x, so vertical seg
            other = [start[1], end[1]]
            if start[0] not in vert_segments:
                vert_segments[start[0]] = set([(min(other), max(other))])
            else:
                vert_segments[start[0]].add((min(other), max(other)))
        elif start[1] == end[1]: # same y, so horz seg
            other = [start[0], end[0]]
            if start[1] not in horz_segments:
                horz_segments[start[1]] = set([(min(other), max(other))])
            else:
                horz_segments[start[1]].add((min(other), max(other)))
        else:
            assert False
    # print("horz_segments", horz_segments)
    # print("vert_segments", vert_segments)
    # print()

    # for y in range(projected_y_len):
    #     for x in range(projected_x_len):
    #         if (x,y) in projected_data:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()

    # print()
    # print()

    # for y in range(projected_y_len):
    #     for x in range(projected_x_len):
    #         if (x,y) in projected_data:
    #             print("#", end="")
    #         else:
    #             done = False

    #             v_segs_at_x = vert_segments[x]
    #             for v_seg in v_segs_at_x:
    #                 if v_seg[0] <= y and v_seg[1] >= y:
    #                     print("X", end="") # inside v seg
    #                     done = True
    #                     break

    #             h_segs_at_y = horz_segments[y]
    #             for h_seg in h_segs_at_y:
    #                 if h_seg[0] <= x and h_seg[1] >= x:
    #                     print("X", end="") # inside h seg
    #                     done = True
    #                     break

    #             if not done:
    #                 print(".", end="")
    #     print()

    # print()
    # print()

    res = ""
    inside_outside = []
    for y in range(projected_y_len):
        inside_outside_row = []
        # if y == 6:
        #     exit(1)
        status = "outside"
        # h_segs_at_y = horz_segments[y]
        # inside_h_seg = None
        entrance_v_seg = None
        inside_entrance_v_seg = None
        for x in range(projected_x_len):
            # print(x,y,"start",status, end="")
            # if status == "h_seg":
            #     assert inside_h_seg is not None
            #     if inside_h_seg[1] == x:
            #         status = "outside"
            #         inside_h_seg = None
            #         print("#", end="") # terminal right
            #         continue
            #     else:
            #         print("#", end="") # inside h seg
            #         continue
            if status == "outside":
                # check if start of horz segment
                # for h_seg in h_segs_at_y:
                #     if h_seg[0] == x:
                #         status = "h_seg"
                #         inside_h_seg = h_seg
                #         break
                # if status == "h_seg":
                #     assert inside_h_seg is not None
                #     print("#", end="") # terminal left
                #     continue

                # check if part of vert segment
                v_segs_at_x = vert_segments[x]
                for v_seg in v_segs_at_x:
                    if v_seg[0] <= y and v_seg[1] >= y:
                        # within v seg
                        res += "#" # inside v seg
                        inside_outside_row.append(True)
                        # print(" flipping in", end="")
                        # print(" INSIDE", end="")
                        status = "inside"
                        if v_seg[0] == y:
                            entrance_v_seg = "extend_down"
                        elif v_seg[1] == y:
                            entrance_v_seg = "extend_up"
                        else:
                            entrance_v_seg = None
                        break
                if status == "inside":
                    # print()
                    continue
                else:
                    res += "." # still outside
                    inside_outside_row.append(False)
                    # print(" OUTSIDE")
                    continue
            elif status == "inside":
                # we _could_ check for h_seg for completeness
                # but it really doesn't matter and doesn't affect the problem

                # check if part of vert segment
                v_segs_at_x = vert_segments[x]
                for v_seg in v_segs_at_x:
                    if v_seg[0] <= y and v_seg[1] >= y:
                        # within v seg
                        if v_seg[0] == y or v_seg[1] == y:
                            if entrance_v_seg is not None:
                                if v_seg[0] == y and entrance_v_seg == "extend_up":
                                    # we stay inside here (saddle/inflection shape)
                                    # print(" inflection stay in", end="")
                                    pass
                                elif v_seg[1] == y and entrance_v_seg == "extend_down":
                                    # we stay inside here (saddle/inflection shape)
                                    # print(" inflection stay in", end="")
                                    pass
                                else:
                                    # print(" corner U-shape flipping out", end="")
                                    status = "outside"
                                entrance_v_seg = None
                            elif inside_entrance_v_seg is not None:
                                if v_seg[0] == y and inside_entrance_v_seg == "extend_up":
                                    # we go outside here (saddle/inflection shape)
                                    # print(" inflection go out", end="")
                                    status = "outside"
                                elif v_seg[1] == y and inside_entrance_v_seg == "extend_down":
                                    # we go outside here (saddle/inflection shape)
                                    # print(" inflection go out", end="")
                                    status = "outside"
                                else:
                                    pass
                                    # print(" corner U-shape staying in", end="")
                                inside_entrance_v_seg = None
                            else:
                                if v_seg[0] == y:
                                    # print(" corner entering down", end="")
                                    inside_entrance_v_seg = "extend_down"
                                elif v_seg[1] == y:
                                    # print(" corner entering up", end="")
                                    inside_entrance_v_seg = "extend_up"
                                else:
                                    assert False
                        else:
                            # print(" non-corner flipping out", end="")
                            status = "outside"
                        break
                res += "#" # regardless, still considered inside for this cell
                inside_outside_row.append(True)
                # print(" INSIDE")
                continue
        res += "\n"
        inside_outside.append(inside_outside_row)
    # print()
    # print(res)

    # print_2d(inside_outside)
    def all_inside(pp1, pp2):
        xs = [pp1[0], pp2[0]]
        ys = [pp1[1], pp2[1]]
        for x in range(min(xs), max(xs)+1):
            for y in range(min(ys), max(ys)+1):
                if not inside_outside[y][x]:
                    return False
        return True

    # print(projected_data)
    max_area = None
    for i in range(len(projected_data)):
        for j in range(i+1, len(projected_data)):
            c_1 = projected_data[i]
            c_2 = projected_data[j]
            if not all_inside(c_1, c_2):
                continue
            x1 = x_proj_to_real_map[c_1[0]]
            y1 = y_proj_to_real_map[c_1[1]]
            x2 = x_proj_to_real_map[c_2[0]]
            y2 = y_proj_to_real_map[c_2[1]]
            area = find_area((x1, y1), (x2, y2))
            # print((x1, y1), (x2, y2), find_area((x1, y1), (x2, y2)))
            if max_area is None or area > max_area:
                # print((x1, y1), (x2, y2), find_area((x1, y1), (x2, y2)))
                max_area = area
    print(max_area)

if __name__ == '__main__':
    main()
    main2()
