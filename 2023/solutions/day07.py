#!/usr/bin/env python3

from collections import defaultdict
from utils import advent

advent.setup(2023, 7)
fin = advent.get_input()

lines = fin.read().strip().split('\n')

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13,
    'A': 14
}

card_values_joker = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 1, 'Q': 12, 'K': 13,
    'A': 14
}

class Hand:
    def __init__(self, line) -> None:
        self.hand, self.bet = line.split(' ')
        
        cards = defaultdict(int)
        for card in self.hand:
            cards[card] += 1
            
        self.values = sorted(cards.values(), reverse=True)
        
    def __lt__(self, other):
        for i in range(len(self.values)):
            if self.values[i] < other.values[i]:
                return True
            elif self.values[i] > other.values[i]:
                return False
        
        for i in range(5):
            if card_values[self.hand[i]] < card_values[other.hand[i]]:
                return True
            elif card_values[self.hand[i]] > card_values[other.hand[i]]:
                return False
            
        return False
    
class Hand_Joker:
    def __init__(self, line) -> None:
        self.hand, self.bet = line.split(' ')
        
        cards = defaultdict(int)
        for card in self.hand:
            cards[card] += 1
        
        jokers = cards['J']
        cards["J"] = 0
        self.values = sorted(cards.values(), reverse=True)
        self.values[0] += jokers
        
        if self.values.count(0) == 1:
            self.values.remove(0)
        
    def __lt__(self, other):
        for i in range(len(self.values)):
            if self.values[i] < other.values[i]:
                return True
            elif self.values[i] > other.values[i]:
                return False
        
        for i in range(5):
            if card_values_joker[self.hand[i]] < card_values_joker[other.hand[i]]:
                return True
            elif card_values_joker[self.hand[i]] > card_values_joker[other.hand[i]]:
                return False
            
        return False
        
hands = sorted([Hand(line) for line in lines])
hands_joker = sorted([Hand_Joker(line) for line in lines])

# Part 1
result_1 = sum((idx + 1) * int(hand.bet) for idx, hand in enumerate(hands))
advent.submit_answer(1, result_1)

# Part 2
result_2 = sum((idx + 1) * int(hand.bet) for idx, hand in enumerate(hands_joker))
advent.submit_answer(2, result_2)