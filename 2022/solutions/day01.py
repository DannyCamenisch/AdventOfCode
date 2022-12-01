#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 1)
fin = advent.get_input()

blocks = [[int(line) for line in block.split('\n')] for block in fin.read()[:-1].split('\n\n')]
blocks = [sum(block) for block in blocks]

sorted_blocks = sorted(blocks, reverse=True)

# Part 1 
advent.submit_answer(1, sorted_blocks[0])

# Part 2
advent.submit_answer(2, sum(sorted_blocks[0:3]))