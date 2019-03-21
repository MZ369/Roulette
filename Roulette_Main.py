# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:33:16 2019

@author: Mads Kragh-Berner
"""
from Roulette_Lib import Player, Board, Pricepool 

def checksum(bet):
    if isinstance(bet, int):
        if bet >= 0 and bet <= 36:
            return True
        else:
            return False
    else:
        if bet in pool1.bet_return.keys():
            return True
        else:
            return False
        
table1 = Board()
pool1 = Pricepool()

player_dict = {}

while True:
    player_name = ' '
    while player_name != '':
        player_capital = 0
        player_name = input("New Player? ").title()
        if player_name != '' and player_name != 'Exit':
            while player_capital <= 0:
                try: 
                    player_capital = int(input(player_name + "'s Capital? "))
                    if player_capital <= 0:
                        print("Insufficient Capital!")
                except ValueError:
                    print("Invalid Number!")
            player_dict[player_name] = Player(player_name, player_capital)
        elif player_name == 'Exit':
            print("The game has stopped! The player ended with:")
            for player in player_dict.values():
                print("\n" + player.name + ", " + str(player.capital) + "$")
            print("\n")
            raise SystemExit()
    
    for player in player_dict.values():
        bet = ' '
        while bet != '':
            value = player.capital + 1
            bet = input(player.name + " make your bet! ").title()
            try:
                bet = int(bet)
            except ValueError:
                pass
            if checksum(bet):
                while value > player.capital:
                    try:
                        value = int(input("How much? "))
                        if value > player.capital:
                            print("Insufficient Capital!")
                    except ValueError:
                        print("Invalid Number!")
                player.make_bet(bet, value) 
            elif bet != '' and checksum(bet) == False:
                print("Invalid Bet!")
    
    roll, upshot = table1.play()
    
    print("\nThe roulette rolled a " + str(roll) + "!")
    
    pool1.price_calculate(player_dict, upshot)
    
    del_list = []
    
    for player in player_dict.values():
        print("\n" + player.name + " now have " + str(player.capital) + "$")
        if player.capital == 0:
            print(player.name + " have been remove from the table due to insufficient capital!")
            del_list.append(player.name)
    
    for player in del_list:
        del player_dict[player.name]     
        
    print("\n______N_E_W___R_O_U_N_D______")