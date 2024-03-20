class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data  # Данные
        self.prev = prev  # Ссылка на предыдущий элемент двусвязного списка
        self.next = next  # Ссылка на следующий элемент двусвязного списка

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DLinkedList:  # Двусвязный список
    def __init__(self, head, tail):
        self.head = head  # Ссылка на начальный элемент двусвязного списка
        self.tail = tail  # Ссылка на конечный элемент двусвязного списка

    def __str__(self):
        return f"{self.head}"

    def push_back(self, data):  # Добавление элемента в конец списка O(1)
        nd = Node(data)
        self.tail.next = nd
        nd.prev = self.tail
        self.tail = nd

    def push_front(self, data):  # Добавление элемента в начало списка O(1)
        nd = Node(data)
        self.head.prev = nd
        nd.next = self.head
        self.head = nd

    def pop_back(self):  # Удаление элемента в конце списка O(1)
        nd = self.tail.prev
        nd.next = None
        self.tail = nd

    def pop_front(self):  # Удаление элемента в начале списка O(1)
        self.head = self.head.next
        self.head.prev = None

    def insert(self, index, data):  # Вставка элемента в любое место списка, кроме начала и конца O(n)
        i = 0
        nd = Node(data)
        previous, curr = None, self.head
        while i < index:
            previous, curr = curr, curr.next
            i += 1
        previous.next = nd
        nd.prev = previous
        curr.prev = nd
        nd.next = curr

    def erase(self, index):  # Удаление элемента в любом месте списка, кроме начала и конца O(n)
        i = 0
        previous, curr = None, self.head
        while i < index:
            previous, curr = curr, curr.next
            i += 1
        previous.next = curr.next
        curr.next.prev = previous

    def at(self, index):  # Доступ к элементу по индексу O(n)
        i = 0
        el = self.head
        while i < index:
            if el.next is None:
                break
            el = el.next
            i += 1
        return el
