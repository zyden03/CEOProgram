"""
title: branching
author: Zyden Walcher
date: 7/18/18 branching
"""


def food_order(choice, menu):
    choices = 'pizza', 'salad', 'sushi', 'fajitas', 'omelets'
    if choice in menu:
        return "your choice" + choice + "is on the menu. it will be out soon"
    else:
        return "your choice is not on the menu. "


def guess_number(low, high):
    """Tell user if guess is out of range"""
    guess = input("give a number between 1 and 80")
    guess = int(guess)
    if guess < low:
        return f"no, {guess} is less than {low}"
    elif guess > high:
        return f"no, {guess} is greater than {high}"
    else:
        return guess


if __name__ == '__main__':
   # menu = ['pizza', 'salad', 'sushi', 'fajitas', 'omelets']
   # choice = input("Enter your choice of entree: ")
   # print(food_order(choice, menu))
   print(guess_number(1, 80))





