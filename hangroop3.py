#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 02:30:15 2019

@author: asukawatanabe
"""

def prepare_secret_word() -> None:
    for character in SECRET_WORD: 
        GUESS_WORD.append("-")
    print("Ok, length of word you need to guess:", LENGTH_WORD, "characters")
    print("You can enter only 1 letter from a-z\n\n")
    print_word_to_guess(GUESS_WORD)