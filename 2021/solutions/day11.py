#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 11)
fin = advent.get_input()

grid = [[int(c) for c in l.strip()] for l in fin.readlines()]

# Part 1
def flash(grid, boolGrid, i, j):    
    cFlashes = 1
    boolGrid[i][j] = True

    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            # Skip the current cell if index is out of bounds
            if (x == i and y == j) or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                continue
            
            # If the cell has not already flashes, increase by 1
            if not boolGrid[x][y]:
                grid[x][y] += 1

            # Recursively flash the cell
            if grid[x][y] > 9 and not boolGrid[x][y]:
                cFlashes += flash(grid, boolGrid, x, y)

    return cFlashes
    
flashes = 0
for _ in range(100):
    # increase every value by 1 and reset the boolGrid
    grid = [[c + 1 for c in l] for l in grid] 
    boolGrid = [[False for c in l] for l in grid]

    # try to flash all the cells
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 9 and not boolGrid[i][j]:
                flashes += flash(grid, boolGrid, i, j)

    # set all cells to 0 if they have been flashes
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if boolGrid[i][j]:
                grid[i][j] = 0
            
advent.submit_answer(1, flashes)

# Part 2
step = 100

while True:
    step += 1
    # increase every value by 1 and reset the boolGrid
    grid = [[c + 1 for c in l] for l in grid]
    boolGrid = [[False for c in l] for l in grid]
    counter = 0

    # try to flash all the cells
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 9 and not boolGrid[i][j]:
                counter += flash(grid, boolGrid, i, j)

    # break if all cells flashes
    if counter == 100:
        break

    # set all cells to 0 if they have been flashes
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if boolGrid[i][j]:
                grid[i][j] = 0

advent.submit_answer(2, step) 