#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 4)
fin = advent.get_input()

lines = [line for line in fin.read().strip().split('\n')]

# Part 1
ans = 0

for line in lines:
    range1, range2 = line.split(',')
    lower1, upper1 = range1.split('-')
    lower2, upper2 = range2.split('-')

    lower1 = int(lower1)
    upper1 = int(upper1)
    lower2 = int(lower2)
    upper2 = int(upper2)

    if lower1 <= lower2 and upper1 >= upper2:
        ans += 1
    if lower1 >= lower2 and upper1 <= upper2:
        ans += 1
    if lower1 == lower2 and upper1 == upper2:
        ans -= 1

advent.submit_answer(1, ans)

# Part 2
ans = 0

for line in lines:
    range1, range2 = line.split(',')
    lower1, upper1 = range1.split('-')
    lower2, upper2 = range2.split('-')

    lower1 = int(lower1)
    upper1 = int(upper1)
    lower2 = int(lower2)
    upper2 = int(upper2)

    # Check if the ranges overlap
    if lower1 <= lower2 and upper1 >= lower2:
        ans += 1
        continue
    if lower1 <= upper2 and upper1 >= upper2:
        ans += 1
        continue
    if lower2 <= lower1 and upper2 >= lower1:
        ans += 1
        continue
    if lower2 <= upper1 and upper2 >= upper1:
        ans += 1
        continue
    
advent.submit_answer(2, ans)