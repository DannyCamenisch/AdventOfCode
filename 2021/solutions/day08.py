#!/usr/bin/env python3

from itertools import permutations
from utils import advent

advent.setup(2021, 8)
fin = advent.get_input()

lines = fin.readlines()

# Part 1
sum = 0

for line in lines:
    out = line.split("|")[1].strip()
    
    for c in out.split(" "):
        if len(c) in {2, 3, 4, 7}:
            sum += 1

advent.submit_answer(1, sum)

# Part 2
def evalSegment(input, perm):
    out = ""
    for i in input:
        cod = ""
        for c in perm:
            if c in i:
                cod += "1"
            else:
                cod += "0"

        if cod == "1111110":
            out += "0"
        elif cod == "0110000":
            out += "1"
        elif cod == "1101101":
            out += "2"
        elif cod == "1111001":
            out += "3"
        elif cod == "0110011":
            out += "4"
        elif cod == "1011011":
            out += "5"
        elif cod == "1011111":
            out += "6"
        elif cod == "1110000":
            out += "7"
        elif cod == "1111111":
            out += "8"
        elif cod == "1111011":
            out += "9"
        else:
            return -1
    return int(out)

sum = 0
perms = permutations(["a", "b", "c", "d", "e", "f", "g"])

for line in lines:
    input = line.split("|")[0].strip().split(" ")
    output = line.split("|")[1].strip().split(" ")

    for p in perms:
        if evalSegment(input, p) != -1:
            sum += evalSegment(output, p)
advent.submit_answer(2, sum)