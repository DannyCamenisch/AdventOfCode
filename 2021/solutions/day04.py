#!/usr/bin/env python3

from utils import advent

advent.setup(2021, 4)
fin = advent.get_input()

draws = list(map(int, fin.readline().strip().split(',')))

class BingoMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.boolMatrix = [[False for x in range(5)] for y in range(5)]
        self.winner = False

    def check(self):
        for i in range(5):
            if self.boolMatrix[i][0] & self.boolMatrix[i][1] & self.boolMatrix[i][2] & self.boolMatrix[i][3] & self.boolMatrix[i][4]:
                return True
            if self.boolMatrix[0][i] & self.boolMatrix[1][i] & self.boolMatrix[2][i] & self.boolMatrix[3][i] & self.boolMatrix[4][i]:
                return True

    def draw(self, number):
        if self.winner:
            return 0

        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == number:
                    self.boolMatrix[i][j] = True
        
        if self.check():
            self.winner = True
            sum = 0
            for i in range(5):
                for j in range(5):
                    if not self.boolMatrix[i][j]:
                        sum += self.matrix[i][j]
            return sum * number
        
        return 0
    
    def print(self):
        print("Matrix: ")
        for row in self.matrix:
            print(row)
        print("\nBoolean Matrix: ")
        for row in self.boolMatrix:
            print(row)
        print("")

#parse matrix input
matrixes = []
matrix = []
for line in fin:
    horizontal = (list(map(int, line.strip().split())))
    if horizontal:
        matrix.append(horizontal)
    else:
        if matrix:
            matrixes.append(BingoMatrix(matrix))
            matrix = []

# Part 1

winner = 0

for num in draws:
    for mat in matrixes:
        winner = mat.draw(num)
        if winner:
            break
    else:
        continue
    break

advent.submit_answer(1, winner)

# Part 2

winner = 0

for num in draws:
    for mat in matrixes:
        temp = mat.draw(num)
        if temp:
            winner = temp

advent.submit_answer(2, winner)