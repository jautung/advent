import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '9_dat.txt'
mapper = {}

def main():
    data = [int(i) for i in readlines(FILENAME)[0].split(',')]
    result = runProgram([1], data)
    print('output', result)
    # print('data', data)

def main2():
    data = [int(i) for i in readlines(FILENAME)[0].split(',')]
    result = runProgram([2], data)
    print('output', result)
    # print('data', data)

def runProgram(INPUTS_SEQ, data):
    input_pos = 0
    curr_pos = 0
    relative_base = 0
    all_outputs = []
    while True:
        # print(f".... stepping {curr_pos}")
        curr_opcode = data[curr_pos]
        parm_modes = curr_opcode//100
        parm_mode_1 = parm_modes%10
        parm_mode_2 = (parm_modes%100) // 10
        parm_mode_3 = (parm_modes%1000) // 100
        curr_opcode = curr_opcode%100
        # print(curr_opcode, parm_mode_1, parm_mode_2, parm_mode_3)
        if curr_opcode == 1:
            inp1 = get_from_data(data, curr_pos+1)
            inp2 = get_from_data(data, curr_pos+2)
            out = get_from_data(data, curr_pos+3)
            if parm_mode_1 == 0:
                real_inp1 = get_from_data(data, inp1)
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            elif parm_mode_1 == 2:
                real_inp1 = get_from_data(data, relative_base + inp1)
            if parm_mode_2 == 0:
                real_inp2 = get_from_data(data, inp2)
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            elif parm_mode_2 == 2:
                real_inp2 = get_from_data(data, relative_base + inp2)
            if parm_mode_3 == 0:
                assign_to_data(data, out, real_inp1 + real_inp2)
            elif parm_mode_3 == 2:
                assign_to_data(data, relative_base + out, real_inp1 + real_inp2)
            curr_pos += 4
        elif curr_opcode == 2:
            inp1 = get_from_data(data, curr_pos+1)
            inp2 = get_from_data(data, curr_pos+2)
            out = get_from_data(data, curr_pos+3)
            if parm_mode_1 == 0:
                real_inp1 = get_from_data(data, inp1)
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            elif parm_mode_1 == 2:
                real_inp1 = get_from_data(data, relative_base + inp1)
            if parm_mode_2 == 0:
                real_inp2 = get_from_data(data, inp2)
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            elif parm_mode_2 == 2:
                real_inp2 = get_from_data(data, relative_base + inp2)
            if parm_mode_3 == 0:
                assign_to_data(data, out, real_inp1 * real_inp2)
            elif parm_mode_3 == 2:
                assign_to_data(data, relative_base + out, real_inp1 * real_inp2)
            curr_pos += 4
        elif curr_opcode == 3:
            inp = get_from_data(data, curr_pos+1)
            # assert(parm_mode_1 == 0)
            # print('input will be stored in position', inp)
            assert(input_pos < len(INPUTS_SEQ))
            # print(f"  > getting input of {INPUT[input_pos]}")
            if parm_mode_1 == 0:
                assign_to_data(data, inp, INPUTS_SEQ[input_pos])
            elif parm_mode_1 == 2:
                assign_to_data(data, relative_base + inp, INPUTS_SEQ[input_pos])
            input_pos += 1
            curr_pos += 2
        elif curr_opcode == 4:
            out = get_from_data(data, curr_pos+1)
            # print('a', out, data[out])
            if parm_mode_1 == 0:
                real_out = get_from_data(data, out)
            elif parm_mode_1 == 1:
                real_out = out
            elif parm_mode_1 == 2:
                real_out = get_from_data(data, relative_base + out)
            # print('output is', real_out)
            # print(f"  > emitting output of {real_out}")
            all_outputs.append(real_out)
            # assert(real_out == 0)
            curr_pos += 2
        elif curr_opcode == 5:
            inp1 = get_from_data(data, curr_pos+1)
            inp2 = get_from_data(data, curr_pos+2)
            if parm_mode_1 == 0:
                real_inp1 = get_from_data(data, inp1)
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            elif parm_mode_1 == 2:
                real_inp1 = get_from_data(data, relative_base + inp1)
            if parm_mode_2 == 0:
                real_inp2 = get_from_data(data, inp2)
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            elif parm_mode_2 == 2:
                real_inp2 = get_from_data(data, relative_base + inp2)
            if real_inp1 != 0:
                curr_pos = real_inp2
            else:
                curr_pos += 3
        elif curr_opcode == 6:
            inp1 = get_from_data(data, curr_pos+1)
            inp2 = get_from_data(data, curr_pos+2)
            if parm_mode_1 == 0:
                real_inp1 = get_from_data(data, inp1)
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            elif parm_mode_1 == 2:
                real_inp1 = get_from_data(data, relative_base + inp1)
            if parm_mode_2 == 0:
                real_inp2 = get_from_data(data, inp2)
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            elif parm_mode_2 == 2:
                real_inp2 = get_from_data(data, relative_base + inp2)
            if real_inp1 == 0:
                curr_pos = real_inp2
            else:
                curr_pos += 3
        elif curr_opcode == 7:
            inp1 = get_from_data(data, curr_pos+1)
            inp2 = get_from_data(data, curr_pos+2)
            out = get_from_data(data, curr_pos+3)
            if parm_mode_1 == 0:
                real_inp1 = get_from_data(data, inp1)
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            elif parm_mode_1 == 2:
                real_inp1 = get_from_data(data, relative_base + inp1)
            if parm_mode_2 == 0:
                real_inp2 = get_from_data(data, inp2)
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            elif parm_mode_2 == 2:
                real_inp2 = get_from_data(data, relative_base + inp2)
            if parm_mode_3 == 0:
                assign_to_data(data, out, 1 if real_inp1 < real_inp2 else 0)
            elif parm_mode_3 == 2:
                assign_to_data(data, relative_base + out, 1 if real_inp1 < real_inp2 else 0)
            curr_pos += 4
        elif curr_opcode == 8:
            inp1 = get_from_data(data, curr_pos+1)
            inp2 = get_from_data(data, curr_pos+2)
            out = get_from_data(data, curr_pos+3)
            if parm_mode_1 == 0:
                real_inp1 = get_from_data(data, inp1)
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_1 == 2:
                real_inp1 = get_from_data(data, relative_base + inp1)
            if parm_mode_2 == 0:
                real_inp2 = get_from_data(data, inp2)
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            elif parm_mode_2 == 2:
                real_inp2 = get_from_data(data, relative_base + inp2)
            if parm_mode_3 == 0:
                assign_to_data(data, out, 1 if real_inp1 == real_inp2 else 0)
            elif parm_mode_3 == 2:
                assign_to_data(data, relative_base + out, 1 if real_inp1 == real_inp2 else 0)
            curr_pos += 4
        elif curr_opcode == 9:
            inp = get_from_data(data, curr_pos+1)
            if parm_mode_1 == 0:
                real_inp = get_from_data(data, inp)
            elif parm_mode_1 == 1:
                real_inp = inp
            elif parm_mode_1 == 2:
                real_inp = get_from_data(data, relative_base + inp)
            relative_base += real_inp
            curr_pos += 2
        elif curr_opcode == 99:
            # print(data[0])
            return all_outputs
        else:
            assert(False)

def get_from_data(data, idx):
    if idx >= 0 and idx < len(data):
        return data[idx]
    assert idx >= 0
    return 0

def assign_to_data(data, idx, val):
    if idx >= 0 and idx < len(data):
        data[idx] = val
    assert idx >= 0
    data += [0 for _ in range(idx - len(data))] + [val]
    # assert len(data) == idx + 1

if __name__ == '__main__':
    main()
    main2()
