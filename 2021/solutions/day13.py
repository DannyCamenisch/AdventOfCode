#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 13)
fin = advent.get_input()

dots, instr = [l.strip().split("\n") for l in fin.read().split("\n\n")]
max_x = int(max(dots, key=lambda x: int(x.split(",")[0])).split(",")[0])
max_y = int(max(dots, key=lambda x: int(x.split(",")[1])).split(",")[1])

paper = [[False for _ in range(max_y + 1)] for _ in range(max_x + 1)]
for d in dots:
    x, y = [int(i) for i in d.split(",")]
    paper[x][y] = True

def print_paper(paper):
    transposed = list()
    for i in range(len(paper[0])):
        row = list()
        for sublist in paper:
            row.append(sublist[i])
        transposed.append(row)

    for row in transposed:
        print("".join(["#" if i else "." for i in row]))

def fold_paper(paper, fold):
    dir, ind = fold.split(" ")[2].split("=")
    ind = int(ind)

    if dir == "x":
        for x in range(1, max_x - ind + 1):
            for y in range(max_y + 1):
                paper[ind - x][y] |= paper[ind + x][y]
                paper[ind + x][y] = False
    else:
        for y in range(1, max_y - ind + 1):
            for x in range(max_x + 1):
                paper[x][ind - y] |= paper[x][ind + y]
                paper[x][ind + y] = False

# Part 1
fold_paper(paper, instr[0])
res = sum(sum(row) for row in paper)

advent.submit_answer(1, res)

# Part 2
for i in range(1, len(instr)):
    fold_paper(paper, instr[i])
    
advent.submit_answer(2, "EAHKRECP")