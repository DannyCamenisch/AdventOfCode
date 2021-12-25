#!/usr/bin/env python3

from utils import advent
import copy

advent.setup(2021, 25)
fin = advent.get_input()

grid = [[s for s in line.strip()] for line in fin.readlines()]

count = 0
while True:
    count += 1
    has_moved = False
    grid_copy = copy.deepcopy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '>':
                if grid[x][(y+1) % len(grid[x])] == '.':
                    grid_copy[x][y] = '.'
                    grid_copy[x][(y+1) % len(grid[x])] = '>'
                    has_moved = True

    grid = grid_copy
    grid_copy = copy.deepcopy(grid)

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'v':
                if grid[(x+1) % len(grid)][y] == '.':
                    grid_copy[x][y] = '.'
                    grid_copy[(x+1) % len(grid)][y] = 'v'
                    has_moved = True
    if not has_moved:
        break
    grid = grid_copy

# Part 1
advent.submit_answer(1, count)