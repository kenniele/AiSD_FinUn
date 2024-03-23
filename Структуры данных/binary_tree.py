class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"\nNode: {self.data}, left: {self.left}, right: {self.right}"


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return f"BinaryTree: {self.root}"

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
            return float("inf") # Если вершина пустая, то приравниваем наибольшее возможное значение
        return min(cur.data, self.min(cur.left), self.min(cur.right))  # Рекурсивно идем по ветвям

    def max(self, cur):  # Поиск максимума O(n)
        if cur is None:
            return float("-inf") # Если вершина пустая, то приравниваем наименьшее возможное значение
        return max(cur.data, self.max(cur.left), self.max(cur.right))  # Рекурсивно идем по ветвям

nd1 = Node(5)
nd2 = Node(10)
nd3 = Node(3)
nd4 = Node(4)
nd1.right = nd2
nd1.left = nd3
nd3.left = nd4
bin = BinaryTree(nd1)

print(bin.is_searching())
