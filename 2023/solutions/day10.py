#!/usr/bin/env python3

from collections import deque
from utils import advent

import networkx as nx

advent.setup(2023, 10)
fin = advent.get_input()

lines = fin.read().strip().split("\n")
board = {i + 1j * j: x for i, l in enumerate(lines) for j, x in enumerate(l)}
directions = {
    "|": [1, -1],
    "-": [1j, -1j],
    "J": [-1, -1j],
    "F": [1, 1j],
    "S": [-1, 1j],
    "7": [1, -1j],
    "L": [-1, 1j],
}

starting_point = next(k for k, v in board.items() if v == "S")
seen = {starting_point}
removed = set()

result_1 = 0

q = deque([(starting_point, 0)])
while q:
    z, d = q.popleft()
    result_1 = max(result_1, d)
    for dz in directions[board[z]]:
        new_z = z + dz
        if new_z not in seen:
            q.append((new_z, d + 1))
            seen.add(new_z)
        removed |= {2 * z, 2 * z + dz, 2 * z + 2 * dz}
        
# Part 1 
advent.submit_answer(1, result_1)

# Part 2
octdir = {-1, -1 + 1j, -1 - 1j, 1, 1 + 1j, 1 - 1j, -1j, 1j}
graph = nx.Graph()
for i in range(-1, 2 * len(lines) + 1):
    for j in range(-1, 2 * len(lines[0]) + 1):
        for dz in octdir:
            z = i + 1j * j
            graph.add_edge(z, z + dz)

for z in removed:
    graph.remove_node(z)

result_2 = sum(
        z.real % 2 == 0 and z.imag % 2 == 0
        for z in set.union(*(x for x in nx.connected_components(graph) if -1 - 1j not in x))
    )

advent.submit_answer(2, result_2)