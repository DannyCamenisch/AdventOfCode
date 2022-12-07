#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 7)
fin = advent.get_input()

lines = [line for line in fin.read().strip().split('\n')]

currentPath = ''
dirs  = []
files = {}

# Part 1

for line in lines:
    if line.startswith('$ cd /'):
        currentPath = ''
        continue
    elif line.startswith('$ cd ..'):
        currentPath = currentPath[:currentPath.rfind('/')]
        continue
    elif line.startswith('$ cd'):
        currentPath += '/' + line[5:]
        continue
    elif line.startswith('$ ls'):
        continue
    elif line.startswith('dir'):
        d = line.split(' ')[1]
        dirs.append(currentPath + '/' + d)
        continue
    else:
        file = line.split(' ')[1]
        size = int(line.split(' ')[0])
        files[currentPath + '/' + file] = size

# Part 1

ans = 0

dirs.append('/')

for d in dirs:
    tmp = 0

    for file in files.keys():
        if file.startswith(d):
            tmp += files[file]
    
    if tmp <= 100000:
        ans += tmp

advent.submit_answer(1, ans)

# Part 2

ans = 70000000

total_size = 0
for file in files.keys():
    total_size += files[file]

for d in dirs:
    tmp = 0

    for file in files.keys():
        if file.startswith(d):
            tmp += files[file]
    
    if 70000000 - total_size + tmp >= 30000000:
        ans = min(ans, tmp)

advent.submit_answer(2, ans)
