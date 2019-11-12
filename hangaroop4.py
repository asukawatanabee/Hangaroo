#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 02:30:23 2019

@author: asukawatanabe
"""

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