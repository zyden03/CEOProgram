"""
title: data_types
author: Zyden Walcher
date: 7/18/18 data_types
"""


def add_tip(total, tip_percent):
    # return total amt including tip
    tip = tip_percent * total
    return total + tip


def age_calculator(current_year, birth_year):
    """returns user's age"""
    age = current_year - birth_year
    return age



def mean(a, b, c):
    """finding average of three numbers"""
    return (a + b + c) / 3

    if __name__ == "__main__":
        print(age_calculator(2018, 2003))
        print(mean(4, 7, 8))