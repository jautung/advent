import sys 
sys.path.append('..')

import copy
import re
import json
from collections import defaultdict
from helper import *

FILENAME = '12_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    r = re.findall('-?[0-9]+', data[0])
    print(sum([int(i) for i in r]))

def main2():
    data = readlines(FILENAME)
    j = json.loads(data[0])

    # count = 0
    def traverse(node):
        if isinstance(node, list):
            return sum([traverse(child) for child in node])
        elif isinstance(node, str):
            return 0
        elif isinstance(node, int):
            return node
        elif isinstance(node, dict):
            if 'red' in node.values():
                return 0
            return sum([traverse(child) for child in node.values()])
        else:
            print(node)
            assert(False)

    t = traverse(j)
    print(t)

if __name__ == '__main__':
    main()
    main2()
