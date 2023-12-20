import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '20_dat.txt'
# mapper = {}

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)
    mapper = dict()
    for item in data:
        ls, rs = item
        if ls[0] == None:
            START = rs
        else:
            module = ls[1]
            assert(module not in mapper)
            mapper[module] = (ls[0], rs) # (type, outputs)
    # print(START)
    # print(mapper)

    on_off_state = dict()
    for key in mapper:
        receiver_type, _ = mapper[key]
        if receiver_type == 'FF':
            on_off_state[key] = 'OFF'
    conj_memory = dict()
    for key in mapper:
        receiver_type, _ = mapper[key]
        if receiver_type == 'CONJ':
            conj_memory[key] = dict()
            for key_2 in mapper:
                if key in mapper[key_2][1]:
                    conj_memory[key][key_2] = 'LOW'
    # print(conj_memory)

    # press the broadcaster
    signals_in_queue = []
    counters = {'HIGH': 0, 'LOW': 0}
    
    def run_signal():
        counters['LOW'] += 1
        for i in START:
            signals_in_queue.append(('broadcaster', 'LOW', i))
        # print(signals_in_queue)
        # this is starting condition
        
        while len(signals_in_queue) > 0:
            first_signal = signals_in_queue.pop(0)
            sender, signal_type, receiver = first_signal
            counters[signal_type] += 1
            # print(sender, signal_type, receiver)
            # print(mapper, receiver)
            if receiver not in mapper:
                continue
            receiver_type, receiver_next_dests = mapper[receiver]
            if receiver_type == 'CONJ':
                conj_memory[receiver][sender] = signal_type
                if all([conj_memory[receiver][inptter] == 'HIGH' for inptter in conj_memory[receiver]]):
                    for i in receiver_next_dests:
                        signals_in_queue.append((receiver, 'LOW', i))
                else:
                    for i in receiver_next_dests:
                        signals_in_queue.append((receiver, 'HIGH', i))
            elif receiver_type == 'FF':
                if signal_type == 'HIGH':
                    pass
                elif signal_type == 'LOW':
                    if on_off_state[receiver] == 'OFF':
                        on_off_state[receiver] = 'ON'
                        for i in receiver_next_dests:
                            signals_in_queue.append((receiver, 'HIGH', i))
                    elif on_off_state[receiver] == 'ON':
                        on_off_state[receiver] = 'OFF'
                        for i in receiver_next_dests:
                            signals_in_queue.append((receiver, 'LOW', i))
                    else:
                        assert(False)                    
                else:
                    assert(False)
            else:
                assert(False)
    # print("first")
    # run_signal()
    # # print(on_off_state)
    # print("second")
    # run_signal()
    # print("third")
    # run_signal()
    # print("forth")
    # run_signal()
    # print(on_off_state)
    # print(conj_memory)
    for _ in range(1000):
        run_signal()
    # print(counters)
    print(counters['HIGH']*counters['LOW'])

def parse(line):
    a = line.split(' -> ')
    assert(len(a) == 2)
    lhs = a[0]
    rhs = a[1]
    rs = [x.strip() for x in rhs.split(',')]
    if lhs[0] == '%':
        ls = ('FF', lhs[1:].strip())
    elif lhs[0] == '&':
        ls = ('CONJ', lhs[1:].strip())
    else:
        assert(lhs == 'broadcaster')
        ls = (None, lhs.strip())
    return ls, rs

def main2():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    # print_2d(data)
    mapper = dict()
    for item in data:
        ls, rs = item
        if ls[0] == None:
            START = rs
        else:
            module = ls[1]
            assert(module not in mapper)
            mapper[module] = (ls[0], rs) # (type, outputs)
    # print(START)
    # print(mapper)

    hash_1 = []
    hash_2 = []
    on_off_state = dict()
    for key in mapper:
        receiver_type, _ = mapper[key]
        if receiver_type == 'FF':
            on_off_state[key] = 'OFF'
            hash_1.append(key)
    conj_memory = dict()
    for key in mapper:
        receiver_type, _ = mapper[key]
        if receiver_type == 'CONJ':
            conj_memory[key] = dict()
            for key_2 in mapper:
                if key in mapper[key_2][1]:
                    conj_memory[key][key_2] = 'LOW'
                    hash_2.append((key, key_2))
    # print(conj_memory)
    def minify_1():
        return ''.join(['1' if on_off_state[x] == 'ON' else '0' for x in hash_1])
    def minify_2():
        return ''.join(['1' if conj_memory[x[0]][x[1]] == 'ON' else '0' for x in hash_2])

    # press the broadcaster
    signals_in_queue = []
    # counters = {'HIGH': 0, 'LOW': 0}
    has_happened = []
    
    def run_signal():
        # counters['LOW'] += 1
        for i in START:
            signals_in_queue.append(('broadcaster', 'LOW', i))
        # print(signals_in_queue)
        # this is starting condition
        
        while len(signals_in_queue) > 0:
            first_signal = signals_in_queue.pop(0)
            sender, signal_type, receiver = first_signal
            if signal_type == 'LOW' and receiver == 'rx':
                has_happened.append(1)
            if sender == 'mk' and receiver == 'kl' and signal_type == 'HIGH':
                print(f"hello there mk {button_presses}")
            if sender == 'fp' and receiver == 'kl' and signal_type == 'HIGH':
                print(f"hello there fp {button_presses}")
            if sender == 'xt' and receiver == 'kl' and signal_type == 'HIGH':
                print(f"hello there xt {button_presses}")
            if sender == 'zc' and receiver == 'kl' and signal_type == 'HIGH':
                print(f"hello there zc {button_presses}")
            # counters[signal_type] += 1
            # print(sender, signal_type, receiver)
            # print(mapper, receiver)
            if receiver not in mapper:
                continue
            receiver_type, receiver_next_dests = mapper[receiver]
            if receiver_type == 'CONJ':
                conj_memory[receiver][sender] = signal_type
                if all([conj_memory[receiver][inptter] == 'HIGH' for inptter in conj_memory[receiver]]):
                    for i in receiver_next_dests:
                        signals_in_queue.append((receiver, 'LOW', i))
                else:
                    for i in receiver_next_dests:
                        signals_in_queue.append((receiver, 'HIGH', i))
            elif receiver_type == 'FF':
                if signal_type == 'HIGH':
                    pass
                elif signal_type == 'LOW':
                    if on_off_state[receiver] == 'OFF':
                        on_off_state[receiver] = 'ON'
                        for i in receiver_next_dests:
                            signals_in_queue.append((receiver, 'HIGH', i))
                    elif on_off_state[receiver] == 'ON':
                        on_off_state[receiver] = 'OFF'
                        for i in receiver_next_dests:
                            signals_in_queue.append((receiver, 'LOW', i))
                    else:
                        assert(False)                    
                else:
                    assert(False)
            else:
                assert(False)
    # print("first")
    # run_signal()
    # # print(on_off_state)
    # print("second")
    # run_signal()
    # print("third")
    # run_signal()
    # print("forth")
    # run_signal()
    # print(on_off_state)
    # print(conj_memory)
    button_presses = 0
    caching_1 = set()
    caching_2 = set()
    while True:
        button_presses += 1
        if button_presses % 10000 == 0:
            print(f"pressing button for {button_presses} time")
            print(minify_1())
        run_signal()
        if len(has_happened) > 0:
            break
        # print(button_presses)
        # print(minify_1())
        # print(minify_2())
        # print()
        if minify_1() in caching_1:
            print("OH WOW REPEAT 1")
        if minify_2() in caching_2:
            # print("OH WOW REPEAT 2")
            pass
        caching_1.add(minify_1())
        caching_2.add(minify_2())
        # print(counters)
        # if button_presses == 5:
        #     break
    print(button_presses)
    # print(counters)
    # print(counters['HIGH']*counters['LOW'])
    # THIS HAS TO BE SOME KIND OF LCM THING BECAUSE THERE WON'T BE REPEATS
    # BUT HOW TO BREAK THIS APART INTO DISJOING LOOPS IS THE QUESTION
    # BECAUSE THIS IS EFFECTIVELY SOME KIND OF TURING MACHINE WHERE ALL THE INPUTS ARE INTERCONNECTED
    # I GUESS WE NEED TO MAKE USE OF SOME SPECIFIC DOMAIN KNOWLEDGE OTHERWISE ITS NOT GUNNA WORK
    # IF WE JUST TREAT THE THING AS A BLACK BOX WITH SOME WEIRD STATE TRANSITION BETWEEN
    # 2^48 -> 2^48 SPACE
    # ok i guess we can just hack by looking at the input and manually taking lcm????
'''
hello there fp 3767
hello there zc 3923
hello there mk 3931
hello there xt 4007
hello there fp 7534
hello there zc 7846
hello there mk 7862
hello there xt 8014
pressing button for 10000 time
001100110101011010100001001100100110010011100100
hello there fp 11301
hello there zc 11769
hello there mk 11793
hello there xt 12021
hello there fp 15068
hello there zc 15692
hello there mk 15724
hello there xt 16028
hello there fp 18835
hello there zc 19615
hello there mk 19655
pressing button for 20000 time
000110010010100111100000001100100000011000011100
hello there xt 20035
hello there fp 22602
hello there zc 23538
hello there mk 23586
hello there xt 24042
'''

'''
000110010010100111100000001100100000011000011100
001100110101011010100001001100100110010011100100
hello there fp 11301
hello there fp 15068
hello there fp 18835
hello there fp 22602

hello there fp 3767

hello there fp 7534
hello there mk 11793
hello there mk 15724
hello there mk 19655
hello there mk 23586

hello there mk 3931

hello there mk 7862
hello there xt 12021
hello there xt 16028
hello there xt 20035
hello there xt 24042

hello there xt 4007

hello there xt 8014
hello there zc 11769
hello there zc 15692
hello there zc 19615
hello there zc 23538

hello there zc 3923

hello there zc 7846
pressing button for 10000 time
pressing button for 20000 time
'''

'''
>>> 3767*3931*4007*3923
232774988886497
'''

if __name__ == '__main__':
    main()
    main2()
