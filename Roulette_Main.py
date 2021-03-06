# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:33:16 2019

@author: Mads Kragh-Berner
"""
from Roulette_Lib import Player, Board, Pricepool 
"""
Funktioner/Variabler
"""
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
"""
Main Loop
"""
while True:
    """
    Player Section
    """
    player_name = ' '
    while player_name != '':
        player_capital = 0
        player_name = input("New Player? ").title()
        if player_name in player_dict.keys():
            print(player_name + ", your capital is " + str(player_dict[player_name].capital) + "$") 
            while player_capital != '':
                player_capital = input("Add more? ")
                if player_capital == '':
                    pass
                else:
                    try:
                        player_capital = int(player_capital) + player_dict[player_name].capital
                        player_dict[player_name] = Player(player_name, player_capital)
                    except ValueError:
                        print("Invalid Number!")
        elif player_name != '' and player_name != 'Leave' and player_name != 'Exit':
            while player_capital <= 0:
                try: 
                    player_capital = int(input(player_name + "'s Capital? "))
                    if player_capital <= 0:
                        print("Insufficient Capital!")
                except ValueError:
                    print("Invalid Number!")
            player_dict[player_name] = Player(player_name, player_capital)  
        elif player_name == 'Leave':
            player_leave = input("Name of Leaving Player? ").title()
            try:
                if player_leave != '':
                    print(player_leave + " leaves the table with " + str(player_dict[player_leave].capital) + "$")
                    del player_dict[player_leave]
            except KeyError:
                print("...")   
        elif player_name == 'Exit':
            print("The game has stopped! The player ended with:")
            for player in player_dict.values():
                print("\n" + player.name + ", " + str(player.capital) + "$")
            print("\n")
            raise SystemExit()
    """
    Bet Section
    """
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
            if player.capital == 0:
                print("All In!")
                break
    """
    Play/Elimination Section
    """
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
        del player_dict[player]    
        
    print("\n______N_E_W___R_O_U_N_D______")