#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 12)
fin = advent.get_input()

grid = [[-1 if c == 'S' else (-2 if c == 'E' else ord(c) - 97) for c in line] for line in fin.read().strip().split('\n')]

start = (0, 0)
end = (0, 0)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == -1:
            start = (i, j)
        if grid[i][j] == -2:
            end = (i, j)

grid[start[0]][start[1]] = 0
grid[end[0]][end[1]] = 26

# Part 1

def explore(grid, start, end):
    queue = [(start, 0)]
    visited = set()

    while queue:
        pos, dist = queue.pop(0)

        if pos in visited:
            continue

        visited.add(pos)

        if pos == end:
            return dist

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= pos[0] + i < len(grid) and 0 <= pos[1] + j < len(grid[0]):
                if grid[pos[0] + i][pos[1] + j] <= grid[pos[0]][pos[1]] + 1:
                    queue.append(((pos[0] + i, pos[1] + j), dist + 1))

    return -1

advent.submit_answer(1, explore(grid, start, end))

# Part 2

possibleStarts = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            possibleStarts.append((i, j))

minSteps = explore(grid, start, end)

for start in possibleStarts:
    steps = explore(grid, start, end)
    if steps != -1:
        minSteps = min(minSteps, steps)

advent.submit_answer(2, minSteps)