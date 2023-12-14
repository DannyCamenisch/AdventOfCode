#!/usr/bin/env python3

from utils import advent
from itertools import count

advent.setup(2023, 14)
fin = advent.get_input()

grid = fin.readlines()

board = {i + 1j * j: c for i, line in enumerate(grid) for j, c in enumerate(line)}
blocked = {k for k, v in board.items() if v == '#'}
stones = {k for k, v in board.items() if v == 'O'}

def tilt(s, d=1):
    while True:
        free = board.keys() - blocked - s
        new_s = {z - d if z - d in free else z for z in s}
        if new_s == s:
            return new_s
        s = new_s

def load(s):
    return sum(len(grid) - z.real for z in s)

def cycle(s):
    for d in (1, 1j, -1, -1j):
        s = tilt(s, d)
    return s

# Part 1
result_1 = int(load(tilt(stones)))
advent.submit_answer(1, result_1)

# Part 2

seen = []
for i in count():
    stones = cycle(stones)
    if stones in seen:
        start = seen.index(stones)
        break
    seen.append(stones)

result_2 = int(load(seen[(1000000000 - i) % (start - i) + i - 1]))
advent.submit_answer(2, result_2)