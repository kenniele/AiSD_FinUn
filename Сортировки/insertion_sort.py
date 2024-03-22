def insertion_sort(data):
    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and temp < data[j]: # пока слева есть элементы (j > 0) и данное число меньше предыдущего элемент
            data[j + 1] = data[j] # сдвигаем предыдущий элемент вправо
            j -= 1 # уменьшаем текущий индекс (для следующего сравнения с предпоследним элементом)
        data[j + 1] = temp
