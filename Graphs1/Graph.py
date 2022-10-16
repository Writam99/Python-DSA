import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i, visited)

    def __bfsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            curr = q.get()
            print(curr)
            for i in range(self.nVertices):
                if self.adjMatrix[curr][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i, visited)

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)

    def __hasPathHelper(self, sv, tv, visited):
        visited[sv] = True
        if self.adjMatrix[sv][tv] > 0:
            return True
        foundPath = False # make it False by default to deal with vertices with no edges going out of them
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                foundPath = self.__hasPathHelper(i, tv, visited)
                if foundPath:
                    return foundPath

        return foundPath

    def hasPath(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        visited = [False for i in range(self.nVertices)]
        return  self.__hasPathHelper(v1,v2, visited)

    def __getPathDFSHelper(self, sv, tv, visited):
        visited[sv] = True
        if self.adjMatrix[sv][tv] > 0:
            return [tv, sv]

        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                path = self.__getPathDFSHelper(i, tv, visited)
                if path is not None:
                    path.append(sv)
                    return path
        return None

    def getPathDFS(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        path = self.__getPathDFSHelper(v1, v2, visited)
        if path is not None:
            for i in path:
                print(i, end = ' ')
            print()
        return ' '

    def __getPathBFSHelper(self, sv, ev, visited):
        q = queue.Queue()
        parent = {}
        q.put(sv)
        visited[sv] = True
        found = False
        while q.empty() is False and found is False:
            curr = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[curr][i] > 0 and visited[i] is False:
                    q.put(i)
                    parent[i] = curr
                    visited[i] = True
                    if i == ev:
                        found = True
                        break

        path = [ev]
        parentV = ev
        while parentV != sv:
            parentV = parent[parentV]
            path.append(parentV)
        return path

    def getPathBFS(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        path = self.__getPathBFSHelper(v1, v2, visited)
        if path is not None:
            for i in path:
                print(i, end=' ')
            print()
        return ' '

    def isConnected(self):
        visited = []
        q = queue.Queue()
        q.put(0)
        visited.append(0)
        while q.empty() is False:
            curr = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[curr][i] > 0 and i not in visited:
                    q.put(i)
                    visited.append(i)

        if len(visited) == self.nVertices:
            return True
        return False

    def __allComponentHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        components = [sv]
        while q.empty() is False:
            curr = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[curr][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
                    components.append(i)
        return components

    def allComponent(self):
        visited = [False for i in range(self.nVertices)]
        ans = []
        for i in range(self.nVertices):
            if visited[i] is False:
                ans.append(self.__allComponentHelper(i, visited))

        return ans

if __name__ == '__main__':
    g = Graph(7)
    g.addEdge(0,1)
    g.addEdge(0,3)
    g.addEdge(2,4)
    g.addEdge(2,5)
    g.addEdge(4,6)
    # g.addEdge(3, 4)
    # g.dfs()
    # print('-------------')
    # g.bfs()
    #
    # print(g.hasPath(0,6))
    # print(g.getPathDFS(0,6))
    #
    # print(g.hasPath(0, 5))
    # print(g.getPathDFS(0, 5))
    #
    # g1 = Graph(6)
    # g1.addEdge(0, 1)
    # g1.addEdge(0, 2)
    # g1.addEdge(0, 3)
    # g1.addEdge(2, 4)
    # g1.addEdge(4, 5)
    # g1.addEdge(3, 5)

    # print("DFS:")
    # g1.dfs()
    # print("BFS:")
    # g1.bfs()
    # print("Getting path DFS:")
    # g1.getPathDFS(0, 5)
    # print("Getting path BFS:")
    # g1.getPathBFS(0, 5)

    print(g.isConnected())
    print(g.allComponent())