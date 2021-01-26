### Timing searches

# For linear and binary search

# 1. Small list
# 2. Large list
# 3. Not in list
# 4. Last in list

from timeit import timeit
from random import randint
from math import floor

list_to_search = [i for i in range(1000)]

########################################################################################################################
# Binary search
########################################################################################################################

def binary_search(sorted_list, value):
    # Initialise left and right
    left = 0
    right = len(sorted_list) - 1
    # Create a loop that ends when left > right
    while left <= right:
        # Calculate the midpoint
        mid = floor((left + right) / 2)
        if sorted_list[mid] > value:
            right = mid - 1
        elif sorted_list[mid] < value:
            left = mid + 1
        elif sorted_list[mid] == value:
            return "Found in position {}".format(mid)
    return False

########################################################################################################################
# Linear search
########################################################################################################################

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

########################################################################################################################
# Time it
########################################################################################################################

ls = lambda: linear_search(list_to_search, 10000)
bs = lambda: binary_search(list_to_search, 10000)

# time the functions for 100 runs each
print("Linear search took:")
print(timeit(ls, number=100))
print("Binary search took:")
print(timeit(bs, number=100))