"""
title: strings
author: Zyden Walcher
date: 7/18/18
"""


def how_eligible(essay):
    """returns how many categories are in a string"""
    count = 0
    if '!' in essay:
        count += 1
    elif '"' in essay:
        count += 1




if __name__ == '__main__':
    print(how_eligible('this? "yes." no, not really!'))
    print(how_eligible('really, not a compound sentence.'))
