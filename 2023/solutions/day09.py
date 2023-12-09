#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 9)
fin = advent.get_input()

lines = [[int(n) for n in line.split()] for line in fin.readlines()]

def find_previous(sequence):
    new_sequence = []
    for i in range(len(sequence) - 1):
        new_sequence.append(sequence[i + 1] - sequence[i])
        
    if all(n == 0 for n in new_sequence):
        return sequence[0] - 0
    else:
        return sequence[0] - find_previous(new_sequence)
    
def find_next(sequence):
    new_sequence = []
    for i in range(len(sequence) - 1):
        new_sequence.append(sequence[i + 1] - sequence[i])
        
    if all(n == 0 for n in new_sequence):
        return sequence[-1] + 0
    else:
        return sequence[-1] + find_next(new_sequence)

# Part 1
result_1 = sum(find_next(line) for line in lines)
advent.submit_answer(1, result_1)

# Part 2
result_2 = sum(find_previous(line) for line in lines)
advent.submit_answer(2, result_2)