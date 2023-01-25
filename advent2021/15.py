import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '15_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    data = [[int(i) for i in list(dat)] for dat in data]

    def get_risk(risks, i, j):
        if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
            return None
        return risks[i][j]

    def iterate(risks):
        new_risks = copy.deepcopy(risks)
        for i in range(len(data)):
            for j in range(len(data[0])):
                neighbor_risks = [get_risk(risks, i, j-1), get_risk(risks, i, j+1), get_risk(risks, i-1, j), get_risk(risks, i+1, j)]
                neighbor_risks = list(filter(lambda x: x != None, neighbor_risks))
                if len(neighbor_risks) >= 1:
                    new_candidate = min(neighbor_risks) + data[i][j]
                    if new_risks[i][j] == None or new_candidate < new_risks[i][j]:
                        new_risks[i][j] = new_candidate
        return new_risks

    risks = dupe_array_with_def_value(data, None)
    risks[0][0] = 0
    while True:
        new_risks = iterate(risks)
        # for i in new_risks:
        #     print(i)
        # print()
        if new_risks == risks:
            break
        risks = new_risks

    # for i in risks:
    #     print(i)

    print(risks[-1][-1])

# Time: 20:51

def main2():
    data = readlines(FILENAME)
    data = [[int(i) for i in list(dat)] for dat in data]

    def plus(row, incr):
        return [((i+incr-1)%9)+1 for i in row]

    data = [dat + plus(dat, 1) + plus(dat, 2) + plus(dat, 3) + plus(dat, 4) for dat in data]

    # print(data)

    def pluss(array, incr):
        return [plus(row, incr) for row in array]

    data = data + pluss(data, 1) + pluss(data, 2) + pluss(data, 3) + pluss(data, 4)
    # print(data)

    def get_risk(risks, i, j):
        if i < 0 or j < 0 or i >= XXX or j >= YYY:
            return None
        return risks[i][j]

    XXX = len(data)
    YYY = len(data[0])

    risks = dupe_array_with_def_value(data, None)
    risks[0][0] = 0

    # tentative_final = None
    def iterate(stage):
        updated = False
        for i in range(XXX):
            for j in range(YYY):
                # print(i, j, YYY)
                neighbor_risks = [get_risk(risks, i, j-1), get_risk(risks, i, j+1), get_risk(risks, i-1, j), get_risk(risks, i+1, j)]
                neighbor_risks = list(filter(lambda x: x != None, neighbor_risks))
                if len(neighbor_risks) >= 1:
                    new_candidate = min(neighbor_risks) + data[i][j]
                    if risks[i][j] == None or new_candidate < risks[i][j]:
                        risks[i][j] = new_candidate
                        updated = True
        return updated

    stage = 0
    # for i in risks:
    #     print(i)
    while True:
        # print('stage', stage)
        updated = iterate(stage)
        # tentative_final = new_risks[-1][-1]
        # for i in risks:
        #     print(i)
        # print()
        # break
        if not updated:
            break
        stage += 1

    # for i in risks:
    #     print(i)

    print(risks[-1][-1])

# Time: 50:03 -- copy.deepcopy is indeed very slow omg

if __name__ == '__main__':
    main()
    main2()
