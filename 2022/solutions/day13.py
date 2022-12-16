#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 13)
fin = advent.get_input()

pairs = [ line.split('\n') for line in fin.read().strip().split('\n\n') ]

def compare(a, b):
    if len(a) == 0 and len(b) == 0:
        return 0
    if len(a) == 0:
        return 1
    if len(b) == 0:
        return -1

    if type(a[0]) is list and type(b[0]) is list:
        return compare(a[0], b[0]) if compare(a[0], b[0]) != 0 else compare(a[1:], b[1:])

    if type(a[0]) is list:
        return compare(a[0], [b[0]]) if compare(a[0], [b[0]]) != 0 else compare(a[1:], b[1:])

    if type(b[0]) is list:
        return compare([a[0]], b[0]) if compare([a[0]], b[0]) != 0 else compare(a[1:], b[1:])

    if a[0] < b[0]:
        return 1 
    elif a[0] > b[0]:
        return -1
    else:
        return compare(a[1:], b[1:])

    

# Part 1

i = 1
ans = 0

for pair in pairs:
    p1 = eval(pair[0])
    p2 = eval(pair[1])

    if compare(p1, p2) == 1:
        ans += i
    
    i += 1

advent.submit_answer(1, ans)

# Part 2

lines = []
lines.append('[[2]]')
lines.append('[[6]]')

for pair in pairs:
    lines.append(pair[0])
    lines.append(pair[1])

lines_sorted = []
for l in lines:
    if len(lines_sorted) == 0:
        lines_sorted.append(l)
    else:
        for i in range(len(lines_sorted)):
            if compare(eval(l), eval(lines_sorted[i])) == 1:
                lines_sorted.insert(i, l)
                break

        if l not in lines_sorted:
            lines_sorted.append(l)

x = lines_sorted.index('[[2]]') + 1
y = lines_sorted.index('[[6]]') + 1

advent.submit_answer(2, x * y)