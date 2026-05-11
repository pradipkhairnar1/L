import heapq

def prims(graph, start):

    visited = set()

    # (weight, current_node, parent)
    min_heap = [(0, start, None)]

    mst = []
    total_cost = 0

    while min_heap:

        weight, current, parent = heapq.heappop(min_heap)

        # Skip if already visited
        if current in visited:
            continue

        # Mark node as visited
        visited.add(current)

        # Add edge to MST
        if parent is not None:
            mst.append((parent, current, weight))
            total_cost += weight

        # Push neighbors into heap
        for neighbor, w in graph[current]:

            if neighbor not in visited:
                heapq.heappush(
                    min_heap,
                    (w, neighbor, current)
                )

    return mst, total_cost


# Graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

mst, cost = prims(graph, 'A')

print("Minimum Spanning Tree:")

for u, v, w in mst:
    print(u, "--", v, "=", w)

print("Total Cost =", cost)







# Find parent of node
def find(parent, node):

    if parent[node] != node:
        parent[node] = find(parent, parent[node])

    return parent[node]


# Union of two sets
def union(parent, rank, u, v):

    root_u = find(parent, u)
    root_v = find(parent, v)

    # Cycle check
    if root_u == root_v:
        return False

    # Union by rank
    if rank[root_u] > rank[root_v]:
        parent[root_v] = root_u

    elif rank[root_u] < rank[root_v]:
        parent[root_u] = root_v

    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


def kruskal(vertices, edges):

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}

    # Make separate set for each vertex
    for vertex in vertices:
        parent[vertex] = vertex
        rank[vertex] = 0

    mst = []
    total_cost = 0

    # Process edges
    for u, v, weight in edges:

        # Add edge if no cycle
        if union(parent, rank, u, v):

            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# Vertices
vertices = ['A', 'B', 'C', 'D']

# Edges
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 1),
    ('C', 'D', 4)
]

mst, cost = kruskal(vertices, edges)

print("Minimum Spanning Tree:")

for u, v, w in mst:
    print(u, "--", v, "=", w)

print("Total Cost =", cost)