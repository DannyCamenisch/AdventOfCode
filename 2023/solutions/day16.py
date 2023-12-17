#!/usr/bin/env python3

from collections import deque
from utils import advent

advent.setup(2023, 16)
fin = advent.get_input()

grid = fin.read().splitlines()

def travel_grid(grid, start=(0, 0), direction=(0, 1)):
    h = len(grid)
    w = len(grid[0])
    
    queue       = deque([(*start, *direction)])
    seen        = set()
    energized   = set()

    while queue:
        r, c, dr, dc = queue.pop()
        
        while 0 <= r < h and 0 <= c < w and (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            energized.add((r, c))

            cell = grid[r][c]

            if cell == '/':
                dr, dc = -dc, -dr
            elif cell == '\\':
                dr, dc = dc, dr
            elif cell == '-' and dr:
                dr, dc = 0, 1
                queue.append((r, c - 1, 0, -1))
            elif cell == '|' and dc:
                dr, dc = 1, 0
                queue.append((r - 1, c, -1, 0))

            r += dr
            c += dc

    return len(energized)

# Part 1 
result_1 = travel_grid(grid)
advent.submit_answer(1, result_1)

# Part 2
result_2 = 0

for r in range(len(grid)):
	result_2 = max(result_2, travel_grid(grid, (r, 0), (0, 1)))
	result_2 = max(result_2, travel_grid(grid, (r, len(grid[0]) - 1), (0, -1)))

for c in range(len(grid[0])):
	result_2 = max(result_2, travel_grid(grid, (0, c), (1, 0)))
	result_2 = max(result_2, travel_grid(grid, (len(grid) - 1, c), (-1, 0)))
 
advent.submit_answer(2, result_2)