# Undirected Graph
class Node:
    def __init__(self, v):
        self.vertex = v
        self.next = None


class Graph:
    def __init__(self, size):
        self.__size = size  # Size is the number of vertices in the graph
        self.__adjList = [None] * size  # Adjacency List

    def add_edge(self, source, destination):
        node = Node(destination)
        node.next = self.__adjList[source]
        self.__adjList[source] = node

        node = Node(source)
        node.next = self.__adjList[destination]
        self.__adjList[destination] = node

    def remove_edge(self, source, destination):
        if source >= self.__size or destination >= self.__size:
            print("Check your vertices")
            return

        head = self.__adjList[source]
        prev = None
        while head is not None and head.vertex != destination:
            prev = head
            head = head.next

        if head is None:
            print("No edge between the vertices")
            return

        if prev is None:
            self.__adjList[source] = head.next
        else:
            prev.next = head.next

        head = self.__adjList[destination]
        prev = None
        while head is not None and head.vertex != source:
            prev = head
            head = head.next

        if prev is None:
            self.__adjList[destination] = head.next
        else:
            prev.next = head.next

    def print_graph(self):
        for i in range(self.__size):
            head = self.__adjList[i]
            print(i, ':', end=' ')
            while head is not None:
                print(head.vertex, end=' ')
                head = head.next
            print()


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.print_graph()
    print('------------')
    g.remove_edge(0, 2)
    g.remove_edge(0, 1)
    g.print_graph()

    g.remove_edge(0,4)
    g.remove_edge(0,1)