#!/usr/bin/env python3

import math
from utils import advent

advent.setup(2023, 8)
fin = advent.get_input()

instructions, maps = fin.read().strip().split('\n\n')

graph = {}
for m in maps.split('\n'):
    k, v = m.split(' = ')
    graph[k] = v[1:-1].split(', ')
    
# Part 1 
result_1 = 0

current_node = "AAA"
current_instruction = 0

while current_node != "ZZZ":
    current_node = graph[current_node][0 if instructions[current_instruction] == "L" else 1]
    current_instruction = (current_instruction + 1) % len(instructions)
    result_1 += 1

advent.submit_answer(1, result_1)

# Part 2
steps = 0

current_nodes = [node for node in graph.keys() if node[2] == "A"]
current_instruction = 0

first_z = [0 for node in current_nodes]
while any(z == 0 for z in first_z):
    for idx, node in enumerate(current_nodes):
        current_nodes[idx] = graph[node][0 if instructions[current_instruction] == "L" else 1]
        
        if current_nodes[idx][2] == "Z" and first_z[idx] == 0:
            first_z[idx] = steps + 1
        
        
    current_instruction = (current_instruction + 1) % len(instructions)
    steps += 1

result_2 = math.lcm(*first_z)
advent.submit_answer(2, result_2)