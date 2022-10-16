from Node import Node

class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, element):
        newNode = Node(element)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1

    def dequeue(self):
        if self.__head is None:
            print("Queue is Empty")
            return

        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data

    def front(self):
        if self.__head is None:
            print("Queue is Empty")
            return

        data = self.__head.data
        return data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0