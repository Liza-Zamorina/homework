def create_adjacency_matrix(V, G):
    adjacency_matrix = []

    for i in range(0, V):
        adjacency_matrix.append([])
        for j in range(0, V):
            adjacency_matrix[i].append(0)
    for i in range(0, len(G)):
        adjacency_matrix[G[i][0]][G[i][1]] = G[i][2]
        adjacency_matrix[G[i][1]][G[i][0]] = G[i][2]

    return adjacency_matrix


def prims_algo(V, G):
    adjacency_matrix = create_adjacency_matrix(V, G)

    vertex = 0

    MST = []
    edges = []
    visited = []
    min_edge = [None, None, float('inf')]

    while len(MST) != V - 1:

        visited.append(vertex)

        for r in range(0, V):
            if adjacency_matrix[vertex][r] != 0:
                edges.append([vertex, r, adjacency_matrix[vertex][r]])

        for e in range(0, len(edges)):
            if edges[e][2] < min_edge[2] and edges[e][1] not in visited:
                min_edge = edges[e]

        edges.remove(min_edge)

        MST.append(min_edge)

        vertex = min_edge[1]
        min_edge = [None, None, float('inf')]

    return MST



a=0
b=1
c=2
d=3
e=4
f=5
g=6
h=7

#  ребра с весом
graph = [
    [a, e, 3],
    [a, b, 6],
    [a, d, 5],
    [d, e, 6],
    [d, g, 5],
    [e, g, 8],
    [e, h, 4],
    [b, f, 2],
    [b, c, 5],
    [c, f, 5],
    [c, h, 9],
    [f, h, 3],
    [g, h, 1]
]

print(prims_algo(8, graph))


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot


        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):

        result = []

        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [];
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("метод Краскаля ")
        print("ребро \t вес")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))

a=0
b=1
c=2
d=3
e=4
f=5
g=6
h=7
# выполняемый код
g = Graph(8)
g.addEdge(0, 4, 3)
g.addEdge(0, 1, 6)
g.addEdge(0, 3, 5)
g.addEdge(3, 4, 6)
g.addEdge(3, 6, 5)
g.addEdge(4, 6, 8)
g.addEdge(4, 7, 4)
g.addEdge(1, 5, 2)
g.addEdge(1, 2, 5)
g.addEdge(2, 5, 5)
g.addEdge(2, 7, 9)
g.addEdge(5, 7, 3)
g.addEdge(6, 7, 1)

g.KruskalMST()