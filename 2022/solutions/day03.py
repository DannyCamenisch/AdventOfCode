#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 3)
fin = advent.get_input()

lines = [line for line in fin.read().strip().split('\n')]

# Part 1
ans = 0

for line in lines:
    length = int(len(line) / 2)

    item1 = line[0:length]
    item2 = line[length:]
    
    tmp = ""

    for c in item1:
        if c in item2 and c not in tmp:
            if c.isupper():
                ans += ord(c) - 64 + 26
            else:
                ans += ord(c) - 96
            tmp += c

advent.submit_answer(1, ans)

# Part 2
ans = 0

for i in range(0, len(lines), 3):
    l1 = lines[i]
    l2 = lines[i+1]
    l3 = lines[i+2]
    
    tmp = ""

    for c in l1:
        if c in l2 and c in l3 and c not in tmp:
            if c.isupper():
                ans += ord(c) - 64 + 26
            else:
                ans += ord(c) - 96
            tmp += c
    
advent.submit_answer(2, ans)