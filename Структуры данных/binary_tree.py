class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def search(self, val):
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


nd1 = Node(5)
nd2 = Node(10)
nd3 = Node(3)
nd4 = Node(1)
nd1.right = nd2
nd1.left = nd3
nd3.left = nd4
bin = BinaryTree(nd1)

print(bin.search(10))