""" Linear search"""

from random import randint

list_to_be_searched = [randint(0, 10000) for _ in range(0, 1000)]

find_value = 5


def linear_search(sequence, search_item):
    """ Function that iterates through a sequence to find an item"""
    # Initialise 'found' flag
    found = False
    # Iterate through items in list
    for position, item in enumerate(sequence):
        # Check if item equals search_item
        if item == search_item:
            found = True
            return position
    # If, after iterating through the list, found is still set to false, return a statement
    if found == False:
        return "Value not found"

print(linear_search(list_to_be_searched, find_value))


