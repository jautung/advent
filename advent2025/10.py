import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *
from itertools import combinations
from ortools.linear_solver import pywraplp

# source .venv/bin/activate

FILENAME = '10_dat.txt'
mapper = {}

def parse_line(line):
    splitted = line.split(' ')
    lights = splitted[0][1:-1]
    wirings = [[int(x) for x in a[1:-1].split(',')] for a in splitted[1:-1]]
    joltage = [int(x) for x in splitted[-1][1:-1].split(',')]
    return lights, wirings, joltage

def fully_run(lst):
    running = set()
    for item in lst:
        for x in item:
            if x in running:
                running.remove(x)
            else:
                running.add(x)
    return running

def min_presses(lights, wirings):
    target = set()
    for i in range(len(lights)):
        if lights[i] == "#":
            target.add(i)
    # print(lights, target)

    # print(len(wirings))
    for clicks in range(len(wirings)+1):
        all_combis = combinations(wirings, clicks)
        for combi in all_combis:
            if fully_run(combi) == target:
                return clicks

    # this happens when it is not possible
    assert False

def main():
    data = readlines(FILENAME)
    data = [parse_line(dat) for dat in data]
    # print_2d(data)

    tot = 0
    for d in data:
        lights, wirings, _ = d
        # print(lights, min_presses(lights, wirings))
        tot += min_presses(lights, wirings)
    print(tot)

def min_presses_2(solver, wirings, joltage):
    # print(wirings, joltage)

    num_buttons = len(wirings)

    # Define variables: x1, x2 (integers)
    # The variables are non-negative integers (Integer constraint)
    int_vars = [solver.IntVar(0, solver.infinity(), f'x{i}') for i in range(num_buttons)]

    # Define Constraints
    for slot_index in range(len(joltage)):
        target = joltage[slot_index]

        expression = 0
        for button_index in range(num_buttons):
            if slot_index in wirings[button_index]:
                expression += int_vars[button_index]

        solver.Add(expression == target)

    # Minimize Objective: x1 + x2
    solver.Minimize(sum(int_vars))

    # Solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        # print('Solution:')
        # print(f'Objective value = {solver.Objective().Value()}')
        # button_presses = [int(x.solution_value()) for x in int_vars]
        # print(button_presses)
        # print(sum(button_presses))
        # print(f'x1 = {int(x1.solution_value())}')
        # print(f'x2 = {int(x2.solution_value())}')
        return int(solver.Objective().Value())
    else:
        print('No optimal solution found.')
        assert False
    assert False

def main2():
    data = readlines(FILENAME)
    data = [parse_line(dat) for dat in data]
    # print_2d(data)

    solver = pywraplp.Solver.CreateSolver('SCIP_MIXED_INTEGER_PROGRAMMING')
    if not solver:
        print("Solver not available")
        assert False
        return

    cases = len(data)

    tot = 0
    for index, d in enumerate(data):
        _, wirings, joltage = d
        tot += min_presses_2(solver, wirings, joltage)
        # print(f'solved {index+1} out of {cases}')
    print(tot)


if __name__ == '__main__':
    main()
    main2()
