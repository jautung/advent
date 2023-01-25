import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def main():
    data = readlines_split_by_newlines(FILENAME)
    print(sum([is_valid(passport) for passport in data]))

def is_valid(passport):
    fields = flatten([p.split() for p in passport])
    fields = [a[:3] for a in fields]
    # print(set(fields))

    NECC = set(['iyr', 'byr', 'pid', 'ecl', 'hgt', 'eyr', 'hcl'])

    return len(NECC - set(fields)) == 0
    # exit()
    # return True

def main2():
    data = readlines_split_by_newlines(FILENAME)
    print(sum([is_valid_2(passport) for passport in data]))

def is_valid_2(passport):
    fields = flatten([p.split() for p in passport])
    real_values = dict()
    for a in fields:
        real_values[a[:3]] = a[4:]

    NECC = set(['iyr', 'byr', 'pid', 'ecl', 'hgt', 'eyr', 'hcl'])

    if len(NECC - set(real_values.keys())) > 0:
        return False
    
    try:
        t = int(real_values['byr'])
        if t < 1920 or t > 2002:
            return False
    except:
        return False

    try:
        t = int(real_values['iyr'])
        if t < 2010 or t > 2020:
            return False
    except:
        return False

    try:
        t = int(real_values['eyr'])
        if t < 2020 or t > 2030:
            return False
    except:
        return False

    if real_values['hgt'][-2:] == 'cm':
        try:
            t = int(real_values['hgt'][:-2])
            if t < 150 or t > 193:
                return False
        except:
            return False
    elif real_values['hgt'][-2:] == 'in':
        try:
            t = int(real_values['hgt'][:-2])
            if t < 59 or t > 76:
                return False
        except:
            return False
    else:
        return False

    if len(real_values['hcl']) != 7:
        return False
    if real_values['hcl'][0] != '#':
        return False
    for i in range(1,7):
        c = real_values['hcl'][i]
        if not is_hexdec(c):
            return False

    if real_values['ecl'] not in set(['amb','blu','brn','gry','grn','hzl','oth']):
        return False

    if len(real_values['pid']) != 9:
        return False
    try:
        int(real_values['pid'])
    except:
        return False

    return True

def is_hexdec(c):
    return (ord('0') <= ord(c) and ord(c) <= ord('9')) or (ord('a') <= ord(c) and ord(c) <= ord('f'))

if __name__ == '__main__':
    main()
    main2()
