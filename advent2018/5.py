import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)[0]
    while True:
        new_data = iterate_on(data)
        # print(new_data)
        if new_data == data:
            # print(new_data)
            print(len(new_data))
            return
        data = new_data
    # print(data)

def iterate_on(data):
    for i in range(len(data)-1):
        f = data[i]
        s = data[i+1]
        if abs(ord(f)-ord(s)) == abs(ord('a')-ord('A')):
            return data[:i] + data[i+2:]
    return data

def main2():
    data = readlines(FILENAME)[0]

    def get_final_size(data):
        while True:
            new_data = iterate_on(data)
            # print(new_data)
            if new_data == data:
                # print(new_data)
                # print(len(new_data))
                return len(new_data)
            data = new_data
        # print(data)

    min_seen = None
    for i in 'abcdefghijklmnopqrstuvwxyz':
        # print(i)
        test_data = ''.join(list(filter(lambda x: x != i and ord(x)-ord(i) != ord('A')-ord('a'), list(data))))
        cand = get_final_size(test_data)
        # print(i, test_data, get_final_size(test_data))
        if not min_seen or cand < min_seen:
            min_seen = cand
    print(min_seen)

if __name__ == '__main__':
    main()
    main2()
