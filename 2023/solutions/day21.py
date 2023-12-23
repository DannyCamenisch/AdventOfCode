#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 21)
fin = advent.get_input()


def count(grid, start, n=64):
    acc = 0
    frontier = {start}
    visited = set()

    for d in range(n):
        if not (d ^ n) & 1:
            acc += len(frontier)
        visited |= frontier
        frontier = {
            (y1, x1)
            for y0, x0 in frontier
            for y1, x1 in [(y0 - 1, x0), (y0, x0 - 1), (y0, x0 + 1), (y0 + 1, x0)]
            if 0 <= y1 < len(grid)
            and 0 <= x1 < len(grid[y1])
            and grid[y1][x1] != "#"
            and (y1, x1) not in visited
        }

    return acc + len(frontier)


grid = [line for line in fin.read().splitlines()]

(start,) = (
    (y, x) for y, line in enumerate(grid) for x, c in enumerate(line) if c == "S"
)


def exponential_count():
    n = 26501365
    m = len(grid)
    q, r = n // m, n % m
    ((y0, x0),) = (
        (y, x) for y, line in enumerate(grid) for x, c in enumerate(line) if c == "S"
    )
    a, b, c, d = (
        count(
            [line * (2 * i + 1) for line in grid] * (2 * i + 1),
            (y0 + i * m, x0 + i * m),
            r + i * m,
        )
        for i in range(4)
    )
    assert d == a - 3 * b + 3 * c
    return a + (b - a) * q + (c - 2 * b + a) * (q * (q - 1) // 2)


# Part 1
result_1 = count(grid, start)
advent.submit_answer(1, result_1)

# Part 2
result_2 = exponential_count()
advent.submit_answer(2, result_2)
