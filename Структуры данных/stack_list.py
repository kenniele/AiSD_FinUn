class Stack:
    def __init__(self, data):
        self.__data = data
        self.__size = len(data)

    def __str__(self):
        return f"Stack size: {self.__size} el.\n" + "\n".join(map(lambda x: str(x), self.__data))

    def push(self, data):  # Вставка элемента в начало O(n)
        self.__data.insert(0, data)
        self.__size += 1

    def pop(self):  # Удаление и возвращение элемента из начала O(n)
        if self.__size == 0:
            return
        self.__size -= 1
        return self.__data.pop(0)

    def peek(self):  # Просмотр верхнего элемента O(1)
        if self.__size == 0:
            return
        return self.__data[0]

    def is_empty(self):  # Проверка, пустой ли стек O(1)
        return self.__size == 0

    def size(self):  # Получение размера стека O(1)
        return self.__size