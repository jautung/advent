import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
mapper = {}

def main():
    data = [int(i) for i in readlines(FILENAME)[0].split(',')]
    # data = [int(dat) for dat in data]
    # print(data)
    curr_pos = 0

    data[1] = 12
    data[2] = 2

    while True:
        # print(data)
        curr_opcode = data[curr_pos]
        if curr_opcode == 1:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            data[out] = data[inp1] + data[inp2]
        elif curr_opcode == 2:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            data[out] = data[inp1] * data[inp2]
        elif curr_opcode == 99:
            print(data[0])
            return
        else:
            assert(False)
        curr_pos += 4

def main2():
    data = [int(i) for i in readlines(FILENAME)[0].split(',')]
    # data = [int(dat) for dat in data]
    # print(data)


    def get_out(noun, verb, data):
        data = data[:]

        data[1] = noun
        data[2] = verb

        curr_pos = 0
        while True:
            # print(data)
            curr_opcode = data[curr_pos]
            if curr_opcode == 1:
                inp1 = data[curr_pos+1]
                inp2 = data[curr_pos+2]
                out = data[curr_pos+3]
                data[out] = data[inp1] + data[inp2]
            elif curr_opcode == 2:
                inp1 = data[curr_pos+1]
                inp2 = data[curr_pos+2]
                out = data[curr_pos+3]
                data[out] = data[inp1] * data[inp2]
            elif curr_opcode == 99:
                return data[0]
                return
            else:
                assert(False)
            curr_pos += 4

    # print(get_out(12,2, data))
    for i in range(100):
        for j in range(100):
            test = get_out(i,j, data)
            if test == 19690720:
                print(100*i+j)
                return
            # print(i,j,d)

if __name__ == '__main__':
    main()
    main2()
