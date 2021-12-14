#!/usr/bin/env python3

from utils import advent
from collections import defaultdict

advent.setup(2021, 14)
fin = advent.get_input()

input = fin.readlines()
polymer = input[0].strip()

rules = defaultdict(str)

for l in input[2:]:
    l = l.strip()
    rules[l[0:2]] = l[0] + l[-1] + l[1]

def react(polymerStr, rules, steps):
    polymer = defaultdict(int)

    for i in range(len(polymerStr) - 1):
        polymer[polymerStr[i:(i+2)]] += 1

    for _ in range(steps):
        tmp = defaultdict(int)

        for p in polymer.keys():
            tmp[rules[p][0:2]] += polymer[p]
            tmp[rules[p][1:3]] += polymer[p]

        polymer = tmp

    charCount = defaultdict(int)

    for p in polymer.keys():
        charCount[p[0]] += polymer[p]
        charCount[p[1]] += polymer[p]

    return max(charCount.values()) - min(charCount.values())

# Part 1
res = react(polymer, rules, 10)
advent.submit_answer(1, res)

# Part 2
res = react(polymer, rules, 40)
advent.submit_answer(2, res)