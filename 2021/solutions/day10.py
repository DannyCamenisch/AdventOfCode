#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 10)
fin = advent.get_input()

# Part 1
lines = [l.strip() for l in fin]
points = 0
incomplete = []

for line in lines:
    stack = []
    corrupt = False
    for char in line:
        if char in {'(', '[', '{', '<'}:
            stack.append(char)
        else:
            top = stack.pop()
            if top != '(' and char == ')':
                points += 3
                corrupt = True
            if top != '[' and char == ']':
                points += 57
                corrupt = True
            if top != '{' and char == '}':
                points += 1197
                corrupt = True
            if top != '<' and char == '>':
                points += 25137
                corrupt = True
            if corrupt:
                break
    if not corrupt:
        incomplete.append(line)
            
advent.submit_answer(1, points)

# Part 2
scores = []

for line in incomplete:
    stack = []
    score = 0
    for char in line:
        if char in {'(', '[', '{', '<'}:
            stack.append(char)
        else:
            top = stack.pop()

    while(len(stack) > 0):
        top = stack.pop()
        score *= 5

        if top == '(':
            score += 1
        elif top == '[':
            score += 2
        elif top == '{':
            score += 3
        elif top == '<':
            score += 4
    scores.append(score)

scores = sorted(scores)
res = scores[int((len(scores) - 1) / 2)]

advent.submit_answer(2, res) 