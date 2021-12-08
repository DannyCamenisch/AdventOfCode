#!/usr/bin/env python3

from re import A
from utils import advent

advent.setup(2021, 5)
fin = advent.get_input()

lines = fin.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

board = [[0 for _ in range(1001)] for _ in range(1001)]

# Part 1
for line in lines:
    a = int(line.split(",")[0])
    b = int(line.split(",")[1].split(" ")[0])
    c = int(line.split(",")[1].split(" ")[2])
    d = int(line.split(",")[2])

    if a != c and b != d:
        continue

    minX = min(a, c)
    maxX = max(a, c)
    minY = min(b, d)
    maxY = max(b, d)
    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            board[x][y] += 1

res = len([k for k in range(1001) for j in range(1001) if board[k][j]>1])

advent.submit_answer(1, res)

# Part 2
for line in lines:
    a = int(line.split(",")[0])
    b = int(line.split(",")[1].split(" ")[0])
    c = int(line.split(",")[1].split(" ")[2])
    d = int(line.split(",")[2])

    if abs(a-c) != abs(b-d):
        continue

    dx = abs(a-c)
    x = 1 if a-c < 0 else -1
    y = 1 if b-d < 0 else -1
    for i in range(dx+1):
        board[a+x*i][b+y*i] += 1

res = len([k for k in range(1001) for j in range(1001) if board[k][j]>1])

advent.submit_answer(2, res)