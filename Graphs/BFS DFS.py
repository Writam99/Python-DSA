import queue

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


class Graph(Digraph):
    def addEdge(self, edge : Edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

    def removeEdge(self, edge : Edge):
        Digraph.removeEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.removeEdge(self, rev)


def buildGraph(graphType):
    g = graphType()
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

def BFS(g : Digraph, source):

    for vertex in g.edges:
        vertex : Node
        vertex.setColor('White')
        vertex.setDistance(0)

    sourceNode = g.getNode(source)
    sourceNode : Node
    sourceNode.setColor('Gray')

    q =queue.Queue()
    q.put(sourceNode)
    print("BFS Traversal: ")
    while not q.empty():
        curr = q.get()
        curr : Node
        print("Visiting", curr.getName())

        for child in g.adjacentNodesOf(curr):
            child : Node
            if child.getColor() == 'White':
                child.setColor('Gray')
                child.setDistance(curr.getDistance() + 1)
                child.setPredecessor(curr)
                q.put(child)
        curr.setColor('Black')
    print()
    print("Distances from source:")
    for node in g.edges:
        node : Node
        print(node.getName(), ":", node.getDistance())

def DFS(g : Digraph):
    for vertex in g.edges:
        vertex : Node
        vertex.setColor('White')

    time = [0]
    print("DFS Traversal:")
    for vertex in g.edges:
        vertex : Node
        if vertex.getColor() == 'White':
            DFS_Visit(g, vertex, time)

    print()
    print("Printing Vertex Name, Discovery Time, Finish Time of each vertex:")
    for node in g.edges:
        node : Node
        print(node.getName(), ":", node.getDiscoveryTime(), node.getFinishTIme())

def DFS_Visit(g : Digraph, curr : Node, time : list):
    time[0] += 1
    curr.setDiscoveryTime(time[0])
    curr.setColor('Gray')
    print(curr.getName())
    for child in g.adjacentNodesOf(curr):
        child : Node
        if child.getColor() == 'White':
            child.setPredecessor(curr)
            DFS_Visit(g, child, time)

    curr.setColor('Black')
    time[0] += 1
    curr.setFinishTime(time[0])



if __name__ == '__main__':
    s = eval(input("Enter Digraph for directed graph or Graph for undirected graph: "))

    g = buildGraph(s)
    # BFS(g, input("Enter source: "))
    # print()

    DFS(g)

    # print("Printing graph:")
    # g.print_graph()

    # print('-------------------')
    #
    # g.removeEdge(Edge(g.getNode('0'), g.getNode('2')))
    # g.removeEdge(Edge(g.getNode('0'), g.getNode('1')))
    # g.print_graph()
    #
    # g.removeEdge(Edge(g.getNode('0'), g.getNode('4')))

