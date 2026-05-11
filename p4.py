import heapq

# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Heuristic Function
# Counts misplaced tiles
def heuristic(state):

    count = 0

    for i in range(3):
        for j in range(3):

            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


# Find blank space (0)
def find_blank(state):

    for i in range(3):
        for j in range(3):

            if state[i][j] == 0:
                return i, j


# Generate possible moves
def generate_moves(state):

    moves = []

    x, y = find_blank(state)

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dx, dy in directions:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            # Copy current state
            new_state = [row[:] for row in state]

            # Swap blank with neighbor
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            moves.append(new_state)

    return moves


# Print puzzle
def print_state(state):

    for row in state:
        print(row)

    print()


# A* Algorithm
def a_star(start):

    heap = []

    visited = []

    # f(n), state
    heapq.heappush(heap, (heuristic(start), start))

    while heap:

        f, current = heapq.heappop(heap)

        print("Current State:")
        print_state(current)

        # Goal Check
        if current == goal:

            print("Goal Reached!")
            return

        visited.append(current)

        # Generate next states
        for move in generate_moves(current):

            if move not in visited:

                h = heuristic(move)

                heapq.heappush(heap, (h, move))


# Initial State
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Run A*
a_star(start)