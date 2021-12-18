#!/usr/bin/env python3

from utils import advent

import ast
import copy
import numpy as np

advent.setup(2021, 18)
fin = advent.get_input()

snailnumbers = [ast.literal_eval(x) for x in fin.readlines()]

def reduce(num):
    while True:
        num, b, _, _ = explode(num)
        if b:
            continue

        num, b = split(num)
        if b:
            continue

        break

def explode(num, depth=0):
    if depth > 3 and isinstance(num[0], int) and isinstance(num[1], int):
        return 0, True, num[0], num[1]
    else:
        for i in range(len(num)):
            if isinstance(num[i], list):
                num[i], b, l, r = explode(num[i], depth+1)
                if b:
                    # try to set left and right 
                    if i == 0 and r != 0:
                        num[1] = right(num[1], r)
                        return num, True, l, 0
                    if i == 1 and l != 0:
                        num[0] = left(num[0], l) 
                        return num, True, 0, r
                      
                    return num, True, l, r        
        return num, False, 0, 0

def left(num, l):
    if isinstance(num, list):
        num[1] = left(num[1], l)
        return num
    else:
        return num + l

def right(num, r):
    if isinstance(num, list):
        num[0] = right(num[0], r)
        return num
    else:
        return num + r

def split(num):
    for i in range(len(num)):
        if isinstance(num[i], list):
            num[i], b = split(num[i])
            if b:
                return num, True
        elif num[i] > 9:
            num[i] = [int(np.floor(num[i]/2)), int(np.ceil(num[i]/2))]
            return num, True

    return num, False

def magnitude(num):
    sum = 0
    for i in range(len(num)):
        if isinstance(num[i], list):
            sum += (3-i) * magnitude(num[i])
        else:
            sum += (3-i) * num[i]

    return sum

# Part 1
snCopy = copy.deepcopy(snailnumbers)
for i in range(len(snCopy) - 1):
    snCopy[i+1] = [snCopy[i], snCopy[i+1]]
    reduce(snCopy[i+1])

advent.submit_answer(1, magnitude(snCopy[-1]))

# Part 2
maxMag = 0
for n1 in snailnumbers:
    for n2 in snailnumbers:
        if n1 != n2:
            num = [copy.deepcopy(n1), copy.deepcopy(n2)]
            reduce(num)

            maxMag = max(maxMag, magnitude(num))

advent.submit_answer(2, maxMag)