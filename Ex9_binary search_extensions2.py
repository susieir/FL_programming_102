""" Create binary search algorithm and test"""

from math import floor
from random import randint

#sorted_list = [1, 2, 3, 4, 5]

sorted_list2 = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9]

def binary_search_closest(sorted_list, value):
    # Initialise left and right
    left = 0
    right = len(sorted_list) - 1
    print("Left is {l} and right is {r}".format(l = left, r = right))
    # Create a loop that ends when left > right, and the position of the value is returned
    while left <= right:
        # Calculate the midpoint
        mid = floor((left + right) / 2)
        print("Midpoint is {m}, value is {v}".format(m=mid, v=value))
        if sorted_list[mid] > value:
            right = mid - 1
            print("Left is {l} and right is {r}".format(l=left, r=right))
        elif sorted_list[mid] < value:
            left = mid + 1
            print("Left is {l} and right is {r}".format(l=left, r=right))
        elif sorted_list[mid] == value:
            return "Found in position {}".format(mid)
    print("Not found")

    # Reset algorithm
    left = 0
    right = len(sorted_list) - 1
    print("Left is {l} and right is {r}".format(l = left, r = right))


    # Create a loop the runs if the value is not found
    while left != right:
        # Calculate the midpoint
        mid = floor((left + right) / 2)
        print("Midpoint is {m}, value is {v}".format(m=mid, v=value))
        if sorted_list[mid] > value:
            right = mid - 1
            print("Left is {l} and right is {r}".format(l=left, r=right))
        elif sorted_list[mid] < value:
            left = mid + 1
            print("Left is {l} and right is {r}".format(l=left, r=right))
    else:
        print("No matching values")
        mid = left
        print("checking position {}".format(left))
        if sorted_list[mid] < value:
            if (abs(sorted_list[mid] - value) <= sorted_list[mid + 1] - value):
                return "The nearest value is {a} in position {b}".format(a = sorted_list[mid], b = mid)
            else:
                return "The nearest value is {a} in position {b}".format(a = sorted_list[mid + 1], b = mid + 1)
        else:
            if (abs(sorted_list[mid] - value) <= sorted_list[mid - 1] - value):
                return "The nearest value is {a} in position {b}".format(a = sorted_list[mid], b = mid)
            else:
                return "The nearest value is {a} in position {b}".format(a = sorted_list[mid - 1], b = mid - 1)


print(binary_search_closest(sorted_list2, 3.4))
