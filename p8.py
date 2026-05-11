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





import heapq

def dijkstra(graph, start):

    distance = {}

    for node in graph:
        distance[node] = float('inf')

    distance[start] = 0

    heap = [(0, start)]

    while heap:

        current_distance, current_node = heapq.heappop(heap)

        for neighbor, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:

                distance[neighbor] = new_distance

                heapq.heappush(heap, (new_distance, neighbor))

    return distance


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

result = dijkstra(graph, 'A')

print(result)