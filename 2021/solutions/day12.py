#!/usr/bin/env python3

from utils import advent
from collections import defaultdict

advent.setup(2021, 12)
fin = advent.get_input()

lines = [l.strip().split('-') for l in fin.readlines()]
tunnels = defaultdict(set)

for line in lines:
    tunnels[line[0]].add(line[1])
    tunnels[line[1]].add(line[0])

# Part 1

def dfs(node, edges, seen, has_double):
    paths = 0

    if node == 'end': 
        return 1

    for child in edges[node]:
        if child.islower():
            if child not in seen:
                paths += dfs(child, edges, seen | { child }, has_double)
            elif has_double and child != 'start':
                paths += dfs(child, edges, seen | { child }, False)
        else:
            paths += dfs(child, edges, seen, has_double)

    return paths

res = dfs('start', tunnels, {'start'}, False)
advent.submit_answer(1, res)

# Part 2

res = dfs('start', tunnels, {'start'}, True)
advent.submit_answer(2, res)