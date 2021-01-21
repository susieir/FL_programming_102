""" Create binary search algorithm and test"""

from math import floor
from random import randint

#sorted_list = [1, 2, 3, 4, 5]

sorted_list2 = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9]

############################################################################################################
# Delivers left-most value
############################################################################################################

def binary_search_left(sorted_list, value):
    # Initialise left and right
    left = 0
    right = len(sorted_list) - 1
#    print("Left is {l} and right is {r}".format(l = left, r = right))
    # Create a loop that ends when left > right
    while left <= right:
        # Calculate the midpoint
        mid = floor((left + right) / 2)
        print("Midpoint is {m}, value is {v}".format(m=mid, v=value))
        if sorted_list[mid] > value:
            right = mid - 1
#            print("Left is {l} and right is {r}".format(l=left, r=right))
        elif sorted_list[mid] < value:
            left = mid + 1
#            print("Left is {l} and right is {r}".format(l=left, r=right))
        elif sorted_list[mid] == value:
            i = 0
            while sorted_list[mid - i] == sorted_list[mid - i - 1]:
#                print("Not first value, next value is in position {}".format(mid - i - 1))
                i += 1
            else:
                return "Left search - found in position {}".format(mid - i)

############################################################################################################
# Delivers right-most value
############################################################################################################

def binary_search_right(sorted_list, value):
    # Initialise left and right
    left = 0
    right = len(sorted_list) - 1
#    print("Left is {l} and right is {r}".format(l = left, r = right))
    # Create a loop that ends when left > right
    while left <= right:
        # Calculate the midpoint
        mid = floor((left + right) / 2)
#        print("Midpoint is {m}, value is {v}".format(m=mid, v=value))
        if sorted_list[mid] > value:
            right = mid - 1
#            print("Left is {l} and right is {r}".format(l=left, r=right))
        elif sorted_list[mid] < value:
            left = mid + 1
#            print("Left is {l} and right is {r}".format(l=left, r=right))
        elif sorted_list[mid] == value:
            i = 0
            while sorted_list[mid + i] == sorted_list[mid + i + 1]:
#                print("Not first value, next value is in position {}".format(mid + i + 1))
                i += 1
            else:
                return "Right search - found in position {}".format(mid + i)


print(binary_search_left(sorted_list2, 4))
print(binary_search_right(sorted_list2, 4))
