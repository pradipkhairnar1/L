import heapq

N = 4

# Function to count attacking queens
def heuristic(board):

    attacks = 0

    for i in range(len(board)):
        for j in range(i + 1, len(board)):

            # Same column
            if board[i] == board[j]:
                attacks += 1

            # Same diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
                
    return attacks


# A* Algorithm
def a_star():

    # Priority queue
    open_list = []

    # Start with empty board
    start = []

    # Add first state
    heapq.heappush(open_list, (0, start))

    while open_list: 
        # Get state with minimum cost
        cost, board = heapq.heappop(open_list)

        # If 4 queens placed
        if len(board) == N:

            # Check solution
            if heuristic(board) == 0:
                return board

        # Next row to place queen
        row = len(board)

        # Try all columns
        for col in range(N):

            # Create new board
            new_board = board + [col]

            # g(n) = queens placed
            g = len(new_board)

            # h(n) = attacking queens
            h = heuristic(new_board)

            # f(n) = g(n) + h(n)
            f = g + h

            # Add to priority queue
            heapq.heappush(open_list, (f, new_board))


# Function to print chessboard
def print_board(board):

    for row in range(N):

        for col in range(N):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# Main
solution = a_star()

print("Solution:", solution)

print("\nChess Board:\n")

print_board(solution)