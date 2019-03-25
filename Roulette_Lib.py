# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:59:53 2019

@author: Mads Kragh-Berner
"""
import random

class Player:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital 
        self.bet_list = {}
    
    def make_bet(self, bet, value):
        self.capital -= value
        self.bet_list[bet] = value
    
    def cash_in(self, price):
        self.capital += price
        self.bet_list = {}

class Pricepool:
    def __init__(self):
        self.bet_return = {"Red": 2, "Black": 2, "Even": 2, "Odd": 2, "Low": 2,
                           "High": 2, "Dozen 1": 3, "Dozen 2": 3, "Dozen 3": 3,
                           "Column 1": 3, "Column 2": 3, "Column 3": 3}  
        
    def price_calculate(self, players, upshot):
        for player in players.values():
            price_outside = 0
            price_inside = 0
            bet_inside = 0
            for bet, value in player.bet_list.items():
                for wincon in upshot:
                    if bet == wincon:
                        if isinstance(bet, int):
                            price_inside += value*36
                        else:
                            price_outside += value*self.bet_return[bet]
                    if isinstance(bet, int):
                        bet_inside += 1
            if bet_inside == 0:
                price = price_outside
            else:
                price = price_outside + (price_inside // bet_inside)    
            player.cash_in(price)
    
class Board: 
    def __init__(self):
        self.bet_upshot = {0: [0], 
                           1: [1, "Red", "Odd", "Low", "Dozen 1", "Column 1"],
                           2: [2, "Black", "Even", "Low", "Dozen 1", "Column 2"],
                           3: [3, "Red", "Odd", "Low", "Dozen 1", "Column 3"],
                           4: [4, "Black", "Even", "Low", "Dozen 1", "Column 1"],
                           5: [5, "Red", "Odd", "Low", "Dozen 1", "Column 2"],
                           6: [6, "Black", "Even", "Low", "Dozen 1", "Column 3"],
                           7: [7, "Red", "Odd", "Low", "Dozen 1", "Column 1"],
                           8: [8, "Black", "Even", "Low", "Dozen 1", "Column 2"],
                           9: [9, "Red", "Odd", "Low", "Dozen 1", "Column 3"],
                           10: [10, "Black", "Even", "Low", "Dozen 1", "Column 1"],
                           11: [11, "Black", "Odd", "Low", "Dozen 1", "Column 2"],
                           12: [12, "Red", "Even", "Low", "Dozen 1", "Column 3"],
                           13: [13, "Black", "Odd", "Low", "Dozen 2", "Column 1"],
                           14: [14, "Red", "Even", "Low", "Dozen 2", "Column 2"],
                           15: [15, "Black", "Odd", "Low", "Dozen 2", "Column 3"],
                           16: [16, "Red", "Even", "Low", "Dozen 2", "Column 1"],
                           17: [17, "Black", "Odd", "Low", "Dozen 2", "Column 2"],
                           18: [18, "Red", "Even", "Low", "Dozen 2", "Column 3"],
                           19: [19, "Red", "Odd", "High", "Dozen 2", "Column 1"],
                           20: [20, "Black", "Even", "High", "Dozen 2", "Column 2"],
                           21: [21, "Red", "Odd", "High", "Dozen 2", "Column 3"],
                           22: [22, "Black", "Even", "High", "Dozen 2", "Column 1"],
                           23: [23, "Red", "Odd", "High", "Dozen 2", "Column 2"],
                           24: [24, "Black", "Even", "High", "Dozen 2", "Column 3"],
                           25: [25, "Red", "Odd", "High", "Dozen 3", "Column 1"],
                           26: [26, "Black", "Even", "High", "Dozen 3", "Column 2"],
                           27: [27, "Red", "Odd", "High", "Dozen 3", "Column 3"],
                           28: [28, "Black", "Even", "High", "Dozen 3", "Column 1"],
                           29: [29, "Black", "Odd", "High", "Dozen 3", "Column 2"],
                           30: [30, "Red", "Even", "High", "Dozen 3", "Column 3"],
                           31: [31, "Black", "Odd", "High", "Dozen 3", "Column 1"],
                           32: [32, "Red", "Even", "High", "Dozen 3", "Column 2"],
                           33: [33, "Black", "Odd", "High", "Dozen 3", "Column 3"],
                           34: [34, "Red", "Even", "High", "Dozen 3", "Column 1"],
                           35: [35, "Black", "Odd", "High", "Dozen 3", "Column 2"],
                           36: [36, "Red", "Even", "High", "Dozen 3", "Column 3"]}
    
    def play(self):
        roll = random.randint(0, 36)
        return (roll, self.bet_upshot[roll])