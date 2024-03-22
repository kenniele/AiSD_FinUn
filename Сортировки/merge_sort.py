def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0 # i — индекс левой части, j — индекс правой части, k — общий индекс
        while i < len(left) and j < len(right): # в этом цикле сравниваются два массива и "сливаются" в один
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        # Следующий кусок кода используется, если в массивах остались какие-либо неотсортированные элементы
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
