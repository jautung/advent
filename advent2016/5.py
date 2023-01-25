import sys 
sys.path.append('..')

import copy
import hashlib
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def main():
    KEY = 'ugkcyxxp'
    # KEY = 'abc'

    i = 0
    num_times = 0
    res = ''
    while True:
        test = KEY + str(i)
        result = hashlib.md5(test.encode())
        if result.hexdigest().startswith('00000'):
            # print(i, result.hexdigest(), result.hexdigest()[5])
            res += result.hexdigest()[5]
            num_times += 1
            if num_times == 8:
                print(res)
                return
            # return
        i += 1

def main2():
    KEY = 'ugkcyxxp'
    # KEY = 'abc'

    i = 0
    # num_times = 0
    res = dict()
    found = set()
    while True:
        test = KEY + str(i)
        result = hashlib.md5(test.encode())
        if result.hexdigest().startswith('00000'):
            # print(i, result.hexdigest(), result.hexdigest()[5])
            pos = result.hexdigest()[5]
            if pos not in found and ord(pos) >= ord('0') and ord(pos) <= ord('7'):
                res[int(pos)] = result.hexdigest()[6]
                # print(int(pos), result.hexdigest()[6])
                found.add(pos)
                if len(found) == 8:
                    for i in range(8):
                        print(res[i],end='')
                    print()
                    return
            # c = result.hexdigest()[6]
            # num_times += 1
            # if num_times == 8:
            #     print(res)
            #     return
            # return
        i += 1

if __name__ == '__main__':
    main()
    main2()
