#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 6)
fin = advent.get_input()

times, distances = fin.read().strip().split('\n')

times = [int(t) for t in times.split()[1:]]
distances = [int(d) for d in distances.split()[1:]]

# Part 1 

result_1 = 1
for t, d in zip(times, distances):
    tmp = 0
    for i in range(0, t + 1):
        if i * (t - i) > d:
            tmp += 1
        
    result_1 *= tmp

advent.submit_answer(1, result_1)

# Part 2

time = int(str(times[0]) + str(times[1]) + str(times[2]) + str(times[3]))
distance = int(str(distances[0]) + str(distances[1]) + str(distances[2]) + str(distances[3]))

result_2 = 0
for i in range(0, time + 1):
    if i * (time - i) > distance:
        result_2 += 1
                    
advent.submit_answer(2, result_2)