#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 15)
fin = advent.get_input()

lines = [line for line in fin.read().strip().split('\n')]

# Part 1

blocks = set()
beacons = set()

sensors = []

for line in lines:
    s_x = int(line.split(':')[0].split(',')[0].split('=')[1].strip())
    s_y = int(line.split(':')[0].split(',')[1].split('=')[1].strip())

    b_x = int(line.split(':')[1].split(',')[0].split('=')[1].strip())
    b_y = int(line.split(':')[1].split(',')[1].split('=')[1].strip())

    d = abs(s_x - b_x) + abs(s_y - b_y) - abs(s_y - 2000000)

    sensors.append((s_x, s_y, abs(s_x - b_x) + abs(s_y - b_y)))

    if b_y == 2000000:
        beacons.add(b_x)

    if d < 0:
        continue
    else:
        blocks.add(s_x)
        for i in range(1, d+1):
            blocks.add(s_x + i)
            blocks.add(s_x - i)

advent.submit_answer(1, len(blocks) - len(beacons))

# Part 2

res = (0, 0)

for s_x, s_y, d in sensors:
    for dx in range(d+2):
        dy = d + 1 - dx

        for sign_x, sign_y in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            x = s_x + sign_x * dx
            y = s_y + sign_y * dy

            if x < 0 or y < 0 or x > 4000000 or y > 4000000:
                continue

            found = True

            for s2_x, s2_y, d2 in sensors:
                if abs(x - s2_x) + abs(y - s2_y) <= d2:
                    found = False
                    break
            
            if found:
                res = (x, y)

advent.submit_answer(2, res[0]*4000000 + res[1])