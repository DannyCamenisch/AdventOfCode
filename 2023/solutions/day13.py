#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 13)
fin = advent.get_input()

patterns = [[[c for c in l] for l in p.split("\n")] for p in fin.read().split("\n\n")]


def check_reflection(p, l):
    for i in range(0, min(l, len(p) - l)):
        if p[l - 1 - i] != p[l + i]:
            return False

    return True


def find_reflection(p, exclude_horizontal=-1, exclude_vertical=-1):
    horizontal = -1
    vertical = -1

    for i in range(1, len(p)):
        if check_reflection(p, i) and i != exclude_horizontal:
            horizontal = i

    p_t = list(map(list, zip(*p)))
    for i in range(1, len(p_t)):
        if check_reflection(p_t, i) and i != exclude_vertical:
            vertical = i

    return horizontal, vertical


def flip(p, x, y):
    if p[x][y] == "#":
        p[x][y] = "."
    else:
        p[x][y] = "#"


result_1 = 0
result_2 = 0
for p in patterns:
    horizontal, vertical = find_reflection(p)

    result_1 += vertical if vertical != -1 else 0
    result_1 += 100 * horizontal if horizontal != -1 else 0

    new_horizontal = -1
    new_vertical = -1
    for i in range(len(p)):
        for j in range(len(p[i])):
            flip(p, i, j)

            tmp_horizontal, tmp_vertical = find_reflection(p, horizontal, vertical)

            if tmp_horizontal != -1 and tmp_horizontal != horizontal:
                new_horizontal = tmp_horizontal

            if tmp_vertical != -1 and tmp_vertical != vertical:
                new_vertical = tmp_vertical

            flip(p, i, j)

    result_2 += new_vertical if new_vertical != -1 else 0
    result_2 += 100 * new_horizontal if new_horizontal != -1 else 0


# Part 1
advent.submit_answer(1, result_1)

# Part 2
advent.submit_answer(2, result_2)
