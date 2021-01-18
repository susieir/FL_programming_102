""" A function that simulates a pair of die being rolled n times and returns the number of occurrences of each score"""

import random
from collections import defaultdict

def single_roll(die=2):
    """ Simulates roll of n dice and returns n numbers from 1 to 6"""
    roll_outcome = []  # Initialise empty list
    for n in range(die):
        roll_outcome.append(random.randint(1,6))
    return roll_outcome


def roll_dice_n_times(n_rolls, die=2):
    """ Simulates n rolls of n dice and returns a list of outcomes"""
    all_outcomes = []  # Initialise empty list
    for n in range(n_rolls):
        all_outcomes.append(single_roll(die))
    return [val for sublist in all_outcomes for val in sublist]


def main(n_rolls, die=2):
    """ Takes a list of all outcomes and converts to a dictionary"""
    occurrence_dict = defaultdict(int)  # Initialise empty dict
    for roll in roll_dice_n_times(n_rolls, die):
        occurrence_dict[roll] += 1
    return occurrence_dict


if __name__ == '__main__':
    print(main(5))