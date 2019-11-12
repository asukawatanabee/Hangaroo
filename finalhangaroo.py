#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 02:18:02 2019

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


def prepare_secret_word() -> None:
    for character in SECRET_WORD: 
        GUESS_WORD.append("-")
    print("Ok, length of word you need to guess:", LENGTH_WORD, "characters")
    print("You can enter only 1 letter from a-z\n\n")
    print_word_to_guess(GUESS_WORD)


def guessing() -> None:
    guess_taken = 1
    MAX_GUESS = 10
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Choose a letter\n").lower()
        if not guess in ALPHABET:
            print("Enter a letter from the ALPHABET")
        elif guess in letter_storage: 
            print("You have already used that letter!")
        else: 
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("Congratulation! You got it correctly!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '-' in GUESS_WORD:
                    print("WINNER!!!")
                    break
            else:
                print("Try Again!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 10:
                    print(" You lost! The secret word was {0}".format(SECRET_WORD))


if __name__ == "__main__":
    beginning()
    ask_user_to_play()
    prepare_secret_word()
    guessing()