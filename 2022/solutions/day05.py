#!/usr/bin/env python3

from utils import advent
from copy import deepcopy

advent.setup(2022, 5)
fin = advent.get_input()

lines = [line for line in fin.read().split('\n')]

stacks = []

for line in lines:
    if line == '':
        break

    stack_size = (len(line) + 1)// 4

    while len(stacks) < stack_size:
        stacks.append([])

    for i in range(len(stacks)):
        ch = line[1+4*i]
        if ch != ' ' and 'A' <= ch <= 'Z':
            stacks[i].append(ch)

cmds = [line for line in lines if line.startswith('move')]

# Part 1

stacks1 = deepcopy(stacks)

for cmd in cmds:
    tokens = cmd.split(' ')
    amt = int(tokens[1])
    src = int(tokens[3]) - 1
    dst = int(tokens[5]) - 1

    for i in range(amt):
        stacks1[dst].insert(0, stacks1[src].pop(0))

ans = ""

for stack in stacks1:
    ans += stack[0]

advent.submit_answer(1, ans)

# Part 2
for cmd in cmds:
    tokens = cmd.split(' ')
    amt = int(tokens[1])
    src = int(tokens[3]) - 1
    dst = int(tokens[5]) - 1

    for i in range(amt):
        stacks[dst].insert(i, stacks[src].pop(0))

ans = ""

for stack in stacks:
    ans += stack[0]   
    
advent.submit_answer(2, ans)