class Graph:
    def __init__(self):
        self.graph = {}

    # Add a vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add an edge (undirected)
    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    # DFS using recursion
    def dfs(self, start):
        visited = set()

        def dfs_helper(node):
            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor in self.graph[node]:
                    dfs_helper(neighbor)

        dfs_helper(start)


# Create graph
g = Graph()

# Add vertices
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

# Add edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")

# DFS Traversal
print("DFS Traversal:")
g.dfs("A")