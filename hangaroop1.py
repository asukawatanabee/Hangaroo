#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 02:29:05 2019

@author: asukawatanabe
"""

import random, sys
from typing import List

WORD_LIST = [
        "apple", "umbrella", "door", "computer", "glass", "juice", "chair", "desktop",
        "laptop", "dog", "cat", "lemon", "cable", "mirror", "hat", "banana", "bread", "python"
        ]
GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST) 
LENGTH_WORD = len(SECRET_WORD)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def print_word_to_guess(letters: List) -> None:
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:
    print("You are on guess {0}/{1}.".format(current, total))


def beginning() -> None:
    print("Hello!Welcome to Hangaroo!\n")
    while True:
        name = input("Name: \n").strip()
        if name == '':
            print("You can't do that! No blank lines")
        else:
            break