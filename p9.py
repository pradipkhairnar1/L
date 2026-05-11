def solve_n_queens_branch_bound(n):
    solutions = []
    board = [-1] * n

    cols = [False] * n
    diag1 = [False] * (2 * n - 1)   # row + col
    diag2 = [False] * (2 * n - 1)   # row - col + n - 1

    def solve(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:

                # Place queen
                board[row] = col
                cols[col] = True
                diag1[row + col] = True
                diag2[row - col + n - 1] = True

                solve(row + 1)

                # Backtrack
                board[row] = -1
                cols[col] = False
                diag1[row + col] = False
                diag2[row - col + n - 1] = False

    solve(0)
    return solutions


def print_board(solution, n):

    for row in range(n):

        for col in range(n):

            if solution[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

    print()


# Main Program
n = 4

solutions = solve_n_queens_branch_bound(n)

print("Solutions:\n")

for sol in solutions:

    print(sol)

    print_board(sol, n)