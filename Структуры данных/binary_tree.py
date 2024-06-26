class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f"\nNode: {self.data}, left: {self.left}, right: {self.right}"


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return f"BinaryTree: {self.root}"

    def append(self, nd, root=None):  # Функция добавления элемента (корректно только для дерева поиска) O(logn)
        if root is None:
            root = self.root
        curr = root
        if nd.data > curr.data:
            if curr.right is None:
                curr.right = nd
                curr.parent = nd
            else:
                self.append(nd, root=curr.right)
        else:
            if curr.left is None:
                curr.left = nd
                curr.parent = nd
            else:
                self.append(nd, root=curr.left)

    def search(self, val):  # Функция поиска элемента в бинарном дереве O(logn) -> O(n)
        cur = self.root
        while True:
            if cur is None:
                return False
            if val == cur.data:
                return True
            if val < cur.data:
                cur = cur.left
            else:
                cur = cur.right

    def breadth_first_search(self):  # Функция обхода дерева в ширину O(n)
        cur = self.root
        v = [cur]
        while len(v) > 0:
            vm = []
            for el in v:
                print(el.data)
                if el.left is not None:
                    vm.append(el.left)
                if el.right is not None:
                    vm.append(el.right)
            v = vm

    def depth_first_search(self, cur, style="lnr"):  # Функция обхода дерева в глубину O(n)
        #  style - стиль обхода дерева, l - left, r - right, n - node
        if cur is not None:
            if style == "lnr":
                self.depth_first_search(cur.left, "lnr")
                print(cur.data)
                self.depth_first_search(cur.right, "lnr")
            elif style == "rnl":
                self.depth_first_search(cur.right, "rnl")
                print(cur.data)
                self.depth_first_search(cur.left, "rnl")
            else:
                print(cur.data)
                self.depth_first_search(cur.left, "nlr")
                self.depth_first_search(cur.right, "nlr")

    def get_height(self, cur):  # Функция вызова глубины поддерева O(logn) -> O(n)
        if cur is not None:
            return 1 + max(self.get_height(cur.left), self.get_height(cur.right))
        else:
            return 0

    def is_balanced(self, cur):  # Проверка на сбалансированность дерева O(n)
        if cur is None:
            return True
        return self.is_balanced(cur.left) and self.is_balanced(cur.right) and \
            abs(self.get_height(cur.left) - self.get_height(cur.right)) <= 1

    def min(self, cur):  # Поиск минимума O(n)
        if cur is None:
            return float("inf")  # Если вершина пустая, то приравниваем наибольшее возможное значение
        return min(cur.data, self.min(cur.left), self.min(cur.right))  # Рекурсивно идем по ветвям

    def max(self, cur):  # Поиск максимума O(n)
        if cur is None:
            return float("-inf")  # Если вершина пустая, то приравниваем наименьшее возможное значение
        return max(cur.data, self.max(cur.left), self.max(cur.right))  # Рекурсивно идем по ветвям

    def is_search(self, cur):  # Проверяет, является ли бинарное дерево бинарным деревом поиска O(n)
        if cur is None:
            return True
        if (cur.left and cur.left.data >= cur.data) or (cur.right and cur.right.data <= cur.data):
            return False
        return self.is_search(cur.left) and self.is_search(cur.right)

    def max_depth(self):  # Показывает количество уровней O(n)
        return max(self.get_height(self.root.left), self.get_height(self.root.right)) + 1

    def sum(self):  # Сумма всех элементов бинарного дерева O(n)
        cur = self.root
        v = [cur]
        s = 0
        while len(v) > 0:
            vm = []
            for el in v:
                s += el.data
                if el.left is not None:
                    vm.append(el.left)
                if el.right is not None:
                    vm.append(el.right)
            v = vm
        return s


nd1 = Node(5)
nd2 = Node(7)
nd3 = Node(3)
nd4 = Node(1)
nd1.right = nd2
nd1.left = nd3
nd3.left = nd4
nd2.parent = nd1
nd3.parent = nd1
nd4.parent = nd3
bin = BinaryTree(nd1)

bin.append(Node(10))
print(bin.root.right)
