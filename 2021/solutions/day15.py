#!/usr/bin/env python3

from utils import advent
from collections import defaultdict
from utils.graph import Graph

advent.setup(2021, 15)
fin = advent.get_input()

map = [[int(c) for c in l.strip()] for l in fin.readlines()]

g = Graph(map)

# Part 1
v = g.dijkstra(0)
advent.submit_answer(1, v[len(map) * len(map[0]) - 1])

# Part 2

map2 = [[0] * len(map[0]) * 5 for _ in range(len(map) * 5)]

for i in range(len(map2)):
    for j in range(len(map2[0])):
        x = i % len(map)
        y = j % len(map[0])

        offset = int(i / len(map)) + int(j / len(map[0]))

        map2[i][j] = (map[x][y] + offset) if (map[x][y] + offset) < 10 else (map[x][y] + offset) % 9

g2 = Graph(map2)
v = g2.dijkstra(0)

advent.submit_answer(2, v[len(map2) * len(map2[0]) - 1])