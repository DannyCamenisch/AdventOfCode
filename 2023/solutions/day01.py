#!/usr/bin/env python3

import string
from utils import advent

advent.setup(2023, 1)
fin = advent.get_input()

lines = [line for line in fin.read()[:-1].split('\n')]

result = 0
for line in lines:
    tmp = ""
    for char in line:
        if char in string.digits:
            tmp += char
            
    result += int(tmp[0] + tmp[-1])

# Part 1 
advent.submit_answer(1, result)

# Part 2

result = 0

digit_mapping = {'one': 'one1one', 'two': 'two2two', 'three': 'three3three', 'four': 'four4four', 'five': 'five5five',
                    'six': 'six6six', 'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'}

for line in lines:
    for word, digit in digit_mapping.items():
        line = line.replace(word, digit)
            
    tmp = ""
    for char in line:
        if char in string.digits:
            tmp += char
                        
    result += int(tmp[0] + tmp[-1])
        
advent.submit_answer(2, result)