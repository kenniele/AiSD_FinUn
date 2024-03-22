from random import randint


def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[randint(0, len(data) - 1)]
    left = [x for x in data if x < pivot]
    mid = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quicksort(left) + mid + quicksort(right)