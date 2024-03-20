from random import randint


def hoar_sort(data, fst, lst):
    if fst >= lst:
        return
    i, j = fst, lst
    pivot = data[randint(fst, lst)]
    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i, j = i + 1, j - 1
    hoar_sort(data, fst, j)
    hoar_sort(data, i, lst)
