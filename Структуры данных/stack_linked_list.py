class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}\n{self.next if self.next is not None else ''}"


class Stack:
    def __init__(self, head):
        self.__head = head
        self.__size = 0

    def __str__(self):
        return f"Stack size: {self.__size} el.\n{self.__head}"

    def push(self, data):  # Вставка элемента в начало O(1)
        nd = Node(data, self.__head)
        self.__head = nd

    def pop(self):  # Удаление и возвращение элемента из начала O(1)
        if self.__size == 0:
            return
        item = self.__head
        self.__head = self.__head.next
        return item

    def peek(self):  # Просмотр верхнего элемента O(1)
        if self.__size == 0:
            return
        return self.__head.data

    def is_empty(self):  # Проверка, пустой ли стек O(1)
        return self.__size == 0

    def size(self):  # Получение размера стека O(1)
        return self.__size
