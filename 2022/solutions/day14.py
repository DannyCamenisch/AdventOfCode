#!/usr/bin/env python3

from utils import advent
from copy import deepcopy

advent.setup(2022, 14)
fin = advent.get_input()

lines = [line for line in fin.read().strip().split('\n')]

blocks = set()

max_y = 0

for line in lines:
    prev_x, prev_y = None, None
    for pair in line.split('->'):
        x, y = pair.strip().split(',')
        x, y = int(x), int(y)

        max_y = max(max_y, y)
        
        if prev_x is None:
            prev_x = x
            prev_y = y
        else:
            if prev_x == x:
                for i in range(min(prev_y, y), max(prev_y, y) + 1):
                    blocks.add((x, i))
            elif prev_y == y:
                for i in range(min(prev_x, x), max(prev_x, x) + 1):
                    blocks.add((i, y))
            
            prev_x = x
            prev_y = y

blocks_s = deepcopy(blocks)

# Part 1 
i = 0
falling = False

while(not falling):
    i += 1
    x, y = 500, 0

    while((x, y+1) not in blocks or (x-1, y+1) not in blocks or (x+1, y+1) not in blocks):
        if (x, y+1) not in blocks:
            y += 1
        elif (x-1, y+1) not in blocks:
            x -= 1
            y += 1
        elif (x+1, y+1) not in blocks:
            x += 1
            y += 1

        if y > 1000:
            falling = True
            break
        
    blocks.add((x, y))

advent.submit_answer(1, i-1)

# Part 2

blocks = blocks_s

for x in range(-500, 1501):
    blocks.add((x, max_y+2))

i = 0

while(True):
    i += 1
    x, y = 500, 0

    while((x, y+1) not in blocks or (x-1, y+1) not in blocks or (x+1, y+1) not in blocks):
        if (x, y+1) not in blocks:
            y += 1
        elif (x-1, y+1) not in blocks:
            x -= 1
            y += 1
        elif (x+1, y+1) not in blocks:
            x += 1
            y += 1

    if (x, y) == (500, 0):
        break
        
    blocks.add((x, y))

advent.submit_answer(2, i)