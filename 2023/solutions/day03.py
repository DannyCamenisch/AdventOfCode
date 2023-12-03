#!/usr/bin/env python3

import re
from collections import defaultdict
from math import prod

from utils import advent

advent.setup(2023, 3)
fin = advent.get_input()

lines = [line.strip() for line in fin.readlines()]

NUMBER_RE = re.compile(r"\d+")
SYMBOL_RE = re.compile(r"[^\s\d.]")


def parse(lines):
    for y0, line in enumerate(lines):
        for match in NUMBER_RE.finditer(line):
            num = int(match.group(0))
            x0, x1 = match.span()
            for y1 in range(max(0, y0 - 1), min(y0 + 2, len(lines))):
                for match in SYMBOL_RE.finditer(lines[y1], x0 - 1, x1 + 1):
                    yield match.start(), y1, num


# Part 1

result_1 = sum(num for _, _, num in parse(lines))
advent.submit_answer(1, result_1)

# Part 2

gears = defaultdict(list)
for x, y, num in parse(lines):
    gears[x, y].append(num)

result_2 = sum(prod(nums) for nums in gears.values() if len(nums) == 2)
advent.submit_answer(2, result_2)
