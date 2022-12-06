#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 6)
fin = advent.get_input()

msg = [c for c in fin.read().strip()]

# Part 1

ans = 4
marker = msg[0:4]

for i in range(4, len(msg)):
    if len(set(marker)) == 4:
        break
    else:
        marker[i % 4] = msg[i]
        ans += 1

advent.submit_answer(1, ans)

# Part 2

ans = 14
marker = msg[0:14]

for i in range(14, len(msg)):
    if len(set(marker)) == 14:
        break
    else:
        marker[i % 14] = msg[i]
        ans += 1

advent.submit_answer(2, ans)
