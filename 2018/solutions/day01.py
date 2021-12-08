#!/usr/bin/env python3

from utils import advent

advent.setup(2018, 1)
fin = advent.get_input()

numbers = tuple(map(int, fin.readlines()))

# Part 1

ans = 0

for x in numbers:
	ans += x

advent.submit_answer(1, ans)

# Part 2

ans = 0
freq = set()
found = True

while found:
	for x in numbers:
		freq.add(ans)
		ans += x
		if ans in freq:
			found = False
			break

advent.submit_answer(2, ans)


