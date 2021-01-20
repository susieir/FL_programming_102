
my_list = [5, 9, 5, 8, 1, 3]

def BubbleSort(unsorted):
    """ A function that conducts a bubble sort on an unsorted list"""
    # Create a copy of the list
    list_copy = my_list[:]

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


print(BubbleSort(my_list))