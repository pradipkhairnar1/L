import heapq


def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]

print("Original Array:", arr)

selection_sort(arr)

print("Sorted Array:", arr)




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