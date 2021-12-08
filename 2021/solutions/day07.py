#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 7)
fin = advent.get_input()

numbers = list(map(int, fin.readline().strip().split(',')))

# Part 1
minVal = 100000000
for i in range(max(numbers) + 1):
    tmp = 0
    for num in numbers:
        tmp += abs(num - i)
    minVal = min(minVal, tmp)
    
advent.submit_answer(1, minVal)

# Part 2
minVal = 10000000000
for i in range(max(numbers) + 1):
    tmp = 0
    for num in numbers:
        n = abs((num - i))
        tmp += n*(n + 1)/2
    minVal = min(minVal, tmp)

advent.submit_answer(2, int(minVal))