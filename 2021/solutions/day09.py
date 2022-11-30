#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 9)
fin = advent.get_input()

hMap = [[int(c) for c in l.strip()] for l in fin.readlines()]

# Part 1
risk = 0

for x in range(len(hMap)):
    for y in range(len(hMap[x])):
        top = hMap[x][y-1] if y > 0 else 10
        down = hMap[x][y+1] if y < len(hMap[x])-1 else 10
        left = hMap[x-1][y] if x > 0 else 10
        right = hMap[x+1][y] if x < len(hMap)-1 else 10

        if hMap[x][y] < min(top, down, left, right):
            risk += hMap[x][y] + 1

advent.submit_answer(1, risk)

# Part 2
def searchBasin(x, y, hMap, bMap):
    size = 1
    bMap[x][y] = True

    if hMap[x][y] == 9:
        return 0

    if x > 0 and not bMap[x-1][y]:
        size += searchBasin(x-1, y, hMap, bMap)
    if x < len(hMap)-1 and not bMap[x+1][y]:
        size += searchBasin(x+1, y, hMap, bMap)
    if y > 0 and not bMap[x][y-1]:
        size += searchBasin(x, y-1, hMap, bMap)
    if y < len(hMap[x])-1 and not bMap[x][y+1]:
        size += searchBasin(x, y+1, hMap, bMap)

    return size

largestB = 0
secondLargestB = 0
thirdLargestB = 0

bMap = [[False for _ in range(len(hMap[0]))] for _ in range(len(hMap))]

for x in range(len(hMap)):
    for y in range(len(hMap[x])):
        if not bMap[x][y]:
            size = searchBasin(x, y, hMap, bMap)
            if size > largestB:
                thirdLargestB = secondLargestB
                secondLargestB = largestB
                largestB = size
            elif size > secondLargestB:
                thirdLargestB = secondLargestB
                secondLargestB = size
            elif size > thirdLargestB:
                thirdLargestB = size

advent.submit_answer(2, thirdLargestB * secondLargestB * largestB) 