class Node:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    # def __str__(self):
    #     return self.__name
    #
    # def __eq__(self, other):
    #     return self.getName() == other.getName()
    #
    # def __hash__(self):
    #     return hash(self.getName())

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

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.count = 0

    def addNode(self, node : Node):
        if node in self.nodes:
            raise ValueError('Duplicate Node')
        else:
            self.count += 1
            self.nodes[node] = self.count  #Making set

    def addEdge(self, edge : Edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges.append(edge)

    def getNode(self, name):
        for node in self.nodes:
            if node.getName() == name:
                return node
        raise NameError(name)

def buildGraph():
    g = Graph()
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

def kruskal():
    g = buildGraph()
    g : Graph
    result = []
    countVertices = 0
    edgeIndex = 0
    g.edges = sorted(g.edges, key= lambda edge : edge.getWeight())
    totalWeight = 0
    nodesReverse = {}
    for keys, values in g.nodes.items():
        nodesReverse[values] = []
        nodesReverse[values].append(keys)

    while countVertices < g.count - 1:
        currentEdge = g.edges[edgeIndex]
        currentEdge : Edge
        src = currentEdge.getSource()
        dst = currentEdge.getDestination()

        # print("Before:", src.getName(), g.nodes[src], dst.getName(), g.nodes[dst])
        if g.nodes[src] != g.nodes[dst]:
            result.append([src, dst, currentEdge.getWeight()])
            totalWeight += currentEdge.getWeight()
            # print("After:", src.getName(), g.nodes[src], dst.getName(), g.nodes[dst])
            countVertices += 1

            num1 = g.nodes[src]
            num2 = g.nodes[dst]
            print(len(nodesReverse[num1]), len(nodesReverse[num2]))

            if len(nodesReverse[num1]) >= len(nodesReverse[num2]):
                while len(nodesReverse[num2]) > 0:
                    item = nodesReverse[num2].pop()
                    g.nodes[item] = num1
                    nodesReverse[num1].append(item)
            else:
                while len(nodesReverse[num1]) > 0:
                    item = nodesReverse[num1].pop()
                    g.nodes[item] = num2
                    nodesReverse[num2].append(item)

        edgeIndex += 1


    print("MST:")
    for item in result:
        print(item[0].getName(), item[1].getName(), item[2])

    print("Total Weight:", totalWeight)

if __name__ == '__main__':
    kruskal()
