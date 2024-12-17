import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '17_dat.txt'
mapper = {}

def run_prog(init_a, init_b, init_c, prog):
    reg_a = init_a
    reg_b = init_b
    reg_c = init_c
    ip = 0

    def get_combo_operand(operand):
        if operand == 0:
            return 0
        elif operand == 1:
            return 1
        elif operand == 2:
            return 2
        elif operand == 3:
            return 3
        elif operand == 4:
            return reg_a
        elif operand == 5:
            return reg_b
        elif operand == 6:
            return reg_c
        elif operand == 7:
            assert False

    output = []
    while True:
        if ip >= len(prog):
            break
        opcode = prog[ip]
        operand = prog[ip+1]
        if opcode == 0: # adv
            numerator = reg_a
            operand_value = get_combo_operand(operand)
            denominator = 2 ** operand_value
            reg_a = numerator // denominator
        elif opcode == 1: # bxl
            reg_b = reg_b ^ operand
        elif opcode == 2: # bst
            operand_value = get_combo_operand(operand)
            reg_b = (operand_value % 8)
        elif opcode == 3: # jnz
            if reg_a == 0:
                pass
            else:
                ip = operand
                continue
        elif opcode == 4: # bxc
            reg_b = reg_b ^ reg_c
        elif opcode == 5: # out
            operand_value = get_combo_operand(operand)
            output.append((operand_value % 8))
        elif opcode == 6: # bdv
            numerator = reg_a
            operand_value = get_combo_operand(operand)
            denominator = 2 ** operand_value
            reg_b = numerator // denominator
        elif opcode == 7: # cdv
            numerator = reg_a
            operand_value = get_combo_operand(operand)
            denominator = 2 ** operand_value
            reg_c = numerator // denominator
        ip += 2

    return (reg_a, reg_b, reg_c, output)



def main():
    data = readlines(FILENAME)
    reg_a = int(data[0].split(":")[1].strip())
    reg_b = int(data[1].split(":")[1].strip())
    reg_c = int(data[2].split(":")[1].strip())
    prog = [int(a.strip()) for a in data[4].split(":")[1].split(',')]

    # print(reg_a)
    # print(reg_b)
    # print(reg_c)
    # print(prog)

    res = run_prog(reg_a,reg_b,reg_c,prog)
    # print(res)
    print(','.join([str(i) for i in res[3]]))


def main2():
    data = readlines(FILENAME)
    # reg_a = int(data[0].split(":")[1].strip())
    reg_b = int(data[1].split(":")[1].strip())
    reg_c = int(data[2].split(":")[1].strip())
    prog = [int(a.strip()) for a in data[4].split(":")[1].split(',')]

    # print(reg_a)
    # print(reg_b)
    # print(reg_c)
    # print(prog)

    # res = run_prog(117440,reg_b,reg_c,prog)
    # for reg_a in range(100):
    #     res = run_prog(reg_a,reg_b,reg_c,prog)
    #     # print(res)
    #     the_out = ','.join([str(i) for i in res[3]])
    #     if the_out.startswith('2'):
    #         print(oct(reg_a), ','.join([str(i) for i in res[3]]))

    # print()
    # for reg_a in range(1000):
    #     res = run_prog(reg_a,reg_b,reg_c,prog)
    #     # print(res)
    #     the_out = ','.join([str(i) for i in res[3]])
    #     if the_out.startswith('2,4'):
    #         print(oct(reg_a), ','.join([str(i) for i in res[3]]))

    # print()
    # for reg_a in range(10000):
    #     res = run_prog(reg_a,reg_b,reg_c,prog)
    #     # print(res)
    #     the_out = ','.join([str(i) for i in res[3]])
    #     if the_out.startswith('2,4,1'):
    #         print(oct(reg_a), ','.join([str(i) for i in res[3]]))


    # wait this only depends on the last 10 bits of a I think
    # so we can precompute this to be 1024 options?
    def my_func_of_a(a):
        k = a & 7
        return (k ^ 5 ^ ((a >> (k ^ 1)) & 7))

    # for i in range(0, 2**10):
    #     print(i, my_func_of_a(i), my_func_of_a(i + 2**10))

    # yea verified

    cached = dict()
    for i in range(0, 2**10):
        cached[i] = my_func_of_a(i)

    TARGET = [2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0]

    # def my_specific_prog(a):
    #     # out = []
    #     curr_i = 0
    #     while a > 0:
    #         # k = a & 7
    #         # thing = (k ^ 5 ^ ((a >> (k ^ 1)) & 7))
    #         # thing = my_func_of_a(a)
    #         thing = cached[a & (2**10-1)]
    #         if thing != TARGET[curr_i]:
    #             return False
    #         # out.append((k ^ 5 ^ (a >> (k ^ 1))) & 7)
    #         a = a >> 3
    #         curr_i += 1
    #     return True
    #     # return out

    def my_specific_prog(a):
        out = []
        curr_i = 0
        while a > 0:
            # k = a & 7
            # thing = (k ^ 5 ^ ((a >> (k ^ 1)) & 7))
            # thing = my_func_of_a(a)
            thing = cached[a & (2**10-1)]
            # if thing != TARGET[curr_i]:
                # return False
            out.append(thing)
            a = a >> 3
            curr_i += 1
        # return True
        return out

    # for i in range(1, 100000000):
    #     if my_specific_prog(i):
    #         print(i, run_prog(i,reg_b,reg_c,prog), my_specific_prog(i))

    # print(5 << (15*3), run_prog(5 << (15*3),reg_b,reg_c,prog), my_specific_prog(5 << (15*3)))
    # print(5 << (15*3) + 6 << (14*3), run_prog(5 << (15*3) + 6 << (14*3),reg_b,reg_c,prog), my_specific_prog(5 << (15*3) + 6 << (14*3)))
    # print(cached[46])
    # test = 5 * 8**15 + 6 * 8**14
    # test = 6 << (14*3)
    # print(oct(test), run_prog(test,reg_b,reg_c,prog), my_specific_prog(test))

    # # for i in range(1, 1000000):
    # for i in range(8**15, 8**16):
    # # for i in range(8**15, 8**15+10000000):
    #     if i % 8**7 == 0:
    #         print(oct(i))
    #     if my_specific_prog(i):
    #         print(i, "YAY")
    #         break
    # # are we supposed to write an equation with 16 variables (0-7) and solve?

    # fixup 16x of 3-bit things of a, from highest to lowest
    # because highest to lowest, we can always choose lowest positive int etc.
    final_a_pieces = [] # each item is a list from lowest to highest possibility, future items assume the lowest, and we backtrack if needed
    def find_all_inputs_to_get(target, addition_to_a):
        # print('find_all_inputs_to_get', target, addition_to_a)
        outs = []
        for i in range(0, 2**3):
            if cached[(addition_to_a + i) & (2**10-1)] == target:
                # return i
                outs.append(i)
        # print('outs', outs)
        return outs
        # assert False

    # position = 0
    while len(final_a_pieces) != 16:
        addition_to_a = 0
        if len(final_a_pieces) > 0:
            addition_to_a += (final_a_pieces[-1][0] * 8)
        if len(final_a_pieces) > 1:
            addition_to_a += (final_a_pieces[-2][0] * 8 * 8)
        if len(final_a_pieces) > 2:
            addition_to_a += (final_a_pieces[-3][0] * 8 * 8 * 8)
        res = find_all_inputs_to_get(TARGET[-len(final_a_pieces)-1], addition_to_a)
        if len(res) == 0:
            # backtrack
            backtrack_to = 1
            did_it = False
            while backtrack_to < len(final_a_pieces):
                if len(final_a_pieces[-backtrack_to]) > 0:
                    final_a_pieces[-backtrack_to] = final_a_pieces[-backtrack_to][1:]
                    did_it = True
                    break
                backtrack_to += 1
            assert did_it
            continue
        final_a_pieces.append(res)
        # position += 1
        # print('final_a_pieces', final_a_pieces)
    # print([a[0] for a in final_a_pieces])
    running = 0
    for a in final_a_pieces:
        running += a[0]
        running *= 8

    test = running//8
    print(test)
    print(oct(test)) # 202322348616234
    print(oct(test), run_prog(test,reg_b,reg_c,prog), my_specific_prog(test))


    # 2,4, 1,1, 7,5, 0,3, 1,4, 4,5, 5,5, 3,0
    # 
    # 2,4 -> reg_b = reg_a % 8             | store a modulo 8 in b
    # 1,1 -> reg_b = reg_b ^ 1             | flip the ones position (b+=1 for even b, b-=1 for odd b)
    # 7,5 -> reg_c = reg_a // (2 ** reg_b) | do stuff... and store in reg_c
    # 0,3 -> reg_a = reg_a // 8            | take the other part of a (#mult of 8) and store in a
    # 1,4 -> reg_b = reg_b ^ 4             | flip the 100s position for b
    # 4,5 -> reg_b = reg_b ^ reg_c         | ???
    # 5,5 -> OUTPUT reg_b (mod 8)
    # 3,0 -> IF a == 0 ends | ELSE jump back to start
    # 
    # some kind of long division program by 8 for whatever's stored in a
    # and somehow outputting stuff along the way
    # start with k = reg_b (incremental positions in octal of a, working backwards)
    # b = k XOR 1
    # c = a / 2^(k XOR 1)
    # b = k XOR 1 XOR 4
    # b = k XOR 1 XOR 4 XOR (a / 2^(k XOR 1))
    # OUTPUT k XOR 1 XOR 4 XOR (a / 2^(k XOR 1))
    # 
    # slide octal a to the right, truncating, and repeat again
    # each output will be [k XOR 1 XOR 4 XOR (a / 2^(k XOR 1))] where k is the octal 'ones' position of a
    # each output will be [k XOR 5 XOR (a truncated (k XOR 1) spaces)] where k is the octal 'ones' position of a
    #
    # I guess we can do approximate size of a
    # a is sliced by 8 every time it outputs a number, so 0-7 output 1 number, 8-8^2-1 output 2 digits, 8^2-8^3-1 output 3 digits,
    # 8^15-8^16-1 output 16 digits

    # for reg_a in range(8**15, 8**15 + 100):
    # for reg_a in range(8**15, 8**16):
    #     res = run_prog(reg_a,reg_b,reg_c,prog)
    #     # print(res)
    #     the_out = ','.join([str(i) for i in res[3]])
    #     # if the_out.startswith('2,4,1'):
    #     print(oct(reg_a), ','.join([str(i) for i in res[3]]))



if __name__ == '__main__':
    # regs = run_prog(0,0,9,[2,6])
    # print('final', regs)
    # regs = run_prog(10,0,0,[5,0,5,1,5,4])
    # print('final', regs)
    # regs = run_prog(2024,0,0,[0,1,5,4,3,0])
    # print('final', regs)
    # regs = run_prog(0,29,0,[1,7])
    # print('final', regs)
    # regs = run_prog(0,2024,43690,[4,0])
    # print('final', regs)
    main()
    main2()
