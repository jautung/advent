import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '2_dat.txt'
cache = {}

'''
Case #1: 2
Case #2: 18
Case #3: 2
Case #4: 0
Case #5: 54
Case #6: 6
Case #7: 3944
Case #8: 3944
Case #9: 2312
Case #10: 1256
Case #11: 384
Case #12: 48
Case #13: 1040840
Case #14: 810240
Case #15: 562480
Case #16: 266440
Case #17: 85000
Case #18: 16160
Case #19: 1280
Case #20: 0
'''

def main():
    data = readlines_split_each_line(FILENAME)
    for index, item in enumerate(data[1:]):
        n = int(item[0])
        k = int(item[1])
        result = compute(n, k)
        print(f"Case #{index+1}: {result}")

def compute(n, k):
    count = 0
    iter_end = 2 ** (n * (n-1))
    for i in range(iter_end):
        key = (n, i)
        if key in cache:
            gap = cache[key]
        else:
            grid = get_grid(n, i)
            # print(i)
            # print_2d(grid)
            scores = get_scores(grid, n)
            # print(scores)
            gap = get_gap(scores)
            cache[key] = gap
        if gap > k:
            count += 1
    return count

def get_grid(n, i):
    grid = [[None for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if row == col:
                continue
            grid[row][col] = 'Win' if i % 2 == 0 else 'Lose'
            i //= 2
    return grid

def get_scores(grid, n):
    ret = {}
    for i in range(n):
        score = 0
        for col in range(n):
            if grid[i][col] == 'Win':
                score += 1
        for row in range(n):
            if grid[row][i] == 'Lose':
                score += 1
        ret[i] = score
    return ret

def get_gap(scores):
    return max(scores.values()) - min(scores.values())

if __name__ == '__main__':
    main()
