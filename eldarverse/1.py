import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '1_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    for index, line in enumerate(data[1:]):
        discount = len(set(line.lower())) * 5
        price = 100 - discount
        print(f"Case #{index+1}: {price}")

if __name__ == '__main__':
    main()
