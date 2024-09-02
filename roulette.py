# Implementation of the roulette game in Python
# Author: Eren Gul

import random

class Roulette:
    def __init__(self):
        self.rounds = 0
        self.num = None
    
    def __str__(self):
        return f"current number: {self.num} current rounds: {self.rounds}"
    
    def roll(self):
        self.num = random.randrange(0, 39) # 37 means 0, 38 means 00
        self.rounds +=1
        return self.num, self.rounds
    
    def inside_bet(self, num1, bet_amount):
        if self.num == num1:
            bet_amount *= 35
        else:
            bet_amount = 0
        return bet_amount

    def first(self, bet_amount):
        if self.num in [1,4,7,10,13,16,19,22,25,28,31,34]:
            bet_amount *= 3
        else:
            bet_amount = 0
        return bet_amount
    
    def second(self, bet_amount):
        if self.num in [2,5,8,11,14,17,20,23,26,29,32,35]:
            bet_amount *= 3
        else:
            bet_amount = 0
        return bet_amount
    
    def third(self, bet_amount):
        if self.num in [3,6,9,12,15,18,21,24,27,30,33,36]:
            bet_amount *= 3
        else:
            bet_amount = 0
        return bet_amount
    
    def one_twelve(self, bet_amount):
        if self.num in [1,2,3,4,5,6,7,8,9,10,11,12]:
            bet_amount *= 3
        else:
            bet_amount = 0
        return bet_amount
    
    def thirteen_twentyfour(self, bet_amount):
        if self.num in [13,14,15,16,17,18,19,20,21,22,23,24]:
            bet_amount *= 3
        else:
            bet_amount = 0
        return bet_amount

    def twentyfive_thirtysix(self, bet_amount):
        if self.num in [25,26,27,28,29,30,31,32,33,34,35,36]:
            bet_amount *= 3
        else:
            bet_amount = 0
        return bet_amount
    
    def one_eighteen(self, bet_amount):
        if self.num in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
            bet_amount *= 2
        else:
            bet_amount = 0
        return bet_amount
    
    def nineteen_thirtysix(self, bet_amount):
        if self.num in [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]:
            bet_amount *= 2
        else:
            bet_amount = 0
        return bet_amount
    
    def even(self, bet_amount):
        if self.num % 2 == 0 and self.num != 38:
            bet_amount *= 2
        else:
            bet_amount = 0
        return bet_amount

    def odd(self, bet_amount):
        if (self.num +1) % 2 == 0 and self.num != 37:
            bet_amount *= 2
        else:
            bet_amount = 0
        return bet_amount
    
    def red(self, bet_amount):
        if self.num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
            bet_amount *= 2
        else:
            bet_amount = 0
        return bet_amount
    
    def black(self, bet_amount):
        if self.num in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
            bet_amount *= 2
        else:
            bet_amount = 0
        return bet_amount
    
    def green(self, bet_amount):
        if self.num in [37, 38]:
            bet_amount *= 18
        else:
            bet_amount = 0
        return bet_amount

    def two(self, num1, num2, bet_amount):
        if num2 == num1 + 1 and num1 % 3 != 0:
            if self.num in [num1, num2]:
                bet_amount *= 18
        elif num2 == num1 + 3 and num1 < 34:
            if self.num in [num1, num2]:
                bet_amount *= 18
        else:
            bet_amount == 0
        return bet_amount

    def three(self, num1, bet_amount):
        if self.num in [num1, num1+1, num1+2] and (num1+2) % 3 == 0:
            bet_amount *= 12
        else:
            bet_amount = 0
        return bet_amount
    
    def four(self, num1, num2, num3, num4, bet_amount):
        if num2 == num1 + 1 and num3 == num2 + 2 and num4 == num3 +1 and num1 < 33:
            if self.num in [num1, num2, num3, num4]:
                bet_amount *= 9
            else:
                bet_amount = 0

    def six(self, num1, bet_amount):
        if self.num in [num1, num1+1, num1+2, num1+3, num1+4, num1+5] and (num1+2) % 3 == 0 and num1 != 36:
            bet_amount *= 6
        else:
            bet_amount = 0
        return bet_amount
    