#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 1)
fin = advent.get_input()

numbers = tuple(map(int, fin.readlines()))
string  = tuple(fin.readlines())

# Part 1 
ans = 0
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i+1]:
        ans += 1

advent.submit_answer(1, ans)

# Part 2
ans = 0
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i+3]:
        ans += 1

advent.submit_answer(2, ans)