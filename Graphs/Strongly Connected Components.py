class Node:
    def __init__(self, name):
        self.__name = name
        self.__color = None
        self.__distance = None
        self.__predecessor = None
        self.__discoveryTime = None
        self.__finishTime = None

    def getName(self):
        return self.__name

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setDistance(self, distance):
        self.__distance = distance

    def getDistance(self):
        return self.__distance

    def setPredecessor(self, predecessor):
        self.__predecessor = predecessor

    def getPredecessor(self):
        return self.__predecessor

    def setDiscoveryTime(self, time):
        self.__discoveryTime = time

    def getDiscoveryTime(self):
        return self.__discoveryTime

    def setFinishTime(self, time):
        self.__finishTime = time

    def getFinishTIme(self):
        return self.__finishTime


class Edge:
    def __init__(self, src : Node, dest : Node):
        """Assumes src and dest are nodes"""
        self.__src = src
        self.__dest = dest

    def getSource(self):
        return self.__src

    def getDestination(self):
        return self.__dest

    def __str__(self):
        return self.__src.getName() + '->' + self.dest.getName()

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
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

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
            for dest in self.edges[src]:
                dest : Node
                print(dest.getName(), end=' ')
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

    print("Enter source and destination of edges. Type Done to stop.")
    s = input().split()
    while s[0] != 'Done':
        g.addEdge(Edge(g.getNode(s[0]), g.getNode(s[1])))
        s = input().split()

    return g

def buildTransposeGraph(g : Digraph):
    gT = Digraph()

    for vertice in g.edges:
        vertice : Node
        gT.addNode(Node(vertice.getName()))

    for vertice in g.edges:
        vertice : Node
        for child in g.adjacentNodesOf(vertice):
            child : Node
            gT.addEdge(Edge(gT.getNode(child.getName()), gT.getNode(vertice.getName())))

    return gT

def stronglyConnected(g : Digraph):
    gT = buildTransposeGraph(g)
    DFS(g)
    timestamp = {}
    for vertice in g.edges:
        vertice: Node
        timestamp[vertice.getFinishTIme()] = gT.getNode(vertice.getName())

    print("Printing connected components:")
    timestamp = sorted(timestamp.items(), reverse=True)
    # print(timestamp)
    # for i in timestamp:
    #     print(i[1].getName())
    DFS(gT, timestamp)


def DFS(g : Digraph, order = None):
    for vertex in g.edges:
        vertex : Node
        vertex.setColor('White')

    time = [0]
    print("DFS Traversal:")
    if order is None:
        for vertex in g.edges:
            vertex : Node
            if vertex.getColor() == 'White':
                DFS_Visit(g, vertex, time)
                print()
    else:
        for vertex in order:
            if vertex[1].getColor() == 'White':
                DFS_Visit(g, vertex[1], time)
                print()

    # print()
    # print("Printing Vertex Name, Discovery Time, Finish Time of each vertex:")
    # for node in g.edges:
    #     node : Node
    #     print(node.getName(), ":", node.getDiscoveryTime(), node.getFinishTIme())

def DFS_Visit(g : Digraph, curr : Node, time : list):
    time[0] += 1
    curr.setDiscoveryTime(time[0])
    curr.setColor('Gray')
    print(curr.getName(), end=' ')
    for child in g.adjacentNodesOf(curr):
        child : Node
        if child.getColor() == 'White':
            child.setPredecessor(curr)
            DFS_Visit(g, child, time)

    curr.setColor('Black')
    time[0] += 1
    curr.setFinishTime(time[0])

if __name__ == '__main__':
    g = buildGraph()
    g.print_graph()
    # print()

    # print("Printing DFS of g:")
    # DFS(g)

    stronglyConnected(g)