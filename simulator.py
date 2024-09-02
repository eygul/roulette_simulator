#Implementation of the Martingale roulette strategy in Python
#Author: Eren Gul

from user import User
import csv 

def Martingale():
    fieldnames = ["bet_type", "initial_balance", "target_balance", "min_bet", "rounds", "final_balance"]
    user = User(1000)
    while user.balance >= 0:
        if user.history == []:
            user.place_bet("red", 1)
        else:
            if user.history[-1][-1] == "won":
                user.place_bet("red", 1)
            else:
                user.place_bet("red", user.history[-1][1]*2)
        if user.balance >= 2000:
            with open (r"results.csv", "a", newline='') as results:
                writer = csv.DictWriter(results, fieldnames=fieldnames)
                writer.writerow({"bet_type": "red", "initial_balance": 1000, "min_bet": 1, "rounds": user.game.rounds, "final_balance": user.balance})
            break
        if user.balance < user.history[-1][1]*2:
            with open (r"results.csv", "a", newline='') as results:
                writer = csv.DictWriter(results, fieldnames=fieldnames)
                writer.writerow({"bet_type": "red", "initial_balance": 1000, "target_balance": 2000, "min_bet": 1, "rounds": user.game.rounds, "final_balance": user.balance})
            break
        
for i in range (34):        
    Martingale()