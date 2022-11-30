#!/usr/bin/env python3

from utils import advent

import copy

advent.setup(2021, 20)
fin = advent.get_input()

rules = fin.readline().strip()
image = [line.strip() for line in fin.readlines()[1:]]

def scale(image):
    new_image = [["."] * (len(image[0]) + 2) for _ in range(len(image) + 2)]
    for i in range(len(image)):
        for j in range(len(image[i])):
            new_image[i+1][j+1] = image[i][j]
    return new_image

def enhance(image):
    image = scale(scale(image))
    enhanced_image = [["."] * (len(image[0])) for _ in range(len(image))]

    for i in range(1, len(image)-1):
        for j in range(1, len(image[i])-1):
            combined = image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] + image[i][j-1] + image[i][j] + image[i][j+1] + image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]
            combined = combined.replace("#", "1").replace(".", "0")
            idx = int(combined, 2)

            enhanced_image[i][j] = rules[idx]

    for i in range(len(image)):
        enhanced_image[i][0] = "." if image[i][0] == "#" else "#"
        enhanced_image[i][len(image)-1] = "." if image[i][len(image)-1] == "#" else "#"

    return enhanced_image

def count_pixels(image):
    return sum(1 for line in image for pixel in line if pixel == "#")

# Part 1
def print_image(image):
    for line in image:
        print(line)

for _ in range(2):
    print_image(image)
    image = enhance(image)


res = count_pixels(image)
print(res)
advent.submit_answer(1, ans) # 5081

# Part 2

advent.submit_answer(2, max_offset)