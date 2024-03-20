class Node: # Элемент односвязного списка
    def __init__(self, data, next=None):
        self.data = data # Данные
        self.next = next # Ссылка на следующий элемент односвязного списка

    def __str__(self):
        return f"{self.data} -> {self.next}"


class LinkedList: # Односвязный список
    def __init__(self, head, tail):
        self.head = head # Ссылка на начало списка типа Node
        self.tail = tail # Ссылка на конец списка типа Node

    def __str__(self):
        return f"{self.head}"

    def push_back(self, data): # Добавление элемента в конец списка O(1)
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def push_front(self, data): # Добавление элемента в начало списка O(1)
        nd = Node(data)
        nd.next, self.head = self.head, nd

    def pop_back(self): # Удаление элемента из конца списка O(n)
        prev, curr = self.head, self.head.next
        while curr.next:
            prev, curr = curr, curr.next
        self.tail = prev
        prev.next = None

    def pop_front(self): # Удаление элемента из начала списка O(1)
        self.head = self.head.next

    def insert(self, index, data): # Вставка элемента в любое место списка, кроме начала и конца O(n)
        i = 0
        prev, curr = None, self.head
        while i < index:
            prev, curr = curr, curr.next
            i += 1
        nd = Node(data)
        prev.next = nd
        nd.next = curr

    def erase(self, index): # Удаление элемента из любого места списка, кроме начала и конца O(n)
        i = 0
        prev, curr = None, self.head
        while i < index:
            prev, curr = curr, curr.next
            i += 1
        prev.next = curr.next