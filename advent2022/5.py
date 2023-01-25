import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    stacks = data[0][:-1]
    instructions = data[1]
    # data = [int(dat) for dat in data]
    # print(stacks)
    ress = []
    for row in stacks:
        res = []
        for i in range(1, len(row), 4):
            res.append(row[i])
        ress.append(res)
        # print(row[1], row[5], row[9])
    ress = transpose(reversed(ress))
    final_stacks = dict()
    for idx, i in enumerate(ress):
        final_stacks[idx+1]= list(filter(lambda x: x != ' ', list(i)))
    # for idx, final_stack in final_stacks.items():
    #     print(idx, final_stack)
    
    instructions = [instruction.split() for instruction in instructions]
    instructions = [(int(instruction[1]), int(instruction[3]), int(instruction[5])) for instruction in instructions]
    # for i in instructions:
    #     print(i)

    def perform(instr, stacks):
        n, fr, to = instr
        moving = stacks[fr][-n:]
        placed = list(reversed(moving))
        stacks[fr] = stacks[fr][:-n]
        stacks[to] = stacks[to] + placed

    for i in instructions:
        perform(i, final_stacks)

    # for idx, final_stack in final_stacks.items():
    #     print(idx, final_stack)

    print(''.join([i[1][-1] for i in sorted([(idx, final_stack) for idx, final_stack in final_stacks.items()])]))

def main2():
    data = readlines_split_by_newlines(FILENAME)
    stacks = data[0][:-1]
    instructions = data[1]
    # data = [int(dat) for dat in data]
    # print(stacks)
    ress = []
    for row in stacks:
        res = []
        for i in range(1, len(row), 4):
            res.append(row[i])
        ress.append(res)
        # print(row[1], row[5], row[9])
    ress = transpose(reversed(ress))
    final_stacks = dict()
    for idx, i in enumerate(ress):
        final_stacks[idx+1]= list(filter(lambda x: x != ' ', list(i)))
    # for idx, final_stack in final_stacks.items():
    #     print(idx, final_stack)
    
    instructions = [instruction.split() for instruction in instructions]
    instructions = [(int(instruction[1]), int(instruction[3]), int(instruction[5])) for instruction in instructions]
    # for i in instructions:
    #     print(i)

    def perform(instr, stacks):
        n, fr, to = instr
        moving = stacks[fr][-n:]
        placed = moving
        stacks[fr] = stacks[fr][:-n]
        stacks[to] = stacks[to] + placed

    for i in instructions:
        perform(i, final_stacks)

    # for idx, final_stack in final_stacks.items():
    #     print(idx, final_stack)

    print(''.join([i[1][-1] for i in sorted([(idx, final_stack) for idx, final_stack in final_stacks.items()])]))

if __name__ == '__main__':
    main()
    main2()
