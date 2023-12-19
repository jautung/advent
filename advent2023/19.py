import time
import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '19_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    first = data[0]
    second = data[1]
    parsed_first = [parse_f(a) for a in first]
    parsed_second = [parse_s(a) for a in second]
    # print_2d(parsed_first)
    # print_2d(parsed_second)
    rule_mapper = dict()
    for x in parsed_first:
        name, cases, default_catch = x
        rule_mapper[name] = (cases, default_catch)
    ret = 0
    for item_dict in parsed_second:
        result = apply_rules(item_dict, rule_mapper)
        # print(item_dict, result)
        if result == 'A':
            ret += item_dict['x'] + item_dict['m'] + item_dict['a'] + item_dict['s']
    print(ret)

def apply_rules(item_dict, rule_mapper):
    current_rule_name = 'in'
    while True:
        rule_to_apply = rule_mapper[current_rule_name]
        output_of_rule = apply_rule(item_dict, rule_to_apply)
        if output_of_rule == 'A' or output_of_rule == 'R':
            return output_of_rule
        current_rule_name = output_of_rule

def apply_rule(item_dict, rule_to_apply):
    cases, default_catch = rule_to_apply
    for case in cases:
        if match_case(item_dict, case[0]):
            return case[1]
    return default_catch

def match_case(item_dict, operators):
    op, var, val = operators
    if op == '<':
        return item_dict[var] < val
    elif op == '>':
        return item_dict[var] > val
    assert(False)

def parse_f(a):
    x = a.split('{')
    name = x[0]
    rules = x[1][:-1]
    rules_lst = rules.split(',')
    cases = [parse_rule(a) for a in rules_lst[:-1]]
    default_catch = rules_lst[-1]
    return name, cases, default_catch

def parse_rule(rule):
    x = rule.split(':')
    output = x[1]
    # input = x[0]
    if '<' in x[0]:
        y = x[0].split('<')
        y[0], int(y[1])
        return ('<', y[0], int(y[1])), output
    elif '>' in x[0]:
        y = x[0].split('>')
        y[0], int(y[1])
        return ('>', y[0], int(y[1])), output
    assert(False)

def parse_s(a):
    inner = a[1:-1]
    scores = inner.split(',')
    ret = dict()
    for i in [x.split('=') for x in scores]:
        ret[i[0]] = int(i[1])
    return ret

def main2():
    data = readlines_split_by_newlines(FILENAME)
    first = data[0]
    parsed_first = [parse_f(a) for a in first]
    rule_mapper = dict()
    for x in parsed_first:
        name, cases, default_catch = x
        rule_mapper[name] = (cases, default_catch)
    # keyframes = dict()
    # keyframes['x'] = []
    # keyframes['m'] = []
    # keyframes['a'] = []
    # keyframes['s'] = []
    # for item in parsed_first:
    #     _, cases, _ = item
    #     for case in cases:
    #         _, var, val = case[0]
    #         keyframes[var].append(val)
    # print(len(keyframes['x']) * len(keyframes['m']) * len(keyframes['a']) * len(keyframes['s']))

    # want to just go and keep track of 'A' and 'R's
    # a_list = [<conditions to be met>, <conditions to be met>, <conditions to be met>, ...]
    # r_list = [<conditions to be met>, <conditions to be met>, <conditions to be met>, ...]
    # <conditions to be met> = [<condition to be met>, <condition to be met>, ...]
    # <condition to be met> = op, var, val
    a_list = []
    r_list = []
    start_search_from_point('in', rule_mapper, [], a_list, r_list)
    # print_2d(a_list)
    # print_2d(r_list)
    ret = 0
    for cond_list in a_list:
        # these ARE non-overlapping by virtue of how they were generated OMG i'm dumb ya
        ret += num_meeting_conds(cond_list)
    # print('a', ret)
    print(ret)

    # ret_2 = 0
    # for cond_list in r_list:
    #     # these ARE non-overlapping by virtue of how they were generated OMG i'm dumb ya
    #     ret_2 += num_meeting_conds(cond_list)
    # print('r', ret_2)
    
    # print('tot', ret + ret_2, 'vs', 4000 ** 4)

    # print_2d(a_list)
    # simplified_a_list = [simplify_cond_list(cond_list) for cond_list in a_list]
    # num_meeting_conds_list = [num_meeting_conds(cond_list) for cond_list in a_list]
    
    # zipped = [(a_list[i], simplified_a_list[i], num_meeting_conds_list[i]) for i in range(len(a_list))]
    # zipped.sort(key=lambda x: x[2], reverse=True)
    # # print_2d(zipped)
    
    # simplified_a_list = [x[1] for x in zipped] # sorted so maybe this is faster???
    # print_2d(simplified_a_list)
    
    # print_2d(num_meeting_conds_list)
    # print_2d(simplified_a_list)
    # counter = 0
    # for x in range(1, 4001):
    #     # print(f"x: processing {x} of 4000")
    #     for m in range(1, 4001):
    #         # print(f"m: processing {m} of 4000")
    #         for a in range(1, 4001):
    #             # print(f"a: processing {a} of 4000")
    #             for s in range(1, 4001):
    #                 item_dict = {
    #                     'x': x,
    #                     'm': m,
    #                     'a': a,
    #                     's': s,
    #                 }
    #                 for simplified_cond in simplified_a_list:
    #                     if match_simplified_cond(item_dict, simplified_cond):
    #                         counter += 1
    #                         break
    #                 # if any([match_simplified_cond(item_dict, simplified_cond) for simplified_cond in simplified_a_list]):
    #                 #     counter += 1
    # print(counter)

def match_simplified_cond(item_dict, simplified_cond):
    for k in ['x', 'm', 'a', 's']:
        lowest_lt, highest_gt = simplified_cond[k]
        if (lowest_lt != None and item_dict[k] >= lowest_lt):
            return False
        if (highest_gt != None and item_dict[k] <= highest_gt):
            return False
    return True

def simplify_cond_list(cond_list):
    ret = dict()
    ret['x'] = [None, None] # lowest_lt, highest_gt
    ret['m'] = [None, None]
    ret['a'] = [None, None]
    ret['s'] = [None, None]
    for cond in cond_list:
        op, var, val = cond
        if op == '<':
            if ret[var][0] == None or ret[var][0] > val:
                ret[var][0] = val
        elif op == '>':
            if ret[var][1] == None or ret[var][1] < val:
                ret[var][1] = val
        else:
            assert(False)
    return ret    

def num_meeting_conds(cond_list):
    x_conds = []
    m_conds = []
    a_conds = []
    s_conds = []
    for cond in cond_list:
        op, var, val = cond
        if var == 'x':
            x_conds.append((op, val))
        elif var == 'm':
            m_conds.append((op, val))
        elif var == 'a':
            a_conds.append((op, val))
        elif var == 's':
            s_conds.append((op, val))
        else:
            assert(False)
    # print_2d(cond_list)
    # print_2d(x_conds)
    # print_2d(m_conds)
    # print_2d(a_conds)
    # print_2d(s_conds)
    # exit(1)
    return num_meeting_single_var_cond_list(x_conds) * num_meeting_single_var_cond_list(m_conds) * num_meeting_single_var_cond_list(a_conds) * num_meeting_single_var_cond_list(s_conds)
    
def num_meeting_single_var_cond_list(s_cond_list):
    # if len(s_cond_list) == 0:
    #     return 4000
    highest_gt = None
    lowest_lt = None
    for i in s_cond_list:
        op, val = i
        if op == '<':
            if lowest_lt == None or lowest_lt > val:
                lowest_lt = val
        elif op == '>':
            if highest_gt == None or highest_gt < val:
                highest_gt = val
        else:
            assert(False)
    if highest_gt == None and lowest_lt == None:
        ret = 4000
    elif highest_gt == None:
        ret = max(lowest_lt - 1, 0)
    elif lowest_lt == None:
        ret = max(4000 - highest_gt, 0)
    else:
        ret = max(lowest_lt - highest_gt - 1, 0)
    # print(s_cond_list, ret)
    return ret

def start_search_from_point(current_rule_name, rule_mapper, current_acc_conditions, a_list, r_list):
    current_rule = rule_mapper[current_rule_name]
    cases, default_catch = current_rule
    current_acc_inverse_conditions = []
    for case in cases:
        # op, var, val = case[0]
        next_rule_if_success = case[1]
        if next_rule_if_success == 'A':
            current_acc_conditions_copy = copy.deepcopy(current_acc_conditions)
            current_acc_inverse_conditions_copy = copy.deepcopy(current_acc_inverse_conditions)
            a_list.append(current_acc_conditions_copy + current_acc_inverse_conditions_copy + [case[0]])
        elif next_rule_if_success == 'R':
            current_acc_conditions_copy = copy.deepcopy(current_acc_conditions)
            current_acc_inverse_conditions_copy = copy.deepcopy(current_acc_inverse_conditions)
            current_acc_conditions_copy.append(case[0])
            r_list.append(current_acc_conditions_copy + current_acc_inverse_conditions_copy + [case[0]])
        else:
            current_acc_conditions_copy = copy.deepcopy(current_acc_conditions)
            current_acc_inverse_conditions_copy = copy.deepcopy(current_acc_inverse_conditions)
            start_search_from_point(next_rule_if_success, rule_mapper, current_acc_conditions_copy + current_acc_inverse_conditions_copy + [case[0]], a_list, r_list)
        current_acc_inverse_conditions.append(invert_rule(case[0]))
    if default_catch == 'A':        
        current_acc_conditions_copy = copy.deepcopy(current_acc_conditions)
        current_acc_inverse_conditions_copy = copy.deepcopy(current_acc_inverse_conditions)
        a_list.append(current_acc_conditions_copy + current_acc_inverse_conditions_copy)
    elif default_catch == 'R':        
        current_acc_conditions_copy = copy.deepcopy(current_acc_conditions)
        current_acc_inverse_conditions_copy = copy.deepcopy(current_acc_inverse_conditions)
        r_list.append(current_acc_conditions_copy + current_acc_inverse_conditions_copy)
    else:
        current_acc_conditions_copy = copy.deepcopy(current_acc_conditions)
        current_acc_inverse_conditions_copy = copy.deepcopy(current_acc_inverse_conditions)
        start_search_from_point(default_catch, rule_mapper, current_acc_conditions_copy + current_acc_inverse_conditions_copy, a_list, r_list)

def invert_rule(operators):
    op, var, val = operators
    if op == '<':
        return '>', var, val-1
    elif op == '>':
        return '<', var, val+1
    assert(False)
    # return operators

if __name__ == '__main__':
    # s = time.time()
    main()
    # print(time.time() - s)
    # print(((time.time() - s) * 6269230080) / 60)
    main2()
