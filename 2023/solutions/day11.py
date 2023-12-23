#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 11)
fin = advent.get_input()

lines = fin.read().strip().splitlines()
galaxies = [(i, j) for i, l in enumerate(lines) for j, x in enumerate(l) if x == "#"]


def expand_galaxies(galaxies, factor):
    new_galaxies = []

    offset_x = 0
    previous_x = -1
    for x, y in sorted(galaxies, key=lambda p: (p[0], p[1])):
        if x != previous_x and x != previous_x + 1:
            offset_x += 1

        previous_x = x
        new_galaxies.append((x + (factor - 1) * offset_x, y))

    galaxies = new_galaxies
    new_galaxies = []

    offset_y = 0
    previous_y = -1
    for x, y in sorted(galaxies, key=lambda p: (p[1], p[0])):
        if y != previous_y and y != previous_y + 1:
            offset_y += 1

        previous_y = y
        new_galaxies.append((x, y + (factor - 1) * offset_y))

    return new_galaxies


# Part 1
result_1 = 0
expanded_galaxies = expand_galaxies(galaxies, 2)
for i in range(len(expanded_galaxies)):
    for j in range(i + 1, len(expanded_galaxies)):
        x1, y1 = expanded_galaxies[i]
        x2, y2 = expanded_galaxies[j]
        result_1 += abs(x1 - x2) + abs(y1 - y2)

advent.submit_answer(1, result_1)

# Part 2
result_2 = 0
expanded_galaxies = expand_galaxies(galaxies, 1000000)
for i in range(len(expanded_galaxies)):
    for j in range(i + 1, len(expanded_galaxies)):
        x1, y1 = expanded_galaxies[i]
        x2, y2 = expanded_galaxies[j]
        result_2 += abs(x1 - x2) + abs(y1 - y2)

advent.submit_answer(2, result_2)
