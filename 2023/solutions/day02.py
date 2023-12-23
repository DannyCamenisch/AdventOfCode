#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 2)
fin = advent.get_input()

lines = [line for line in fin.read().strip().split("\n")]

# Part 1
result_1 = 0
result_2 = 0
for idx, line in enumerate(lines):
    max_red = 0
    for red in line.split("red")[:-1]:
        max_red = max(max_red, int(red.strip().split(" ")[-1]))

    max_green = 0
    for green in line.split("green")[:-1]:
        max_green = max(max_green, int(green.strip().split(" ")[-1]))

    max_blue = 0
    for blue in line.split("blue")[:-1]:
        max_blue = max(max_blue, int(blue.strip().split(" ")[-1]))

    if max_red < 13 and max_green < 14 and max_blue < 15:
        result_1 += idx + 1

    result_2 += max_red * max_green * max_blue

advent.submit_answer(1, result_1)
advent.submit_answer(2, result_2)
