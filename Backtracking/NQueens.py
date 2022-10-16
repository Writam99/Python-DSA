def displayBoard(board, n):
    global calls
    calls += 1
    print("Possibility", calls, ":")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print()
    return

def isSafe(row, col, board, n):
    #vertical direction
    i = row - 1
    while i >= 0:
        if board[i][col] == 1:
            return False
        i -= 1

    #upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    #upper right diagonal
    i = row -1
    j = col + 1
    while i>= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def printPathHelper(row, n, board):
    if row == n:
        # for i in range(n):
        #     for j in range(n):
        #         print(board[i][j], end = ' ')
        # print()
        displayBoard(board, n)
        return

    for col in range(n):
        if isSafe(row, col, board, n):
            board[row][col] = 1
            printPathHelper(row + 1, n, board)
            board[row][col] = 0

    return

def printPath(n):
    board = [[0 for j in range(n)] for i in range(n)]
    printPathHelper(0, n, board)

if __name__ == '__main__':
    n = int(input("Enter n: "))
    calls = 0
    printPath(n)