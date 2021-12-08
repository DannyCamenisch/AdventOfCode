#!/usr/bin/env python3

from utils import advent

advent.setup(2018, 2)
fin = advent.get_input()

boxIds = tuple(map(str, fin.readlines()))

# Part 1
res = {2: 0, 3: 0}

for i in boxIds:
    has_two = False
    has_three = False

    for char in range(ord('a'), ord('z') + 1):
        if i.count(chr(char)) == 2:
            has_two = True
        if i.count(chr(char)) == 3:
            has_three = True
    res[2] += int(has_two)
    res[3] += int(has_three)

advent.submit_answer(1, res[2] * res[3])

# Part 2
res = ""

for a in boxIds:
	for b in boxIds:
		if a == b:
			continue

		diffSmallerOne = 0

		for i in range(0, len(a)):
			if(a[i] != b[i]):
				diffSmallerOne += 1

		if(diffSmallerOne <= 1):
			temp = ""
			for i in range(0, len(a)):
				if a[i] == b[i]:
					temp += a[i]
			res = temp

advent.submit_answer(2, res)
