""" Merge sort example"""
from timeit import timeit
from random import randint

# Generate random list
list_to_sort = [randint(0,10000) for i in range(1000)]

############################################################################################
# BUBBLE SORT
############################################################################################

def BubbleSort(unsorted):
    """ A function that conducts a bubble sort on an unsorted list"""
    # Create a copy of the list
    list_copy = unsorted[:]

    # Initialise swapped variable
    swapped = True

    # Set up while loop that runs until swapped is False
    while swapped is True:
        swapped = False
        i = 0
        for i in range(len(list_copy) - 1):
            if list_copy[i] > list_copy[i + 1]:
                list_copy[i], list_copy[i + 1] = list_copy[i + 1], list_copy[i]
                swapped = True
    return list_copy

############################################################################################
# MERGE SORT
############################################################################################

def merge(list_a, list_b):
    list_c = []
    while len(list_a) > 0  and len(list_b) > 0:
        if list_a[0] < list_b[0]:
            list_c.append(list_a.pop(0))
        else:
            list_c.append(list_b.pop(0))
    if list_a == []:
        list_c += list_b
    else:
        list_c += list_a
#    print("merged list is", list_c)
    return list_c


def merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    else:
        middle = len(unsorted) // 2
        front = unsorted[:middle]
        back = unsorted[middle:]
#        print("splits are", front, back)
        front = merge_sort(front)
        back = merge_sort(back)
    return merge(front, back)

######################################################################


# Create anonymous functions to use with timeit
bs = lambda: BubbleSort(list_to_sort)
ms = lambda: merge_sort(list_to_sort)
ts = lambda: sorted(list_to_sort)

# Time the functions for 100 runs each
print("Merge took:")
print(timeit(ms, number = 100))

print("Bubble took:")
print(timeit(bs, number = 100))

print("Timesort took:")
print(timeit(ts, number=100))
