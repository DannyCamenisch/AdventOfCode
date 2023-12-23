#!/usr/bin/env python3

import numpy as np

from utils import advent

advent.setup(2023, 18)
fin = advent.get_input()

instructions = [[x for x in line.strip().split()] for line in fin.read().splitlines()]

lut = {
    "R": (1, 0),
    "D": (0, 1),
    "L": (-1, 0),
    "U": (0, -1),
}

border = 0
corners = [(0, 0)]

border_hex = 0
corners_hex = [(0, 0)]

for i in instructions:
    x, y, z = lut[i[0]], int(i[1]), i[2]

    border += y
    corners.append((corners[-1][0] + x[0] * y, corners[-1][1] + x[1] * y))

    x = list(lut.values())[int(z[-2])]
    y = int(z[2:7], 16)

    border_hex += y
    corners_hex.append((corners_hex[-1][0] + x[0] * y, corners_hex[-1][1] + x[1] * y))


def area(corners, border):
    corners = np.array(corners)

    x = corners[:, 0]
    y = corners[:, 1]

    s1 = np.sum(x * np.roll(y, -1))
    s2 = np.sum(y * np.roll(x, -1))

    a = 0.5 * np.absolute(s1 - s2)

    return int(a) + int(border / 2) + 1


# Part 1
result_1 = area(corners, border)
advent.submit_answer(1, result_1)

# Part 2
result_2 = area(corners_hex, border_hex)
advent.submit_answer(2, result_2)
