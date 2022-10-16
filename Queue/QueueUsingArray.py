class Queue:

    def __init__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0

    def enqueue(self, data):
        self.__arr.append(data)
        self.__count += 1

    def dequeue(self):
        if self.__count == 0:
            print("Queue is empty")
            return
        element = self.__arr[self.__front]
        self.__front += 1
        self.__count -= 1
        return element

    def front(self):
        if self.__count == 0:
            print("Queue is empty")
            return
        element = self.__arr[self.__front]
        return element

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0