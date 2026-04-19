import sys

sys.path.append("..")

import copy
from collections import defaultdict
from helper import *

FILENAME = "17_dat.txt"
mapper = {}


def main():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]

    # print_2d(data)
    originalPoints = set()
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "#":
                originalPoints.add((r, c))
    # print(originalPoints)

    ITERATIONS = 6
    currentPoints = [(x, y, 0) for x, y in originalPoints]
    for iter in range(ITERATIONS):
        # print(iter, numActive(currentPoints))
        currentPoints = runIteration(currentPoints)
    print(numActive(currentPoints))


def numActive(points):
    return len(points)


def runIteration(points):
    candidatePoints = getCandidates(points)
    finalActivePoints = set()
    for cPoint in candidatePoints:
        neighbors = getNeighbors(cPoint)
        numNeighborsOn = 0
        for n in neighbors:
            if n in points:
                numNeighborsOn += 1
        if cPoint in points and (numNeighborsOn == 2 or numNeighborsOn == 3):
            finalActivePoints.add(cPoint)
        elif cPoint not in points and numNeighborsOn == 3:
            finalActivePoints.add(cPoint)
    return finalActivePoints


def getCandidates(points):
    allCandidates = set()
    for p in points:
        allCandidates.add(p)
        allCandidates = allCandidates.union(getNeighbors(p))
    return allCandidates


def getNeighbors(point):
    x, y, z = point
    allNs = set()
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            for k in range(-1, 2, 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                allNs.add((x + i, y + j, z + k))
    return allNs


def main2():
    data = readlines(FILENAME)
    data = [[d for d in dat] for dat in data]

    # print_2d(data)
    originalPoints = set()
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "#":
                originalPoints.add((r, c))
    # print(originalPoints)

    ITERATIONS = 6
    currentPoints = [(x, y, 0, 0) for x, y in originalPoints]
    for iter in range(ITERATIONS):
        # print(iter, numActive(currentPoints))
        currentPoints = runIteration2(currentPoints)
    print(numActive(currentPoints))


def runIteration2(points):
    candidatePoints = getCandidates2(points)
    finalActivePoints = set()
    for cPoint in candidatePoints:
        neighbors = getNeighbors2(cPoint)
        numNeighborsOn = 0
        for n in neighbors:
            if n in points:
                numNeighborsOn += 1
        if cPoint in points and (numNeighborsOn == 2 or numNeighborsOn == 3):
            finalActivePoints.add(cPoint)
        elif cPoint not in points and numNeighborsOn == 3:
            finalActivePoints.add(cPoint)
    return finalActivePoints


def getCandidates2(points):
    allCandidates = set()
    for p in points:
        allCandidates.add(p)
        allCandidates = allCandidates.union(getNeighbors2(p))
    return allCandidates


def getNeighbors2(point):
    x, y, z, w = point
    allNs = set()
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            for k in range(-1, 2, 1):
                for l in range(-1, 2, 1):
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue
                    allNs.add((x + i, y + j, z + k, w + l))
    return allNs


if __name__ == "__main__":
    main()
    main2()
