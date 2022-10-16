def displayPath(solution, n):
    global calls
    calls += 1
    print("Path", calls, ":")
    for i in range(n):
        for j in range(n):
            print(solution[i][j], end=' ')
        print()
    print()
    return

def printPathHelper(x,y,maze,n,solution):
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        # print(solution)
        displayPath(solution, n)
        return

    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0 or solution[x][y] == 1:
        return

    solution[x][y] = 1
    printPathHelper(x + 1, y, maze, n, solution) #Down
    printPathHelper(x, y + 1, maze, n, solution) #Right
    printPathHelper(x - 1, y, maze, n, solution) #Top
    printPathHelper(x, y - 1, maze, n, solution) #Left
    solution[x][y] = 0
    return

def printPath(maze):
    n = len(maze)
    solution = [[0 for j in range(n)] for i in range(n)]
    printPathHelper(0,0,maze,n,solution)

if __name__ == '__main__':
    n = int(input("Enter n: "))
    maze = []
    for i in range(n):
        row = [int(ele) for ele in input("Enter row " + str(i+1) + ": ").split()]
        maze.append(row)

    calls = 0
    printPath(maze)

    if calls == 0:
        print("No Path")