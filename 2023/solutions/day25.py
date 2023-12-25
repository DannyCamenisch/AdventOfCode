#!/usr/bin/env python3

import networkx as nx

from utils import advent

advent.setup(2023, 25)
fin = advent.get_input()

graph = nx.Graph()
for l in fin.read().splitlines():
    a, *dsts = l.split()
    a = a[:-1]
    for dst in dsts:
        graph.add_edge(a, dst)

_, partitions = nx.stoer_wagner(graph)

# Part 1
result_1 = len(partitions[0]) * len(partitions[1])
advent.submit_answer(1, result_1)
