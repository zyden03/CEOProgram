"""
title: while loops
author: Zyden Walcher
date: 7/19/18 while loops
"""
import random


def goguess():
    """tell user if guess is out of range"""
    guess = input("I have a number between 1 and 20 inclusive")
    guess = int(guess)
    num_matches = 0
    answer = random.randint(1, 20)
    while guess != answer:
        guess = input("I have a number between 1 and 20 inclusive")
        guess = int(guess)
        if guess < answer:
            print( f"{guess} is lower than the answer.")
            num_matches += 1
        elif guess > answer:
            print( f"{guess} is higher than the answer")
            num_matches += 1
        else:
            return f"my number is {answer}, you guessed in {num_matches} guesses "


if __name__ == '__main__':
    print(goguess())