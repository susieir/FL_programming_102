""" Merge sort example"""
from timeit import timeit
from random import randint

# Generate random list
list_to_sort = [randint(0, 1000) for i in range(1000)]

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
    print("merged list is", list_c)
    return list_c


def merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    else:
        middle = len(unsorted) // 2
        front = unsorted[:middle]
        back = unsorted[middle:]
        print("splits are", front, back)
        front = merge_sort(front)
        back = merge_sort(back)
    return merge(front, back)


merge_sort(my_list)