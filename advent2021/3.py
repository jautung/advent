import sys 
sys.path.append('..')

import copy
from helper import *

FILENAME = '3_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    data = transpose(data)
    gamma = [most_common(dat) for dat in data]
    epsilon = [least_common(dat) for dat in data]
    print(bin_to_int(''.join(gamma)) * bin_to_int(''.join(epsilon)))

def main2():
    data = readlines(FILENAME)
    data = [list(dat) for dat in data]
    size = len(data[0])

    oxygen_data = copy.deepcopy(data)
    for i in range(size):
        bits = [dat[i] for dat in oxygen_data]
        bit = most_common(bits, default_if_tie='1')
        oxygen_data = [dat for dat in oxygen_data if dat[i] == bit]

    co2_data = copy.deepcopy(data)
    for i in range(size):
        bits = [dat[i] for dat in co2_data]
        bit = least_common(bits, default_if_tie='0')
        co2_data = [dat for dat in co2_data if dat[i] == bit]

    print(bin_to_int(''.join(oxygen_data[0])) * bin_to_int(''.join(co2_data[0])))

if __name__ == '__main__':
    main()
    main2()
