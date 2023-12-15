#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 15)
fin = advent.get_input()

instructions = fin.read().strip().split(',')

def hash_algo(label):
    tmp = 0
    for c in label:
        tmp += ord(c)
        tmp *= 17
        tmp %= 256
    return tmp

def hashmap_algo(instr, boxes):
    if "-" in instr:
        label = instr[:-1]
        box = hash_algo(label)
        
        if label in boxes[box]:
            boxes[box].pop(label)
        
    if "=" in instr:
        label, num = instr.split("=")
        box = hash_algo(label)
        boxes[box][label] = int(num)

def fill_boxes():
    boxes = [{} for _ in range(256)]
    for instr in instructions:
        hashmap_algo(instr, boxes)
        
    return boxes

def focusing_power(boxes):
    fp = 0
    for i, box in enumerate(boxes):
        for j, label in enumerate(box):
            v = box[label]
            fp += (i + 1) * (j + 1) * v
            
    return fp

# Part 1 
result_1 = sum(hash_algo(instr) for instr in instructions)
advent.submit_answer(1, result_1)

# Part 2
result_2 = focusing_power(fill_boxes())
advent.submit_answer(2, result_2)