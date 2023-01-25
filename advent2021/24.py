import sys 
sys.path.append('..')

import copy
import random
from collections import defaultdict
from helper import *

FILENAME = '24_dat.txt'
mapper = {}

class Node:
   def __init__(self, left = None, right = None, op = None):
      self.left = left
      self.right = right
      self.op = op

def print_tree(node, indent = 0, up_to_depth = None):
    if up_to_depth != None and indent >= up_to_depth:
        print(' ' * indent, node)
        return
    if not isinstance(node, Node):
        print(' ' * indent, node)
    else:
        print(' ' * indent, node.op)
        print_tree(node.left, indent = indent + 1, up_to_depth = up_to_depth)
        print_tree(node.right, indent = indent + 1, up_to_depth = up_to_depth)

def depth_tree(node):
    if not isinstance(node, Node):
        return 1
    else:
        return max(depth_tree(node.left), depth_tree(node.right)) + 1

def main():
    data = readlines_split_each_line(FILENAME)

    # INPUT = [1,1,1,1]

    # def run_alu(inp):
    #     inp_idx = 0
    #     vals = {
    #         'w': 0,
    #         'x': 0,
    #         'y': 0,
    #         'z': 0,
    #     }

    #     def get_second_arg(dat):
    #         if dat[2] in vals:
    #             return vals[dat[2]]
    #         else:
    #             return int(dat[2])

    #     for dat in data:
    #         if dat[0] == 'inp':
    #             vals[dat[1]] = inp[inp_idx]
    #             inp_idx += 1
    #         elif dat[0] == 'add':
    #             vals[dat[1]] = vals[dat[1]] + get_second_arg(dat)
    #         elif dat[0] == 'mul':
    #             vals[dat[1]] = vals[dat[1]] * get_second_arg(dat)
    #         elif dat[0] == 'div':
    #             vals[dat[1]] = int(vals[dat[1]] / get_second_arg(dat))
    #         elif dat[0] == 'mod':
    #             vals[dat[1]] = vals[dat[1]] % get_second_arg(dat)
    #         elif dat[0] == 'eql':
    #             vals[dat[1]] = 1 if (vals[dat[1]] == get_second_arg(dat)) else 0
    #     return vals

    inp_idx = 0
    vals = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    def get_second_arg(dat):
        if dat[2] in vals:
            return vals[dat[2]]
        else:
            return int(dat[2])

    for dat in data:
        if dat[0] == 'inp':
            vals[dat[1]] = 'inp' + str(inp_idx)
            inp_idx += 1
        elif dat[0] == 'add' and get_second_arg(dat) == 0:
            continue
        elif dat[0] == 'add' and vals[dat[1]] == 0:
            vals[dat[1]] = get_second_arg(dat)
        elif dat[0] == 'mul' and get_second_arg(dat) == 1:
            continue
        elif dat[0] == 'mul' and vals[dat[1]] == 1:
            vals[dat[1]] = get_second_arg(dat)
        elif dat[0] == 'mul' and get_second_arg(dat) == 0:
            vals[dat[1]] = 0
        elif dat[0] == 'mul' and vals[dat[1]] == 0:
            vals[dat[1]] = 0
        elif dat[0] == 'div' and get_second_arg(dat) == 1:
            continue
        elif dat[0] == 'div' and vals[dat[1]] == 1:
            vals[dat[1]] = get_second_arg(dat)
        elif dat[0] == 'mod' and get_second_arg(dat) == 1:
            continue
        elif dat[0] == 'mod' and vals[dat[1]] == 1:
            vals[dat[1]] = get_second_arg(dat)
        else:
            left = vals[dat[1]]
            right = get_second_arg(dat)
            if isinstance(left, int) and isinstance(right, int):
                if dat[0] == 'add':
                    vals[dat[1]] = left + right
                elif dat[0] == 'mul':
                    vals[dat[1]] = left * right
                elif dat[0] == 'div':
                    vals[dat[1]] = int(left / right)
                elif dat[0] == 'mod':
                    vals[dat[1]] = left % right
                elif dat[0] == 'eql':
                    vals[dat[1]] = 1 if (left == right) else 0
            else:
                vals[dat[1]] = Node(left=left, right=right, op=dat[0])
        # elif dat[0] == 'mul':
        #     vals[dat[1]] = vals[dat[1]] * get_second_arg(dat)
        # elif dat[0] == 'div':
        #     vals[dat[1]] = int(vals[dat[1]] / get_second_arg(dat))
        # elif dat[0] == 'mod':
        #     vals[dat[1]] = vals[dat[1]] % get_second_arg(dat)
        # elif dat[0] == 'eql':
        #     vals[dat[1]] = 1 if (vals[dat[1]] == get_second_arg(dat)) else 0

    # print_tree(vals['w'])
    # print_tree(vals['x'])
    # print_tree(vals['y'])
    # print_tree(vals['z'])
    # print(vals['z'].right.op)
    print_tree(vals['z'], up_to_depth = 7)

    # print(depth_tree(vals['z']))
    # print('f')

    # for i in range(10):
    #     print(i, run_alu([i]))
    # val = run_alu([int(i) for i in list('13579246899999')])
    # print('VALID' if val['z'] == 0 else 'INVALID')
    # for model_num in range(99999999999999, -1, -1):
    # f = open('24_out.txt', 'w')
    # for _ in range(1000000):
    #     model_num = random.randint(0, 99999999999999)
    #     model_num_str = str(model_num).rjust(14, '0')
    #     if '0' in list(model_num_str):
    #         continue
    #     val = run_alu([int(i) for i in list(model_num_str)])
    #     check = val['z']
    #     # print(model_num_str, check)
    #     f.write(str(model_num_str) + ' ' + str(check) + '\n')
    #     # if check == 0:
    #     #     print('VALID!!!')
    #     #     return
    #     #     # print('VALID' if val['z'] == 0 else 'INVALID')
    # f.close()
    # f = open('24_out.txt', 'w')

    # def in_out(model_num):
    #     model_num_str = str(model_num).rjust(14, '0')
    #     if '0' in list(model_num_str):
    #         return None
    #     val = run_alu([int(i) for i in list(model_num_str)])
    #     return val['z']

    # res = []
    # for _ in range(1000000):
    #     model_num = random.randint(0, 99999999999999)
    #     check = in_out(model_num)
    #     if check == None:
    #         continue
    #     if check < 100000:
    #         print(model_num, check)
    #         res.append((model_num, check))
        # f.write(str(model_num_str) + ' ' + str(check) + '\n')
        # if check == 0:
        #     print('VALID!!!')
        #     return
        #     # print('VALID' if val['z'] == 0 else 'INVALID')
    # f.close()
    # print()
    # print()
    # print()
    # print_2d(sorted(res))

    # for i in range(25884696711345 - 10, 25884696711345 + 10):
    #     model_num = i
    #     check = in_out(model_num)
    #     print(model_num, check)

    # POS = 1 # increment by 1
    # POS = 1000000 # increment by 26
    # POS = 100000
    # START = 25884696711345
    # for i in range(START, START + 9*POS, POS):
    #     model_num = i
    #     check = in_out(model_num)
    #     print(model_num, check)

    # ROLL = 11884696711345
    # for POS in range(14):
    #     print('rolling', POS)
    #     for i in range(1, 10):
    #         model_num = str(ROLL)[:POS] + str(i) + str(ROLL)[POS+1:]
    #         # model_num[POS] = str(i)
    #         check = in_out(model_num)
    #         print(model_num, check)
    #     print()

    # print(11111111764121, in_out(11111111764121))


# https://docs.google.com/spreadsheets/d/1bUoXb7Zt0NV-wMxgsfPjEIs2JYOdgS4MmokmW7Giyu4/edit#gid=0
# https://docs.google.com/spreadsheets/d/1j1JdsJvZFTf3kyoiIg6kdMfZVpSV_QgoasJ3uFFUCWs/edit#gid=0

# TIME: imma lowkey give up after 1 hour and do another approach

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

# TIME: 

if __name__ == '__main__':
    main()
    main2()
