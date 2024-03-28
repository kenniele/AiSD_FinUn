class Node:
    def __init__(self, name, to=None):
        if to is None:
            to = []
        self.name = name
        self.to = to

    def __str__(self):
        return f"{self.name}"


class Graph:
    def __init__(self):
        self.nodes = {}  # Набор вершин графа {вершина1: [ребенок1, ребенок2, ...], ...}

    def __str__(self):
        res = ""
        for node, to in self.nodes.items():
            res += f"{node.name}: {", ".join(map(lambda x: x.name, to))}\n"
        return res

    def make_by_dict(self, data):  # Функция для превращения словаря узлов (не связанных) в граф
        for parent, children in data.items():
            parent.to = children
            self.nodes[parent] = children

    def add_node(self, parent, node):  # Функция добавления узла графа O(1)
        pass

    def depth_first_search(self, start):
        visited, stack = [], [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(set(self.nodes[vertex.name]) - set(visited))
        return [vertex.name for vertex in visited]

    def breadth_first_search(self, start):
        visited, queue = [], [start]
        while queue:
            cur = queue.pop()
            if cur not in visited:
                visited.append(cur)
                queue = list(set(self.nodes[cur.name]) - set(visited)) + queue
        return [vertex.name for vertex in visited]

graph = Graph()
nd1 = Node("A")
nd2 = Node("B")
nd3 = Node("C")
nd4 = Node("D")
nd5 = Node("E")
nd6 = Node("F")
d = {nd1: [nd2, nd3],
     nd2: [nd1, nd4, nd5],
     nd3: [nd1, nd6],
     nd4: [nd2],
     nd5: [nd2, nd6],
     nd6: [nd3, nd5]}
graph.get_from_dict(d)
print(graph)
print(graph.depth_first_search(nd1))
print(graph.breadth_first_search(nd1))
