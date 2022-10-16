class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt

def getParent(v, parent):
    if v == parent[v]:
        return v
    return getParent(parent[v], parent)

def kruskal(edges, nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges, key = lambda edge : edge.wt)
    count = 0
    output = []
    i = 0
    while count < nVertices - 1:
        currentEdge = edges[i]
        srcParent = getParent(currentEdge.src, parent)
        destParent = getParent(currentEdge.dest, parent)

        if srcParent != destParent:
            output.append(currentEdge)
            count += 1
            parent[srcParent] = destParent
        i += 1

    return output

def main():
    n = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    print("Enter source, destination and weight: ")
    edges = []
    for i in range(E):
        curr_input = [int(ele) for ele in input().split()]
        src, dest, wt = curr_input
        edge = Edge(src, dest, wt)
        edges.append(edge)

    output = kruskal(edges, n)
    print("Output :")
    print("V1" + " " + "V2" + " " + "W")
    for edge in output:
        if edge.src < edge.dest:
            print(str(edge.src) + "  " + str(edge.dest) + "  " + str(edge.wt))
        else:
            print(str(edge.dest) + "  " + str(edge.src) + "  " + str(edge.wt))

if __name__ == '__main__':
    main()