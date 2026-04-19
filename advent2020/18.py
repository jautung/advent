import sys

sys.path.append("..")

import copy
import re
from collections import defaultdict
from helper import *

FILENAME = "18_dat.txt"
mapper = {}


def main():
    data = readlines(FILENAME)
    totalOfAll = 0
    for i in data:
        # print(i, solve(i))
        totalOfAll += solve(i)
    print(totalOfAll)


def solve(line):
    pendingNum = ""
    layerIdx = 0
    runningTotal = []
    pendingOperation = []
    for idx, char in enumerate(line):
        if char == " ":
            continue
        elif char.isdigit():
            pendingNum += char
            if idx + 1 >= len(line) or not line[idx + 1].isdigit():
                realNum = int(pendingNum)
                assert (
                    len(runningTotal) == layerIdx or len(runningTotal) == layerIdx + 1
                )
                if len(runningTotal) == layerIdx:
                    runningTotal.append(realNum)
                else:
                    assert len(pendingOperation) == layerIdx + 1
                    if pendingOperation[layerIdx] == "+":
                        runningTotal[layerIdx] += realNum
                    elif pendingOperation[layerIdx] == "-":
                        runningTotal[layerIdx] -= realNum
                    elif pendingOperation[layerIdx] == "*":
                        runningTotal[layerIdx] *= realNum
                    else:
                        assert False
                pendingNum = ""
        elif char in set(["+", "-", "*"]):
            assert (
                len(pendingOperation) == layerIdx
                or len(pendingOperation) == layerIdx + 1
            )
            if len(pendingOperation) == layerIdx:
                pendingOperation.append(char)
            else:
                pendingOperation[layerIdx] = char
        elif char == "(":
            layerIdx += 1
            runningTotal.append(0)
            pendingOperation.append("+")
        elif char == ")":
            pendingOperation.pop()
            finishedFromInside = runningTotal.pop()
            if pendingOperation[-1] == "+":
                runningTotal[-1] += finishedFromInside
            elif pendingOperation[-1] == "-":
                runningTotal[-1] -= finishedFromInside
            elif pendingOperation[-1] == "*":
                runningTotal[-1] *= finishedFromInside
            else:
                assert False
            layerIdx -= 1
            # print(runningTotal, pendingOperation)
        else:
            assert False
    assert len(runningTotal) == 1
    return runningTotal[0]


def main2():
    data = readlines(FILENAME)
    totalOfAll = 0
    for i in data:
        # final = solve2(i)
        # print("final", final)
        # print(i, solve2(i))
        totalOfAll += solve2(i)
    print(totalOfAll)


def solve2(line):
    while "(" in line and ")" in line:
        matches = re.findall(r"\([^\(\)]+\)", line)
        for match in matches:
            inner = match[1:-1]
            # print(inner, solve2Simple(inner))
            line = line.replace(match, str(solve2Simple(inner)), 1)
            # innerVal = solve2(inner)
            # line = line.replace(match, str(innerVal), 1)
        # print("replaced line", line)
    return solve2Simple(line)


def solve2Simple(line):
    assert "(" not in line and ")" not in line
    additionParts = line.split("*")
    additionParts = [sum([int(x) for x in part.split("+")]) for part in additionParts]
    return product(additionParts)


if __name__ == "__main__":
    main()
    main2()
