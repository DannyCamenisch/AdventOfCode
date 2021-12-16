#!/usr/bin/env python3

from sys import builtin_module_names
from utils import advent
from math import prod

advent.setup(2021, 16)
fin = advent.get_input()

hexcode =  fin.readline().strip()
bitcode =  bin(int(hexcode, base=16)).lstrip('0b')

if hexcode[0] in '4567':
    bitcode = '0' + bitcode
elif hexcode[0] in '23':
    bitcode = '00' + bitcode
elif hexcode[0] == '1':
    bitcode = '000' + bitcode
elif hexcode[0] == '0':
    bitcode = '0000' + bitcode

versionSum = 0

def parse_bitcode(bitcode):
    global versionSum

    version = int(bitcode[0:3], base=2)
    id      = int(bitcode[3:6], base=2)

    versionSum += version

    if id == 4: # package is a literal value
        bitcode = bitcode[6:]
        numStr = ""

        while True:
            numStr += bitcode[1:5]

            if bitcode[0] == '0':
                return int(numStr, base=2), bitcode[5:]

            bitcode = bitcode[5:]
            
        #res.append(int(numStr, base=2))

    else: # package is a operator
        lengthID = int(bitcode[6:7], base=2)
        lit = []

        if lengthID == 0:
            length = int(bitcode[7:22], base=2)
            subpackage = bitcode[22:22+length]

            while subpackage:
                tmp, subpackage = parse_bitcode(subpackage)
                lit.append(tmp)
            bitcode = bitcode[(22 + length):]
                
        if lengthID == 1:
            length = int(bitcode[7:18], base=2)

            bitcode = bitcode[18:] # remove the operator and its length from the bitcode
            for _ in range(length):
                tmp, bitcode = parse_bitcode(bitcode)
                lit.append(tmp)

        if id == 0:
            return sum(lit), bitcode
        elif id == 1:
            return prod(lit), bitcode
        elif id == 2:
            return min(lit), bitcode
        elif id == 3:
            return max(lit), bitcode
        elif id == 5:
            return int(lit[0] > lit[1]), bitcode
        elif id == 6:
            return int(lit[0] < lit[1]), bitcode
        elif id == 7:
            return int(lit[0] == lit[1]), bitcode

# Part 1
res, _ = parse_bitcode(bitcode)

advent.submit_answer(1, versionSum)

# Part 2

advent.submit_answer(2, res)