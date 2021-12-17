#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 2)
fin = advent.get_input()

commands = fin.readlines()

# Part 1
distance = 0
depth = 0

for cmd in commands:
    dir = cmd.split(" ")[0]
    num = int(cmd.split(" ")[1])

    if dir == "forward":
        distance += num
    elif dir == "up":
        depth -= num
    elif dir == "down":
        depth += num

advent.submit_answer(1, distance * depth)

# Part 2
distance = 0
depth = 0
aim = 0

for cmd in commands:
    dir = cmd.split(" ")[0]
    num = int(cmd.split(" ")[1])

    if dir == "forward":
        distance += num
        depth += num * aim
    elif dir == "up":
        aim -= num
    elif dir == "down":
        aim += num

advent.submit_answer(2, distance * depth)