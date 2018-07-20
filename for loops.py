"""
title: for loops
author: Zyden Walcher
date: 7/19/18 for loops
"""


def find_matches(secret, guesses):
    num_matches = 0
    for i in range(5):
        if int(secret[i]) == int(guesses[i]):
            num_matches += 1



def short_hand(phrase):
    phrase = phrase.replace("For", "4")
    phrase = phrase.replace("Too", "2")
    phrase = phrase.replace("And", "&")
    phrase = phrase.replace("You", "U")


    phrase = phrase.replace("a", "")
    phrase = phrase.replace("e", "")
    phrase = phrase.replace("i", "")
    phrase = phrase.replace("o", "")
    phrase = phrase.replace("u", "")
    phrase = phrase.replace("A", "")
    phrase = phrase.replace("E", "")
    phrase = phrase.replace("I", "")
    phrase = phrase.replace("O", "")
    phrase = phrase.replace("U", "")

if __name__ == '__main__':
    print(short_hand("thank you for that! You are too sweet and kind!"))








