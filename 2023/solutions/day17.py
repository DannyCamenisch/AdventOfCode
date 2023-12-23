#!/usr/bin/env python3

import heapq

import numpy as np

from utils import advent

advent.setup(2023, 17)
fin = advent.get_input()

grid = [[int(c) for c in line] for line in fin.read().splitlines()]


def dijkstra(grid, flowmin=1, flowmax=3):
    (
        h,
        w,
    ) = len(
        grid
    ), len(grid[0])
    shortest_paths = np.full((h, w), np.inf)
    pq = [(0, (0, 0), (0, 0))]
    seen = set()

    while pq:
        heat, (x, y), (dx, dy) = heapq.heappop(pq)
        if (x, y, dx, dy) in seen:
            continue

        seen.add((x, y, dx, dy))
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (dx == i and dy == j) or (dx == -i and dy == -j):
                continue

            new_heat = heat
            if 0 <= x + i * (flowmin - 1) < h and 0 <= y + j * (flowmin - 1) < w:
                for d in range(1, flowmin):
                    nx, ny = x + (i * d), y + (j * d)
                    new_heat += grid[nx][ny]

            for flow in range(flowmin, flowmax + 1):
                nx, ny = x + i * flow, y + j * flow
                if 0 <= nx < h and 0 <= ny < w:
                    new_heat += grid[nx][ny]
                    if new_heat < shortest_paths[nx][ny]:
                        shortest_paths[nx][ny] = new_heat
                    heapq.heappush(pq, (new_heat, (nx, ny), (i, j)))
                else:
                    break

    return int(shortest_paths[-1][-1])


# Part 1
result_1 = dijkstra(grid)
advent.submit_answer(1, result_1)

# Part 2
result_2 = dijkstra(grid, 4, 10)
advent.submit_answer(2, result_2)
