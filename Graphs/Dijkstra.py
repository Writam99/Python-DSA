import heapq

class Node:
    def __init__(self, name):
        self.__name = name
        self.__distance = float("inf")
        self.__predecessor = None

    def getName(self):
        return self.__name

    def setDistance(self, distance):
        self.__distance = distance

    def getDistance(self):
        return self.__distance

    def setPredecessor(self, predecessor):
        self.__predecessor = predecessor

    def getPredecessor(self):
        return self.__predecessor

    def __lt__(self, other):
        return self.__distance < other.getDistance()

    def __gt__(self, other):
        return self.__distance > other.getDistance()

    def __eq__(self, other):
        return self.__distance == other.getDistance()

    def __hash__(self):
        return hash(self.__name)

    def __iter__(self):
        return self

class Edge:
    def __init__(self, src : Node, dest : Node, weight):
        self.__src = src
        self.__dest = dest
        self.__weight = weight

    def getSource(self):
        return self.__src

    def getDestination(self):
        return self.__dest

    def getWeight(self):
        return self.__weight

class Digraph:
    def __init__(self):
        self.edges = {}

    def addNode(self, node : Node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node] = []

    def addEdge(self, edge : Edge):
        src = edge.getSource()
        dest = edge.getDestination()
        weight = edge.getWeight()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, weight])

    def removeEdge(self, edge : Edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].remove(dest)

    def adjacentNodesOf(self, node : Node):
        return self.edges[node]

    def hasNode(self, node : Node):
        return node in self.edges

    def getNode(self, name):
        for node in self.edges:
            if node.getName() == name:
                return node
        raise NameError(name)

    def print_graph(self):
        for src in self.edges:
            src : Node
            print(src.getName(), ":", end=' ')
            for dest, weight in self.edges[src]:
                dest : Node
                print(dest.getName(), weight,  end=' ')
            print()

def buildGraph():
    g = Digraph()
    print("Enter the nodes. Type Done to stop.")
    inputList = [ele for ele in input().split()]
    for name in inputList:
        if name != 'Done':
            g.addNode(Node(name))
        else:
            break

    print("Enter source, destination and weight of edges. Type Done to stop.")
    s = input().split()
    while s[0] != 'Done':
        g.addEdge(Edge(g.getNode(s[0]), g.getNode(s[1]), int(s[2])))
        s = input().split()

    return g

def relax(source : Node, child : Node, weight):
    if child.getDistance() > source.getDistance() + weight:
        child.setDistance(source.getDistance() + weight)
        child.setPredecessor(source)

    if source.getName() == 's':
        print(child.getName(), child.getDistance())

def dijkstra(source):
    g = buildGraph()
    # g.print_graph()
    g : Digraph
    sourceNode = g.getNode(source)

    sourceNode : Node
    sourceNode.setDistance(0)

    verticesSet = set()
    verticesList = []

    for node in g.edges:
        heapq.heappush(verticesList, node)

    while len(verticesList) > 0:
        heapq.heapify(verticesList)
        minNode = heapq.heappop(verticesList)
        print("Printing min node", minNode.getName(), minNode.getDistance())
        verticesSet.add(minNode)

        for child in g.adjacentNodesOf(minNode):
            # print(child)
            relax(minNode, child[0], child[1])

    for vertex in verticesSet:
        vertex : Node
        if vertex.getName() != source:
            print(vertex.getName(), ":", vertex.getDistance(), vertex.getPredecessor().getName())

if __name__ == '__main__':
    dijkstra(input("Enter source: "))