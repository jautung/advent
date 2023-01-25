import sys 
sys.path.append('..')

import copy
import hashlib
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def main():
    KEY = 'iwrupvqb'

    i = 0
    while True:
        test = KEY + str(i)
        result = hashlib.md5(test.encode())
        if result.hexdigest().startswith('00000'):
            print(i, result.hexdigest())
            return
        i += 1

def main2():
    KEY = 'iwrupvqb'

    i = 0
    while True:
        test = KEY + str(i)
        result = hashlib.md5(test.encode())
        if result.hexdigest().startswith('000000'):
            print(i, result.hexdigest())
            return
        i += 1

if __name__ == '__main__':
    main()
    main2()
