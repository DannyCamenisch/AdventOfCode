#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 10)
fin = advent.get_input()

cmds = [line for line in fin.read().strip().split('\n')]

# Part 1

x = 1
cycle = 1

ans = 0

for cmd in cmds:
    if cmd.startswith('noop'):
        cycle += 1
    elif cmd.startswith('addx'):
        cycle += 1

        if cycle in {20, 60, 100, 140, 180, 220}:
            ans += x * cycle
        
        x += int(cmd.split()[1])
        cycle += 1

    if cycle in {20, 60, 100, 140, 180, 220}:
        ans += x * cycle

advent.submit_answer(1, ans)

# Part 2

crt = ['⬜️' for _ in range(240)]

def print_crt():
    for i in range(0, 240, 40):
        print(''.join(crt[i:i+40]))

x = 1
cycle = 0

for cmd in cmds:
    if cycle % 40 in {x-1, x, x+1}:
        crt[cycle] = '⬛️'

    if cmd.startswith('noop'):
        cycle += 1
    elif cmd.startswith('addx'):
        cycle += 1

        if cycle % 40 in {x-1, x, x+1}:
            crt[cycle] = '⬛'
        
        x += int(cmd.split()[1])
        cycle += 1

print_crt()

advent.submit_answer(2, "PAPJCBHP")
