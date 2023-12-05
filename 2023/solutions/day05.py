#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 5)
fin = advent.get_input()

seeds, *maps = fin.read().strip().split("\n\n")
seeds = [int(seed) for seed in seeds.split(":")[1].split()]

class Mapping:
    def __init__(self, map):
        lines = map.split("\n")[1:]
        self.mappings = [[int(x) for x in line.split()] for line in lines]
        
    def map_seed(self, seed):
        for dst, src, size in self.mappings:
            if src <= seed < src + size:
                return dst + seed - src
        return seed
    
    def map_seed_range(self, seed_range):
        mapped_intersections = []
        for dst, src, size in self.mappings:
            remaining_seed_range = []
            while seed_range:
                start, end = seed_range.pop()
            
                before = (start, min(end, src))
                inter = (max(start, src), min(src + size, end))
                after = (max(src + size, start), end)
                
                if before[1]>before[0]:
                    remaining_seed_range.append(before)
                if inter[1]>inter[0]:
                    mapped_intersections.append((inter[0] - src + dst, inter[1] - src + dst))
                if after[1]>after[0]:
                    remaining_seed_range.append(after)
                    
            seed_range = remaining_seed_range
                
        return seed_range + mapped_intersections

mappings = [Mapping(map) for map in maps]

# Part 1 
locations = []
for seed in seeds:
    for mapping in mappings:
        seed = mapping.map_seed(seed)
        
    locations.append(seed)

advent.submit_answer(1, min(locations))

# Part 2
locations = []
for start, size in list(zip(seeds[::2], seeds[1::2])):
    seed_range = [(start, start + size)]
    for mapping in mappings:
        seed_range = mapping.map_seed_range(seed_range)
    
    locations.append(min(seed_range[0]))
    
advent.submit_answer(2, min(locations))