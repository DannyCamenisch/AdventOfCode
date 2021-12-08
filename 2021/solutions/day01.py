#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 1)
fin = advent.get_input()

numbers = tuple(map(int, fin.readlines()))

# Part 1 
ans = 0
for i in range(len(numbers)):
    if i == 0:
        continue

    if numbers[i-1] < numbers[i]:
        ans += 1

advent.submit_answer(1, ans)

# Part 2
ans = 0
for i in range(len(numbers)):
    if i == 0 or i == 1 or i == 2:
        continue

    sum1 = numbers[i-3] + numbers[i-2] + numbers[i-1]
    sum2 = numbers[i-2] + numbers[i-1] + numbers[i]

    if sum1 < sum2:
        ans += 1

advent.submit_answer(2, ans)