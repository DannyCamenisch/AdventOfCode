#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 2)
fin = advent.get_input()

lines = [line for line in fin.read().strip().split('\n')]

# Part 1
ans = 0

for line in lines:
    parts = line.split(' ')
    
    if parts[1] == 'X':
        ans += 1
        ans += 0 if parts[0] == 'B' else 3 if parts[0] == 'A' else 6
    if parts[1] == 'Y':
        ans += 2
        ans += 0 if parts[0] == 'C' else 3 if parts[0] == 'B' else 6
    if parts[1] == 'Z':
        ans += 3
        ans += 0 if parts[0] == 'A' else 3 if parts[0] == 'C' else 6


advent.submit_answer(1, ans)

# Part 2
ans = 0

for line in lines:
    parts = line.split(' ')
    
    if parts[1] == 'X':
        ans += 0
        ans += 3 if parts[0] == 'A' else 1 if parts[0] == 'B' else 2
    if parts[1] == 'Y':
        ans += 3
        ans += 1 if parts[0] == 'A' else 2 if parts[0] == 'B' else 3
    if parts[1] == 'Z':
        ans += 6
        ans += 2 if parts[0] == 'A' else 3 if parts[0] == 'B' else 1

advent.submit_answer(2, ans)