import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '15_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    nums = [int(dat) for dat in data[0].split(',')]

    last_said_two_turns_for_number = {}
    last_num = None

    def say(will_say_num, turn_number):
        nonlocal last_num, last_said_two_turns_for_number
        if will_say_num in last_said_two_turns_for_number:
            last_said_two_turns_for_number[will_say_num].append(turn_number)
            last_said_two_turns_for_number[will_say_num] = last_said_two_turns_for_number[will_say_num][-2:]
        else:
            last_said_two_turns_for_number[will_say_num] = [turn_number]
        last_num = will_say_num
        # print("speak", turn_number, will_say_num)

    # NUM_TURNS = 10
    NUM_TURNS = 2020
    # NUM_TURNS = 30000000
    for i in range(NUM_TURNS):
        if i < len(nums):
            speak = nums[i]
            say(nums[i], i)
            continue
        ls_dat = last_said_two_turns_for_number[last_num]
        assert(ls_dat is not None)
        if (len(ls_dat)) == 1:
            say(0, i)
            continue
        say(i - ls_dat[0] - 1, i)

    print(last_num)

# def main2():
#     data = readlines(FILENAME)
#     nums = [int(dat) for dat in data[0].split(',')]

#     last_said_two_turns_for_number = {}
#     last_num = None
#     records = []

#     def say(will_say_num, turn_number):
#         nonlocal last_num, last_said_two_turns_for_number
#         if will_say_num in last_said_two_turns_for_number:
#             last_said_two_turns_for_number[will_say_num].append(turn_number)
#             last_said_two_turns_for_number[will_say_num] = last_said_two_turns_for_number[will_say_num][-2:]
#         else:
#             last_said_two_turns_for_number[will_say_num] = [turn_number]
#         last_num = will_say_num
#         records.append(last_num)
#         res = check_for_cycle()
#         if res:
#             print(res)
#         print("speak", turn_number, will_say_num)

#     # WAIT A SECOND, CYCLES ARE NOT MATHEMATICALLY POSSIBLE NO?
#     # OTHER THAN THE 1,1,1,1,1,1,1 CONTRIVED EXAMPLE
#     # MAYBE ACTUALLY JUST WAIT TO RUN 30M??!?!?
#     def check_for_cycle():
#         nonlocal records
#         specific_anchor = records[-1]
#         if specific_anchor == 0:
#             return False
#         idx = len(records) - 2
#         first_loop = []
#         while idx >= 0:
#             curr = records[idx]
#             if curr == 0:
#                 return False
#             if curr == specific_anchor:
#                 # closes first loop
#                 # check second loop
#                 sec_idx = idx - 1
#                 for i in range(len(first_loop)):
#                     if records[sec_idx] != first_loop[i]:
#                         return False
#                     sec_idx -= 1
#                 if records[sec_idx] != specific_anchor:
#                     return False
#                 print("FOUND A CYCLE", specific_anchor, first_loop)
#                 return True
#             first_loop.append(curr)
#             idx -= 1
#         return False

#     # NUM_TURNS = 10
#     # NUM_TURNS = 2020
#     NUM_TURNS = 30000000
#     for i in range(NUM_TURNS):
#         if i < len(nums):
#             speak = nums[i]
#             say(nums[i], i)
#             continue
#         ls_dat = last_said_two_turns_for_number[last_num]
#         assert(ls_dat is not None)
#         if (len(ls_dat)) == 1:
#             say(0, i)
#             continue
#         say(i - ls_dat[0] - 1, i)

#     print(last_num)

def main2():
    data = readlines(FILENAME)
    nums = [int(dat) for dat in data[0].split(',')]

    last_said_two_turns_for_number = {}
    last_num = None

    def say(will_say_num, turn_number):
        nonlocal last_num, last_said_two_turns_for_number
        if will_say_num in last_said_two_turns_for_number:
            last_said_two_turns_for_number[will_say_num].append(turn_number)
            last_said_two_turns_for_number[will_say_num] = last_said_two_turns_for_number[will_say_num][-2:]
        else:
            last_said_two_turns_for_number[will_say_num] = [turn_number]
        last_num = will_say_num
        # print("speak", turn_number, will_say_num)

    # NUM_TURNS = 10
    # NUM_TURNS = 2020
    NUM_TURNS = 30000000
    for i in range(NUM_TURNS):
        if i < len(nums):
            speak = nums[i]
            say(nums[i], i)
            continue
        ls_dat = last_said_two_turns_for_number[last_num]
        assert(ls_dat is not None)
        if (len(ls_dat)) == 1:
            say(0, i)
            continue
        say(i - ls_dat[0] - 1, i)

    print(last_num)

if __name__ == '__main__':
    main()
    main2()
