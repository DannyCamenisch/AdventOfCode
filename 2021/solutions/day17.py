#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 17)

# hardcoded input
targetMinX = 281
targetMaxX = 311
targetMinY = -74
targetMaxY = -54

def launch_probe(x, y):
    curX = 0
    curY = 0
    maxY = 0

    while True:
        curX += x
        curY += y

        if x > 0:
            x -= 1
        elif x < 0:
            x += 1

        y -= 1

        maxY = max(maxY, curY)

        if curX >= targetMinX and curX <= targetMaxX and curY <= targetMaxY and curY >= targetMinY:
            return True, maxY

        if curX > targetMaxX or curY < targetMinY:
            return False, 0


# Part 1
maxY = 0
count = 0

for x in range(0, targetMaxX + 1):
    for y in range(targetMinY, 100):
        res, tmpY = launch_probe(x, y)
        
        if res:
            count += 1
            maxY = max(maxY, tmpY)

advent.submit_answer(1, maxY)

# Part 2
advent.submit_answer(2, count)