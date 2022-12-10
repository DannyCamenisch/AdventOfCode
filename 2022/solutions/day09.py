#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 9)
fin = advent.get_input()

cmds = [(d, int(n)) for d, n in (l.split(' ') for l in fin.read().strip().split('\n'))]

# Part 1

visited = set()

head = (0, 0)
tail = (0, 0)

visited.add(tail)

for d, n in cmds:
    for _ in range(n):
        if d == 'U':
            head = (head[0], head[1] + 1)
        elif d == 'D':
            head = (head[0], head[1] - 1)
        elif d == 'R':
            head = (head[0] + 1, head[1])
        elif d == 'L':
            head = (head[0] - 1, head[1])

        diff = (head[0] - tail[0], head[1] - tail[1])

        if pow(diff[0], 2) + pow(diff[1], 2) <= 2:
            continue
        else:
            if diff[0] < 0:
                tail = (tail[0] - 1, tail[1])
            elif diff[0] > 0:
                tail = (tail[0] + 1, tail[1])

            if diff[1] < 0:
                tail = (tail[0], tail[1] - 1)
            elif diff[1] > 0:
                tail = (tail[0], tail[1] + 1)

        visited.add(tail)

advent.submit_answer(1, len(visited))

# Part 2

visited = set()

pos = [(0, 0)] * 10

visited.add(pos[9])

def move(tail, head):
    diff = (head[0] - tail[0], head[1] - tail[1])

    if pow(diff[0], 2) + pow(diff[1], 2) > 2:
        if diff[0] < 0:
            tail = (tail[0] - 1, tail[1])
        elif diff[0] > 0:
            tail = (tail[0] + 1, tail[1])

        if diff[1] < 0:
            tail = (tail[0], tail[1] - 1)
        elif diff[1] > 0:
            tail = (tail[0], tail[1] + 1)

    return tail

for d, n in cmds:
    for _ in range(n):
        if d == 'U':
            pos[0] = (pos[0][0], pos[0][1] + 1)
        elif d == 'D':
            pos[0] = (pos[0][0], pos[0][1] - 1)
        elif d == 'R':
            pos[0] = (pos[0][0] + 1, pos[0][1])
        elif d == 'L':
            pos[0] = (pos[0][0] - 1, pos[0][1])

        for i in range(1, 10):
            pos[i] = move(pos[i], pos[i-1])

        visited.add(pos[9])

advent.submit_answer(2, len(visited))
