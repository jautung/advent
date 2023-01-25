import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '11_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    data = [parse_data(dat) for dat in data]
    # data = [int(dat) for dat in data]
    # print_2d(data)
    max_monkey_num = None
    items_for_monkeys = def_dict([])
    for monkey_num, starting_items, op, divisible_by, true_throw, false_throw in data:
        items_for_monkeys[monkey_num] = starting_items
        if max_monkey_num == None or monkey_num > max_monkey_num:
            max_monkey_num = monkey_num
    # print(items_for_monkeys)
    # print(max_monkey_num)
    inspected = def_dict(0)
    ROUNDS = 20
    for i in range(1, ROUNDS+1):
        items_for_monkeys, data, max_monkey_num = conduct_round(items_for_monkeys, data, max_monkey_num, inspected)
        # print(i, items_for_monkeys)
    # print(inspected)
    sortzz = sorted(inspected.values())
    print(sortzz[-1] * sortzz[-2])

def conduct_round(items_for_monkeys, data, max_monkey_num, inspected):
    for i in range(max_monkey_num+1):
        monkey_num, starting_items, op, divisible_by, true_throw, false_throw = data[i]
        starting_items = items_for_monkeys[i]
        for starting_item in starting_items:
            items_for_monkeys[i] = []
            process_item(starting_item, op, divisible_by, true_throw, false_throw, items_for_monkeys)
            inspected[i] += 1
    return items_for_monkeys, data, max_monkey_num

def parse_data(dat):
    monkey_num = int(dat[0].split()[1][:-1])
    starting_items = [int(i.strip()) for i in dat[1].split(':')[1:][0].split(',')]
    operation = dat[2].split(':')[1:][0].strip().split('=')[1:][0].strip()
    if len(operation.split('*')) > 1:
        if operation.split('*')[1].strip() == 'old':
            op = ('square',)
        else:
            op = ('times', int(operation.split('*')[1].strip()))
    elif len(operation.split('+')) > 1:
        if operation.split('+')[1].strip() == 'old':
            op = ('double',)
        else:
            op = ('plus', int(operation.split('+')[1].strip()))
    divisible_by = int(dat[3].split()[-1].strip())
    true_throw = int(dat[4].split()[-1].strip())
    false_throw = int(dat[5].split()[-1].strip())
    # print(monkey_num, starting_items, op, divisible_by, true_throw, false_throw)
    return (monkey_num, starting_items, op, divisible_by, true_throw, false_throw)

def process_item(starting_item, op, divisible_by, true_throw, false_throw, items_for_monkeys):
    if op[0] == 'square':
        after_item = starting_item * starting_item
    elif op[0] == 'times':
        after_item = starting_item * op[1]
    elif op[0] == 'double':
        after_item = starting_item + starting_item
    elif op[0] == 'plus':
        after_item = starting_item + op[1]
    after_item_2 = after_item // 3
    if after_item_2 % divisible_by == 0:
        # print('throwing', after_item_2, 'to', true_throw)
        items_for_monkeys[true_throw].append(after_item_2)
    else:
        # print('throwing', after_item_2, 'to', false_throw)
        items_for_monkeys[false_throw].append(after_item_2)

def main2():
    data = readlines_split_by_newlines(FILENAME)
    data = [parse_data(dat) for dat in data]
    # data = [int(dat) for dat in data]
    # print_2d(data)
    max_monkey_num = None
    all_divisible_bys = 1
    items_for_monkeys = def_dict([])
    for monkey_num, starting_items, op, divisible_by, true_throw, false_throw in data:
        all_divisible_bys *= divisible_by
        items_for_monkeys[monkey_num] = starting_items
        if max_monkey_num == None or monkey_num > max_monkey_num:
            max_monkey_num = monkey_num
    # print(items_for_monkeys)
    # print(max_monkey_num)
    # print(all_divisible_bys)
    inspected = def_dict(0)
    ROUNDS = 10000
    for i in range(1, ROUNDS+1):
        items_for_monkeys, data, max_monkey_num = conduct_round_2(items_for_monkeys, data, max_monkey_num, inspected, all_divisible_bys)
        # print(i, items_for_monkeys)
    # print(inspected)
    sortzz = sorted(inspected.values())
    print(sortzz[-1] * sortzz[-2])

def conduct_round_2(items_for_monkeys, data, max_monkey_num, inspected, all_divisible_bys):
    for i in range(max_monkey_num+1):
        monkey_num, starting_items, op, divisible_by, true_throw, false_throw = data[i]
        starting_items = items_for_monkeys[i]
        for starting_item in starting_items:
            items_for_monkeys[i] = []
            process_item_2(starting_item, op, divisible_by, true_throw, false_throw, items_for_monkeys, all_divisible_bys)
            inspected[i] += 1
    return items_for_monkeys, data, max_monkey_num

def process_item_2(starting_item, op, divisible_by, true_throw, false_throw, items_for_monkeys, all_divisible_bys):
    if op[0] == 'square':
        after_item = starting_item * starting_item
    elif op[0] == 'times':
        after_item = starting_item * op[1]
    elif op[0] == 'double':
        after_item = starting_item + starting_item
    elif op[0] == 'plus':
        after_item = starting_item + op[1]
    after_item_2 = after_item % all_divisible_bys
    if after_item_2 % divisible_by == 0:
        # print('throwing', after_item_2, 'to', true_throw)
        items_for_monkeys[true_throw].append(after_item_2)
    else:
        # print('throwing', after_item_2, 'to', false_throw)
        items_for_monkeys[false_throw].append(after_item_2)

if __name__ == '__main__':
    main()
    main2()
