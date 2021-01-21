""" Create binary search algorithm and test"""

from math import floor
from random import randint

sorted_list = [1, 2, 3, 4, 5]

sorted_list2 = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9]

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

print(binary_search(sorted_list2, 2))
