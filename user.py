# Implementation of the roulette game in Python
# Author: Eren Gul

from roulette import Roulette

class User:
    def __init__(self, balance):
        self.balance = balance
        self.game = Roulette()
        self.interactions = {
            "inside_bet": lambda num1, bet_amount: self.game.inside_bet(num1, bet_amount),
            "first": lambda bet_amount: self.game.first(bet_amount),
            "second": lambda bet_amount: self.game.second(bet_amount),
            "third": lambda bet_amount: self.game.third(bet_amount),
            "one_twelve": lambda bet_amount: self.game.one_twelve(bet_amount),
            "thirteen_twentyfour": lambda bet_amount: self.game.thirteen_twentyfour(bet_amount),
            "twentyfive_thirtysix": lambda bet_amount: self.game.twentyfive_thirtysix(bet_amount),
            "even": lambda bet_amount: self.game.even(bet_amount),
            "odd": lambda bet_amount: self.game.odd(bet_amount),
            "red": lambda bet_amount: self.game.red(bet_amount),
            "black": lambda bet_amount: self.game.black(bet_amount),
            "green": lambda bet_amount: self.game.green(bet_amount),
            "two": lambda num1, num2, bet_amount: self.game.even(num1, num2, bet_amount),
            "three": lambda num1, bet_amount: self.game.even(num1, bet_amount),
            "four": lambda num1, num2, num3, num4, bet_amount: self.game.even(num1, num2, num3, num4, bet_amount),
            "six": lambda num1, bet_amount: self.game.even(num1, bet_amount),
        }
        self.history = []
    def place_bet(self, bet_type, bet_amount, *args):
        if bet_amount < self.balance:
            if bet_type in self.interactions:
                self.game.roll()
                print(self.game)
                self.balance -= bet_amount
                returns = self.interactions[bet_type](bet_amount, *args)
                self.balance += returns
                print(f"You bet {bet_amount} and your returns are {returns}. Your current balance is {self.balance}")
                if returns == 0:
                    self.history.append([bet_type, bet_amount, "lost"])
                else:
                    self.history.append([bet_type, bet_amount, "won"])
            else:
                print("INVALID BET TYPE.")
        else:
            print("YOU DO NOT HAVE ENOUGH BALANCE FOR THIS BET. PLEASE TRY AGAIN.")

