class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data} -> {self.next}"


class Queue:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def enqueue(self, data):  # Добавляет элемент в конец очереди O(1)
        new_node = Node(data)
        self.tail.next = new_node

    def dequeue(self):  # Удаляет и возвращает элемент из начала очереди O(1)
        need = self.head
        if need:
            self.head = self.head.next
        return need

    def peek(self):  # Без удаления возвращает элемент из начала очереди O(1)
        return self.head

    def is_empty(self):  # Проверка, пустая ли очередь O(1)
        return self.head is None

    def size(self):  # Находит размер очереди O(n)
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
