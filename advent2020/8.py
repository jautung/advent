import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '8_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    glob = 0
    indx = 0
    indx_hist = []
    while True:
        if indx in indx_hist:
            print(glob)
            break
        indx_hist.append(indx)
        l = data[indx]
        ins = l.split(' ')
        instr = ins[0]
        arg = int(ins[1])
        # print(instr, arg)
        if instr == 'nop':
            indx += 1
        elif instr == 'jmp':
            indx += arg
        elif instr == 'acc':
            indx += 1
            glob += arg
    # print(data)

def runner(prog):
    glob = 0
    indx = 0
    indx_hist = []
    while True:
        if indx == len(prog):
            print('it worked')
            print(glob)
            return True # correct program
        if indx in indx_hist:
            # print('x')
            return False # bad program
        indx_hist.append(indx)
        l = prog[indx]
        ins = l.split(' ')
        instr = ins[0]
        arg = int(ins[1])
        # print(instr, arg)
        if instr == 'nop':
            indx += 1
        elif instr == 'jmp':
            indx += arg
        elif instr == 'acc':
            indx += 1
            glob += arg
    # print(data)

def main2():
    data = readlines(FILENAME)
    for index, d in enumerate(data):
        if d.startswith('nop'):
            new_data = copy.deepcopy(data)
            new_data[index] = 'jmp' + new_data[index][3:]
            # new_data[index]
            runner(new_data)
        elif d.startswith('jmp'):
            new_data = copy.deepcopy(data)
            new_data[index] = 'nop' + new_data[index][3:]
            # new_data[index]
            runner(new_data)
            
    # runner(data)

if __name__ == '__main__':
    main()
    main2()
