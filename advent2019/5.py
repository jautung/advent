import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def main():
    data = [int(i) for i in readlines(FILENAME)[0].split(',')]
    # data = [int(dat) for dat in data]
    # print(data)
    curr_pos = 0

    INPUT = 1

    while True:
        # print(data)
        curr_opcode = data[curr_pos]
        parm_modes = curr_opcode//100
        parm_mode_1 = parm_modes%10
        parm_mode_2 = (parm_modes%100) // 10
        parm_mode_3 = (parm_modes%1000) // 100
        curr_opcode = curr_opcode%100
        # print(curr_opcode, parm_mode_1, parm_mode_2, parm_mode_3)
        if curr_opcode == 1:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            data[out] = real_inp1 + real_inp2
            curr_pos += 4
        elif curr_opcode == 2:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            data[out] = real_inp1 * real_inp2
            curr_pos += 4
        elif curr_opcode == 3:
            inp = data[curr_pos+1]
            assert(parm_mode_1 == 0)
            # print('input will be stored in position', inp)
            data[inp] = INPUT
            curr_pos += 2
        elif curr_opcode == 4:
            out = data[curr_pos+1]
            # print('a', out, data[out])
            if parm_mode_1 == 0:
                real_out = data[out]
            elif parm_mode_1 == 1:
                real_out = out
            print('output is', real_out)
            # assert(real_out == 0)
            curr_pos += 2
        elif curr_opcode == 99:
            # print(data[0])
            return
        else:
            assert(False)

def main2():
    data = [int(i) for i in readlines(FILENAME)[0].split(',')]
    # data = [int(dat) for dat in data]
    # print(data)
    curr_pos = 0

    INPUT = 5

    while True:
        # print(data)
        curr_opcode = data[curr_pos]
        parm_modes = curr_opcode//100
        parm_mode_1 = parm_modes%10
        parm_mode_2 = (parm_modes%100) // 10
        parm_mode_3 = (parm_modes%1000) // 100
        curr_opcode = curr_opcode%100
        # print(curr_opcode, parm_mode_1, parm_mode_2, parm_mode_3)
        if curr_opcode == 1:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            data[out] = real_inp1 + real_inp2
            curr_pos += 4
        elif curr_opcode == 2:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            data[out] = real_inp1 * real_inp2
            curr_pos += 4
        elif curr_opcode == 3:
            inp = data[curr_pos+1]
            assert(parm_mode_1 == 0)
            # print('input will be stored in position', inp)
            data[inp] = INPUT
            curr_pos += 2
        elif curr_opcode == 4:
            out = data[curr_pos+1]
            # print('a', out, data[out])
            if parm_mode_1 == 0:
                real_out = data[out]
            elif parm_mode_1 == 1:
                real_out = out
            print('output is', real_out)
            # assert(real_out == 0)
            curr_pos += 2
        elif curr_opcode == 5:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            if real_inp1 != 0:
                curr_pos = real_inp2
            else:
                curr_pos += 3
        elif curr_opcode == 6:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            if real_inp1 == 0:
                curr_pos = real_inp2
            else:
                curr_pos += 3
        elif curr_opcode == 7:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            if real_inp1 < real_inp2:
                data[out] = 1
            else:
                data[out] = 0
            curr_pos += 4
        elif curr_opcode == 8:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            if real_inp1 == real_inp2:
                data[out] = 1
            else:
                data[out] = 0
            curr_pos += 4
        elif curr_opcode == 99:
            # print(data[0])
            return
        else:
            assert(False)

if __name__ == '__main__':
    # main()
    main2()
