#!/usr/bin/env python3

import sympy

from utils import advent

advent.setup(2023, 24)
fin = advent.get_input()

hailstones = [[int(x) for x in line.replace("@", ",").split(",")] for line in fin]

RANGE_MIN = 200_000_000_000_000
RANGE_MAX = 400_000_000_000_000


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


# Part 1
result_1 = 0
for h1 in range(len(hailstones) - 1):
    for h2 in range(h1 + 1, len(hailstones)):
        x1, y1, _, dx1, dy1, _ = hailstones[h1]
        x2, y2, _, dx2, dy2, _ = hailstones[h2]

        div = det((dy1, dy2), (dx1, dx2))
        if div == 0:
            continue

        d1 = det((x1, y1), (x1 + dx1, y1 + dy1))
        d2 = det((x2, y2), (x2 + dx2, y2 + dy2))
        x = det((d1, d2), (dx1, dx2)) / div
        y = det((d1, d2), (dy1, dy2)) / div
        t1 = (x - x1) / dx1
        t2 = (x - x2) / dx2

        if (
            t1 >= 0
            and t2 >= 0
            and RANGE_MIN <= x <= RANGE_MAX
            and RANGE_MIN <= y <= RANGE_MAX
        ):
            result_1 += 1
advent.submit_answer(1, result_1)

# Part 2
x, y, z, dx, dy, dz, t1, t2, t3 = sympy.symbols("x y z dx dy dz t1 t2 t3")
x1, y1, z1, dx1, dy1, dz1 = hailstones[0]
x2, y2, z2, dx2, dy2, dz2 = hailstones[1]
x3, y3, z3, dx3, dy3, dz3 = hailstones[2]

eqs = [
    x1 - x + (dx1 - dx) * t1,
    y1 - y + (dy1 - dy) * t1,
    z1 - z + (dz1 - dz) * t1,
    x2 - x + (dx2 - dx) * t2,
    y2 - y + (dy2 - dy) * t2,
    z2 - z + (dz2 - dz) * t2,
    x3 - x + (dx3 - dx) * t3,
    y3 - y + (dy3 - dy) * t3,
    z3 - z + (dz3 - dz) * t3,
]

X, Y, Z, *_ = sympy.solve(eqs, [x, y, z, dx, dy, dz, t1, t2, t3])[0]

result_2 = X + Y + Z
advent.submit_answer(2, result_2)
