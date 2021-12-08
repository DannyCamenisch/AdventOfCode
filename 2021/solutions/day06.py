#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 6)
fin = advent.get_input()

numbers = list(map(int, fin.readline().strip().split(',')))
fishes = {}

for num in numbers:
    if num not in fishes:
        fishes[num] = 1
    else:
        fishes[num] += 1

# Part 1
for _ in range(80):
    tmpFish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0} 
    for i in range(9):
        if i in fishes:
            if i == 0:
                tmpFish[8] += fishes[i]
                tmpFish[6] += fishes[i]
            else:
                tmpFish[i-1] += fishes[i]
    fishes = tmpFish
            
res = sum(fishes.values())

advent.submit_answer(1, res)

# Part 2
for _ in range(256 - 80):
    tmpFish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0} 
    for i in range(9):
        if i in fishes:
            if i == 0:
                tmpFish[8] += fishes[i]
                tmpFish[6] += fishes[i]
            else:
                tmpFish[i-1] += fishes[i]
    fishes = tmpFish
            
res = sum(fishes.values())

advent.submit_answer(2, res)