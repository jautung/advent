from itertools import combinations
import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '24_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    
    # TEST_X_MIN = 7
    # TEST_X_MAX = 27
    # TEST_Y_MIN = 7
    # TEST_Y_MAX = 27

    TEST_X_MIN = 200000000000000
    TEST_X_MAX = 400000000000000
    TEST_Y_MIN = 200000000000000
    TEST_Y_MAX = 400000000000000

    # print_2d(data)
    counter = 0
    pairs = list(combinations(data, 2))
    for pair in pairs:
        h1, h2, = pair
        p1, v1 = h1
        p2, v2 = h2
        px1, py1, pz1 = p1
        vx1, vy1, vz1 = v1
        px2, py2, pz2 = p2
        vx2, vy2, vz2 = v2
        if vx2 * vy1 - vy2 * vx1 == 0:
            # print('parallel')
            pass
        else:
            t2 = ((py2 - py1) * vx1 - (px2 - px1) * vy1) / (vx2 * vy1 - vy2 * vx1)
            t1 = ((py1 - py2) * vx2 - (px1 - px2) * vy2) / (vx1 * vy2 - vy1 * vx2)
            if t1 < 0 or t2 < 0:
                # print('past')
                pass
            else:
                coords1 = (px1 + t1 * vx1, py1 + t1 * vy1)
                # coords2 = (px2 + t2 * vx2, py2 + t2 * vy2)
                if TEST_X_MIN <= coords1[0] and coords1[0] <= TEST_X_MAX and TEST_Y_MIN <= coords1[1] and coords1[1] <= TEST_Y_MAX:
                    counter += 1
                    # print('in bounds')
                    pass
                else:
                    # print('out of bounds')
                    pass
                # print(coords1, coords2)
                #
                # X COORD OF INTERSECT
                # px1 + ((py1 - py2) * vx2 - (px1 - px2) * vy2) * vx1 / (vx1 * vy2 - vy1 * vx2)
                # Y COORD OF INTERSECT
                # py1 + ((py1 - py2) * vx2 - (px1 - px2) * vy2) * vy1 / (vx1 * vy2 - vy1 * vx2)
                # a = TEST_X_MIN * (vx1 * vy2 - vy1 * vx2) <= px1 * (vx1 * vy2 - vy1 * vx2) + ((py1 - py2) * vx2 - (px1 - px2) * vy2) * vx1
                # b = TEST_X_MAX * (vx1 * vy2 - vy1 * vx2) >= px1 * (vx1 * vy2 - vy1 * vx2) + ((py1 - py2) * vx2 - (px1 - px2) * vy2) * vx1
                # c = TEST_Y_MIN * (vx1 * vy2 - vy1 * vx2) <= py1 * (vx1 * vy2 - vy1 * vx2) + ((py1 - py2) * vx2 - (px1 - px2) * vy2) * vy1
                # d = TEST_Y_MAX * (vx1 * vy2 - vy1 * vx2) >= py1 * (vx1 * vy2 - vy1 * vx2) + ((py1 - py2) * vx2 - (px1 - px2) * vy2) * vy1
                # if a and b and c and d:
                #     counter += 1
                #     # print('in bounds')
                #     pass
                # else:
                #     # print('out of bounds')
                #     pass
                # #
                # #
                # a_ = TEST_X_MIN <= px1 + t1 * vx1
                # b_ = px1 + t1 * vx1 <= TEST_X_MAX
                # c_ = TEST_Y_MIN <= py1 + t1 * vy1
                # d_ = py1 + t1 * vy1 <= TEST_Y_MAX
                # print(a, a_)
                # print(TEST_X_MIN, px1 + t1 * vx1, t1)
                # print(TEST_X_MIN * (vx1 * vy2 - vy1 * vx2), px1 * (vx1 * vy2 - vy1 * vx2) + ((py1 - py2) * vx2 - (px1 - px2) * vy2) * vx1)
                # assert(a == a_)
                # assert(b == b_)
                # assert(c == c_)
                # assert(d == d_)
                # ah, right negatives in a inequality
                    
                
        
        # time t and t2
        # px1 + t1 * vx1, py1 + t1 * vy1
        # px2 + t2 * vx2, py2 + t2 * vy2
        #
        # px1 + t1 * vx1 == px2 + t2 * vx2 and py1 + t1 * vy1 == py2 + t2 * vy2
        #
        # t1 = ((px2 + t2 * vx2) - px1) / vx1
        # (t2 * vx2 + px2 - px1) * vy1 / vx1 = py2 + t2 * vy2 - py1
        # (t2 * vx2 * vy1) + (px2 - px1) * vy1 = (py2 - py1) * vx1 + (t2 * vy2 * vx1)
        # t2 * (vx2 * vy1 - vy2 * vx1) = (py2 - py1) * vx1 - (px2 - px1) * vy1
        # t2 = ((py2 - py1) * vx1 - (px2 - px1) * vy1) / (vx2 * vy1 - vy2 * vx1)
        #
        # intersection point 
        # need t1, t2 >= 0 and X and Y in bounds
    print(counter)

def parse(line):
    sides = line.split('@')
    position = [int(a.strip()) for a in sides[0].split(',')]
    velocity = [int(a.strip()) for a in sides[1].split(',')]
    return position, velocity

def main2():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    print_2d(data)
    # you're telling me there is a solution to this?!?!
    # probably jsut need two or three to define it no?
    # at time t any stone is at, for hailstone 1:
    # px1 + t * vx1, py1 + t * vy1, pz1 + t * vz1
    # and for hailstone i
    # px_i + t * vx_i, py_i + t * vy_i, pz_i + t * vz_i
    
    # I mean I have 6 degrees of freedom to fudge the stone
    # px_s + t * vx_s, py_s + t * vy_s, pz_s + t * vz_s
    
    # "
    # find (px_s, vx_s, py_s, vy_s, pz_s, vz_s), so that...
    # for EACH i in the list, there EXIST t_i > 0 such that:
    # @ px_i + t_i * vx_i == px_s + t_i * vx_s
    # @ py_i + t_i * vy_i == py_s + t_i * vy_s
    # @ pz_i + t_i * vz_i == pz_s + t_i * vz_s
    # "
    #
    # such that...
    # t_i == (px_i-px_s)/(vx_s-vx_i)
    # t_i == (py_i-py_s)/(vy_s-vy_i)
    # t_i == (pz_i-pz_s)/(vz_s-vz_i)
    # which means all RHS equal, which is 2 equations
    # i guess we just need 3 hail to define 6 equations then? then just solve for the _s?
    #
    # (px_1-px_s)/(vx_s-vx_1) == (py_1-py_s)/(vy_s-vy_1)
    # (px_1-px_s)/(vx_s-vx_1) == (pz_1-pz_s)/(vz_s-vz_1)
    # (px_2-px_s)/(vx_s-vx_2) == (py_2-py_s)/(vy_s-vy_2)
    # (px_2-px_s)/(vx_s-vx_2) == (pz_2-pz_s)/(vz_s-vz_2)
    # (px_3-px_s)/(vx_s-vx_3) == (py_3-py_s)/(vy_s-vy_3)
    # (px_3-px_s)/(vx_s-vx_3) == (pz_3-pz_s)/(vz_s-vz_3)
    # just need to solve this?!?!?
    # just wolfram alpha this?!?!? this is boring...

    # (A-a)/(b-D) == (G-c)/(e-M)
    # (A-a)/(b-D) == (H-d)/(f-N)
    # (B-a)/(b-E) == (I-c)/(e-O)
    # (B-a)/(b-E) == (J-d)/(f-P)
    # (C-a)/(b-F) == (K-c)/(e-Q)
    # (C-a)/(b-F) == (L-d)/(f-R)
    
    # Solve {(A-a)/(b-D) = (G-c)/(e-M), (A-a)/(b-D) = (H-d)/(f-N), (B-a)/(b-E) = (I-c)/(e-O), (B-a)/(b-E) = (J-d)/(f-P), (C-a)/(b-F) = (K-c)/(e-Q), (C-a)/(b-F) = (L-d)/(f-R)} for (a,b,c,d,e,f)
    # wolfram gave up
    # let's try specific example
    # (19-px_s)/(vx_s+2) == (13-py_s)/(vy_s-1)
    # (19-px_s)/(vx_s+2) == (30-pz_s)/(vz_s+2)
    # (18-px_s)/(vx_s+1) == (19-py_s)/(vy_s+1)
    # (18-px_s)/(vx_s+1) == (22-pz_s)/(vz_s+2)
    # (20-px_s)/(vx_s+2) == (25-py_s)/(vy_s+2)
    # (20-px_s)/(vx_s+2) == (34-pz_s)/(vz_s+4)

    # (19-a)/(d+2) == (13-b)/(e-1), (19-a)/(d+2) == (30-c)/(f+2), (18-a)/(d+1) == (19-b)/(e+1), (18-a)/(d+1) == (22-c)/(f+2), (20-a)/(d+2) == (25-b)/(e+2), (20-a)/(d+2) == (34-c)/(f+4)
    # no solutions because divide by 0... hmmmm
    # (19-a)*(e-1)=(13-b)*(d+2), (19-a)*(f+2)=(30-c)*(d+2), (18-a)*(e+1)=(19-b)*(d+1), (18-a)*(f+2)=(22-c)*(d+1), (20-a)*(e+2)=(25-b)*(d+2), (20-a)*(f+4)=(34-c)*(d+2)
    # ok too many solutions I guess
    # just need to deal with adding more constraints i guess
    # and we need wolfram pro to fully solve bigger numbers
    # screw this shit

if __name__ == '__main__':
    main()
    main2()
