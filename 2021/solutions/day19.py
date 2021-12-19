#!/usr/bin/env python3

from utils import advent

import itertools
import operator

advent.setup(2021, 19)
fin = advent.get_input()

scanners = []
for line in fin.read().strip().split("\n\n"):
    scanner = [tuple(map(int, line.split(","))) for line in line.split("\n")[1:]]
    scanners.append(scanner)

visited = set()
individual_beacons = set()
offsets = [(0, 0, 0)] * len(scanners)

# rotates a given beacon by rx, ry, rz times 90 degrees in the given direction
def rotate(beacon, rx, ry, rz):
    x, y, z = beacon
    for _ in range(rx):
        x, y, z = x, z, -y
    for _ in range(ry):
        x, y, z = z, y, -x
    for _ in range(rz):
        x, y, z = y, -x, z
    return x, y, z


def match(fixed_beacons, beacons):
    fixed_set = set(fixed_beacons)
    for r in itertools.product(range(4), repeat=3):
        r_beacons = [rotate(b, *r) for b in beacons]
        for b in fixed_beacons:
            for r_b in r_beacons:
                offset = tuple(map(operator.sub, b, r_b))
                offset_beacons = [tuple(map(operator.add, beacon, offset)) for beacon in r_beacons]
                if len(set(offset_beacons) & fixed_set) >= 12:
                    return [offset_beacons, offset]
    

def search(i, beacons, cur_offset):
    offsets[i] = cur_offset
    individual_beacons.update(beacons)
    visited.add(i)
    for i, scanner in enumerate(scanners):
        if i in visited:
            continue
        match_ = match(beacons, scanner)
        if match_:
            search(i, match_[0], match_[1] + cur_offset)

# Part 1
search(0, scanners[0], (0, 0, 0))
advent.submit_answer(1, len(individual_beacons))

# Part 2
max_offset = 0
for a, b in itertools.product(offsets, repeat=2):
    max_offset = max(max_offset, abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]))

advent.submit_answer(2, max_offset)