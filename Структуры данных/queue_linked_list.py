class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data} -> {self.next}"


class Queue:
    def __init__(self, head, tail):
        self.__head = head
        self.__tail = tail
        self.__size = 0

    def enqueue(self, data):  # Добавляет элемент в конец очереди O(1)
        new_node = Node(data)
        self.__tail.next = new_node
        self.__size += 1

    def dequeue(self):  # Удаляет и возвращает элемент из начала очереди O(1)
        item = self.__head
        if item:
            self.__head = self.__head.next
            self.__size -= 1
        return item

    def peek(self):  # Без удаления возвращает элемент из начала очереди O(1)
        return self.__head.data

    def is_empty(self):  # Проверка, пустая ли очередь O(1)
        return self.__size == 0

    def size(self):  # Находит размер очереди O(1)
        return self.__size
