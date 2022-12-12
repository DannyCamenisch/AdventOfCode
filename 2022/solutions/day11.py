#!/usr/bin/env python3

from utils import advent
import math

advent.setup(2022, 11)
fin = advent.get_input()

lines = [line for line in fin.read().strip().split('\n')]

class Monkey:
    def __init__(self, lines, div=3):
        self.items = [int(i) for i in lines[1].split(':')[1].split(',')]
        self.op    = lines[2].split('= old')[1].strip()
        self.test  = int(lines[3].split('by')[1].strip())
        self.out1  = int(lines[4].split('monkey')[1].strip())
        self.out2  = int(lines[5].split('monkey')[1].strip())
        self.div   = div

        self.numInsepcted = 0

    def addItem(self, item):
        self.items.append(item)

    def setDiv(self, div):
        self.div = div

    def inspectItems(self, monkeys):
        for item in self.items:
            num = 0
            if self.op.split(' ')[1] == 'old':
                num = item
            else:
                num = int(self.op.split(' ')[1])

            if self.op.split(' ')[0] == '+':
                num += item
            else:
                num *= item

            num = math.floor(num / 3)

            if num % self.test == 0:
                monkeys[self.out1].addItem(num)
            else:
                monkeys[self.out2].addItem(num)
            
            self.numInsepcted += 1
        
        self.items = []

    def inspectItemsHard(self, monkeys):
        for item in self.items:
            num = 0
            if self.op.split(' ')[1] == 'old':
                num = item
            else:
                num = int(self.op.split(' ')[1])

            if self.op.split(' ')[0] == '+':
                num += item
            else:
                num *= item

            num = num % self.div

            if num % self.test == 0:
                monkeys[self.out1].addItem(num)
            else:
                monkeys[self.out2].addItem(num)
            
            self.numInsepcted += 1
        
        self.items = []

monkeys = []

for i in range(0, len(lines), 7):
    monkeys.append(Monkey(lines[i:i+7]))

# Part 1

itemsInspected = []

for _ in range(20):
    for monkey in monkeys:
        monkey.inspectItems(monkeys)

for monkey in monkeys:
    itemsInspected.append(monkey.numInsepcted)

sortedItems = sorted(itemsInspected)

advent.submit_answer(1, sortedItems[-1] * sortedItems[-2])

# Part 2

monkeys = []

for i in range(0, len(lines), 7):
    monkeys.append(Monkey(lines[i:i+7]))

div = 1
for monkey in monkeys:
    div *= monkey.test

for monkey in monkeys:
    monkey.setDiv(div)

for _ in range(10000):
    for monkey in monkeys:
        monkey.inspectItemsHard(monkeys)

for monkey in monkeys:
    itemsInspected.append(monkey.numInsepcted)

sortedItems = sorted(itemsInspected)

advent.submit_answer(2, sortedItems[-1] * sortedItems[-2])