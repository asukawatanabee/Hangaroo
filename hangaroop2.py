#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 02:29:16 2019

@author: asukawatanabe
"""

def ask_user_to_play() -> None:
    print("Well, that's perfect moment to play some Hangaroo!\n")
    while True:
        gameChoice = input("Play a game? \n").upper()
        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("Have a nice day! :)")
        else:
            print("Answer Yes or No")
            continue
        
