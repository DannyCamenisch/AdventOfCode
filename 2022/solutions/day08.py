#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 8)
fin = advent.get_input()

grid  = [[int(c) for c in line] for line in fin.read().strip().split('\n')]

# Part 1

def visible(grid, x, y):
    if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[x]) - 1:
        return True

    top = True
    bottom = True
    left = True
    right = True

    for dx in range(0, x):
        if grid[dx][y] >= grid[x][y]:
            top = False

    for dx in range(x+1, len(grid)):
        if grid[dx][y] >= grid[x][y]:
            bottom = False

    for dy in range(0, y):
        if grid[x][dy] >= grid[x][y]:
            left = False

    for dy in range(y+1, len(grid[x])):
        if grid[x][dy] >= grid[x][y]:
            right = False
    
    return top or bottom or left or right

ans = 0

for x in range(0, len(grid)):
    for y in range(0, len(grid[x])):
        if visible(grid, x, y):
            ans += 1

advent.submit_answer(1, ans)

# Part 2

def scenic_score(grid, x, y):
    top = 0
    bottom = 0
    left = 0
    right = 0

    for dx in range(x-1, -1, -1):
        top += 1
        if grid[dx][y] >= grid[x][y]:
            break

    for dx in range(x+1, len(grid)):
        bottom += 1
        if grid[dx][y] >= grid[x][y]:
            break

    for dy in range(y-1, -1, -1):
        left += 1
        if grid[x][dy] >= grid[x][y]:
            break

    for dy in range(y+1, len(grid[x])):
        right += 1
        if grid[x][dy] >= grid[x][y]:
            break

    return top * bottom * left * right

ans = 0

for x in range(0, len(grid)):
    for y in range(0, len(grid[x])):
        ans = max(scenic_score(grid, x, y), ans)

advent.submit_answer(2, ans)
