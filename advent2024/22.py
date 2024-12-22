import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *
from itertools import product

FILENAME = '22_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    # print(data)

    def evolve(number):
        def mix(value, number):
            return value ^ number
        def prune(number):
            return number % 16777216
        first_result = number * 64
        number = mix(first_result, number)
        number = prune(number)
        second_result = number // 32
        number = mix(second_result, number)
        number = prune(number)
        third_result = number * 2048
        number = mix(third_result, number)
        number = prune(number)
        return number 

    # x = 123
    # for i in range(10):
    #     x = evolve(x)
    #     print(i, x)

    def evolve_n(number, times):
        for _ in range(2000):
            number = evolve(number)
        return number

    c = 0
    for d in data:
        # print(d, evolve_n(d, 2000))
        c += evolve_n(d, 2000)
    print(c)

def main2():
    data = readlines(FILENAME)
    data = [int(dat) for dat in data]
    # print(data)

    def evolve(number):
        def mix(value, number):
            return value ^ number
        def prune(number):
            return number % 16777216
        first_result = number * 64
        number = mix(first_result, number)
        number = prune(number)
        second_result = number // 32
        number = mix(second_result, number)
        number = prune(number)
        third_result = number * 2048
        number = mix(third_result, number)
        number = prune(number)
        return number 

    def generate_info(number):
        all_prices = dict()
        last_4_differences = []
        for _ in range(2000):
            prev_number = number
            number = evolve(prev_number)
            difference = (number%10) - (prev_number%10)
            price = number%10
            if len(last_4_differences) < 4:
                last_4_differences.append(difference)
                if len(last_4_differences) == 4:
                    frozen_last_4_differences = tuple(last_4_differences)
                    if frozen_last_4_differences not in all_prices:
                        all_prices[frozen_last_4_differences] = price
            else:
                last_4_differences = last_4_differences[1:] + [difference]
                frozen_last_4_differences = tuple(last_4_differences)
                if frozen_last_4_differences not in all_prices:
                    all_prices[frozen_last_4_differences] = price
        return all_prices

    # print(generate_info(1)[(-2,1,-1,3)])
    # print(generate_info(2)[(-2,1,-1,3)])
    # print((-2,1,-1,3) in generate_info(3))
    # print(generate_info(2024)[(-2,1,-1,3)])

    all_infos = [generate_info(d) for d in data]

    values_for_target = dict()
    targets = product(range(-9,10), repeat=4)
    for target in targets:
        value_for_target = sum([info[target] for info in all_infos if target in info])
        values_for_target[target] = value_for_target

    # print(values_for_target[(-2,1,-1,3)])
    best_target = max(values_for_target, key=values_for_target.get)
    # print(best_target)
    print(values_for_target[best_target])
    

if __name__ == '__main__':
    # main()
    main2()
