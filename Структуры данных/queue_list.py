class Queue:
    def __init__(self, data=None, max_size=None):
        if data is None:
            data = []
        self.data = data
        self.max_size = max_size
        self.size = len(self.data)

    def __str__(self):
        return " -> ".join(map(lambda x: str(x), self.data))

    def enqueue(self, data):  # Добавляет элемент в конец очереди от O(1) до O(n)
        while self.size == self.max_size:
            self.data.pop(0)
            self.size -= 1
        self.data.append(data)
        self.size += 1

    def dequeue(self):  # Удаляет и возвращает элемент из начала очереди O(n)
        if self.size == 0:
            return
        self.size -= 1
        return self.data.pop(0)

    def peek(self):  # Без удаления возвращает элемент из начала очереди O(1)
        if self.size == 0:
            return
        return self.data[0]

    def is_empty(self):  # Проверка, пустая ли очередь O(1)
        return self.size == 0

    def size(self):  # Находит размер очереди O(1)
        return self.size
