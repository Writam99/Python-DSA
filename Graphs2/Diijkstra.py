import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2, distance):
        self.adjMatrix[v1][v2] = distance
        self.adjMatrix[v2][v1] = distance

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

    def __getMinVertex(self, visited, distance):
        min_vertex = -1
        for i in range(self.nVertices):
            if visited[i] is False and (min_vertex == -1 or distance[min_vertex] > distance[i]):
                min_vertex = i
        return min_vertex

    def diijkstra(self):
        visited = [False for i in range(self.nVertices)]
        distance = [float("inf") for i in range(self.nVertices)]
        distance[0] = 0

        for i in range(self.nVertices - 1):
            min_vertex = self.__getMinVertex(visited, distance)
            visited[min_vertex] = True

            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j] > 0 and visited[j] is False:
                    curr_distance = distance[min_vertex] + self.adjMatrix[min_vertex][j]
                    if curr_distance < distance[j]:
                        distance[j] = curr_distance


        #Outputting
        for vertex, dist in enumerate(distance):
            print(vertex, dist)

def main():
    n = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    g = Graph(n)
    print("Enter source, destination and weight: ")
    for i in range(E):
        curr_input = [int(ele) for ele in input().split()]
        g.addEdge(curr_input[0], curr_input[1], curr_input[2])

    g.diijkstra()

if __name__ == '__main__':
    main()
