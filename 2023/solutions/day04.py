#!/usr/bin/env python3

from utils import advent

advent.setup(2023, 4)
fin = advent.get_input()

cards = [[[int(number) for number in numbers.strip().split(" ") if number.isdigit()] for numbers in line.split(":")[1].split("|")] for line in fin]

result_1 = 0
result_2 = 0

num_cards = [1 for _ in range(0, len(cards))]
for idx, card in enumerate(cards):
    winning_numbers = 0
    for number in card[1]:
        if number in card[0]:
            winning_numbers += 1
            
    if winning_numbers > 0:
        result_1 += 2**(winning_numbers-1)
        
        for num in range(1, winning_numbers + 1):
            num_cards[idx + num] += num_cards[idx]
            
result_2 = sum(num_cards)

# Part 1
advent.submit_answer(1, result_1)

# Part 2
advent.submit_answer(2, result_2)
