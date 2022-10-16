import sys
import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt

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

    def __getMinVertex(self, visited, weight):
        min_vertex = -1
        for i in range(self.nVertices):
            if visited[i] is False and (min_vertex == -1 or weight[min_vertex] > weight[i]):
                min_vertex = i
        return min_vertex

    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        weight[0] = 0

        for i in range(self.nVertices - 1):
            min_vertex = self.__getMinVertex(visited, weight)
            visited[min_vertex] = True

            #Explore the neighbours of minVertex which is not visted and update
            #the weight corresponding to them if required

            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j] > 0 and visited[j] is False:
                    if weight[j] > self.adjMatrix[min_vertex][j]:
                        weight[j] = self.adjMatrix[min_vertex][j]
                        parent[j] = min_vertex

        #Ouuput
        print("Output :")
        print("V1" + " " + "V2" + " " + "W")
        for i in range(1, self.nVertices):
            if i < parent[i]:
                print(str(i) + "  " + str(parent[i]) + "  " + str(weight[i]))
            else:
                print(str(parent[i]) + "  " + str(i) + "  " + str(weight[i]))

def main():
    n = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    g = Graph(n)
    print("Enter source, destination and weight: ")
    for i in range(E):
        curr_input = [int(ele) for ele in input().split()]
        g.addEdge(curr_input[0], curr_input[1], curr_input[2])

    g.prims()

if __name__ == '__main__':
    main()