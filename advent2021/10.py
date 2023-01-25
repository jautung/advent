import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '10_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    
    score = 0
    for dat in data:
        curr = ''
        for i in dat:
            if i == '(':
                curr += i
            elif i == '[':
                curr += i
            elif i == '{':
                curr += i
            elif i == '<':
                curr += i
            elif i == ')':
                if curr[-1] == '(':
                    curr = curr[:-1]
                else:
                    score += 3
                    break
            elif i == ']':
                if curr[-1] == '[':
                    curr = curr[:-1]
                else:
                    score += 57
                    break
            elif i == '}':
                if curr[-1] == '{':
                    curr = curr[:-1]
                else:
                    score += 1197
                    break
            elif i == '>':
                if curr[-1] == '<':
                    curr = curr[:-1]
                else:
                    score += 25137
                    break
    print(score)

# Time: 10:39

def main2():
    data = readlines(FILENAME)
    
    scores = []
    for dat in data:
        curr = ''
        stop = False
        for i in dat:
            if i == '(':
                curr += i
            elif i == '[':
                curr += i
            elif i == '{':
                curr += i
            elif i == '<':
                curr += i
            elif i == ')':
                if curr[-1] == '(':
                    curr = curr[:-1]
                else:
                    stop = True
                    break
            elif i == ']':
                if curr[-1] == '[':
                    curr = curr[:-1]
                else:
                    stop = True
                    break
            elif i == '}':
                if curr[-1] == '{':
                    curr = curr[:-1]
                else:
                    stop = True
                    break
            elif i == '>':
                if curr[-1] == '<':
                    curr = curr[:-1]
                else:
                    stop = True
                    break
        if stop:
            continue
        scores.append(scoring(list(reversed(curr))))
    scores = sorted(scores)
    print(scores[len(scores)//2])

def scoring(lst):
    score = 0
    for i in lst:
        if i == '(':
            score *= 5
            score += 1
        elif i == '[':
            score *= 5
            score += 2
        elif i == '{':
            score *= 5
            score += 3
        elif i == '<':
            score *= 5
            score += 4
    return score

# Time: 15:52

if __name__ == '__main__':
    main()
    main2()
