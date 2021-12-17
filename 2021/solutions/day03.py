#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 3)
fin = advent.get_input()

numbers = tuple(map(str, fin.readlines()))

# Part 1 
d = [0 for _ in range(len(numbers[0])-1)]

for i in range(len(numbers[0])):
    for j in range(len(numbers)):
        if numbers[j][i] == '1':
            d[i] += 1

gamma = ""
epsilon = ""
for i in range(len(d)):
    if d[i] >= len(numbers)/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

advent.submit_answer(1, int(gamma, 2) * int(epsilon, 2))

# Part 2
A = numbers
B = numbers
for i in range(12):
    if len(A) > 1:
        a0 = len([x  for x in A if x[i]=='0'])
        a1 = len([x  for x in A if x[i]=='1'])
        if a1 >= a0:
            A = [x for x in A if x[i]=='1']
        else:
            A = [x for x in A if x[i]=='0']
    if len(B) > 1:
        b0 = len([x  for x in B if x[i]=='0'])
        b1 = len([x  for x in B if x[i]=='1'])
        if b1 >= b0:
            B = [x for x in B if x[i]=='0']
        else:
            B = [x for x in B if x[i]=='1']

advent.submit_answer(2, int(A[0].strip(), 2) * int(B[0].strip(), 2))