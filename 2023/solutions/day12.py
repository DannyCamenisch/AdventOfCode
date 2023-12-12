#!/usr/bin/env python3

from utils import advent
from functools import cache

advent.setup(2023, 12)
# fin = advent.get_input()

with open("2023/inputs/2023_12.txt") as fin:
    lines = [l.split() for l in fin.read().strip().split("\n")]

springs = [(group, tuple(map(int, sizes.split(",")))) for group, sizes in lines]

@cache
def num_solutions(s, sizes, num_done_in_group=0):
    if not s:
        return not sizes and not num_done_in_group
    num_sols = 0
    
    possible = [".", "#"] if s[0] == "?" else s[0]
    for c in possible:
        if c == "#":
            num_sols += num_solutions(s[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                if sizes and sizes[0] == num_done_in_group:
                    num_sols += num_solutions(s[1:], sizes[1:])
            else:
                num_sols += num_solutions(s[1:], sizes)
    return num_sols

# Part 1
result_1 = sum(num_solutions(group + ".", sizes) for group, sizes in springs)
advent.submit_answer(1, result_1)

# Part 2
result_2 = sum(num_solutions("?".join([group] * 5) + ".", sizes * 5) for group, sizes in springs)
advent.submit_answer(2, result_2)