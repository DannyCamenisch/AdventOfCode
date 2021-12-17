#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 17)

# target area: x=281..311, y=-74..-54

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

        if curX >= 281 and curX <= 311 and curY <= -54 and curY >= -74:
            return True, maxY

        if curX > 311 or curY < -74:
            return False, 0


# Part 1
maxY = 0
count = 0
for x in range(0, 312):
    for y in range(-75, 1001):
        res, tmp = launch_probe(x, y)
        
        if res:
            count += 1
            maxY = max(maxY, tmp)

advent.submit_answer(1, maxY)

# Part 2
advent.submit_answer(2, count)