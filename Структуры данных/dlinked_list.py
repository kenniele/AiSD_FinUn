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

    def info(self): # Выводит информацию о списке
        curr = self.head
        while curr is not None:
            print(f"Значение - {curr.data}\n"
                  f"{curr.prev.data if curr.prev else None} -> X -> "
                  f"{curr.next.data if curr.next else None}\n")
            curr = curr.next

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

    def __reversed__(self):  # Разворот списка O(n)
        self.head, self.tail = self.tail, self.head
        curr = self.head
        while True:
            curr.next, curr.prev = curr.prev, curr.next
            if curr.next is None:
                break
            curr = curr.next

    def join(self, other):  # Слияние двусвязных списков O(n + m)
        if isinstance(other, DLinkedList):
            if self.head.data < other.head.data:
                temp_head = self.head
                c1, c2 = self.head.next, other.head
            else:
                temp_head = other.head
                c1, c2 = self.head, other.head.next
            c = temp_head
            while c1 is not None and c2 is not None:
                if c1.data < c2.data:
                    c.next = c1
                    c1 = c1.next
                else:
                    c.next = c2
                    c2 = c2.next
                c.next.prev = c
                c = c.next
            while c1 is not None:
                c.next = c1
                c1 = c1.next
                c.next.prev = c
            while c2 is not None:
                c.next = c2
                c2 = c2.next
                c.next.prev = c
        return NotImplemented

    def is_palindrome(self):  # Проверка, является ли палиндромом O(n)
        c1, c2 = self.head, self.tail
        while True:
            if c1.data != c2.data:
                return False
            if c1.next is None:
                return True
            c1, c2 = c1.next, c2.prev

    def unique(self): # Убирает повторения в списке O(n)
        c, n = self.head, self.head.next
        d = {c.data: 1}
        while n is not None:
            item = d.get(n.data, None)
            if item is None:
                d[n.data] = 1
                c, n = n, n.next
            else:
                n = n.next
                c.next = n
                n.prev = c
        self.tail = c

    def get_middle(self): # Средний элемент O(n)
        c1, c2 = self.head, self.tail
        while c1 is not None:
            if c1 is c2:
                return c1.data
            elif c1.next is c2 and c2.prev is c1:
                return c1.data, c2.data
            c1, c2 = c1.next, c2.prev
