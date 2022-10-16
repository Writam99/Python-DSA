#My own advanced implementation
class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:

    def __init__(self):
        self.bucketSize = 20
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0

    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return (abs(hc) % (self.bucketSize))

    def insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]

        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()

    def rehash(self):
        temp = self.buckets
        self.bucketSize = 2 * self.bucketSize
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next

    def getLoadFactor(self):
        return self.count/self.bucketSize

    def get(self, key, defaultValue = None):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]

        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        return defaultValue

    def keys(self):
        key = []
        for head in self.buckets:
            while head is not None:
                key.append(head.key)
                head = head.next

        return key

    def values(self):
        value = []
        for head in self.buckets:
            while head is not None:
                value.append(head.value)
                head = head.next

        return value

    def items(self):
        item = []
        for head in self.buckets:
            while head is not None:
                item.append((head.key, head.value))
                head = head.next

        return item

    def remove(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None

        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1
                return head.value
            prev = head
            head = head.next

        return None

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.insert(key, value)

    def __iter__(self):
        return iter(self.keys())


# if __name__ == '__main__':
#     m = Map()
#
#     for i in range(1,11):
#         m[i] = i**2             #This is due to __setitem__()
#
#     for i in range(1,11):
#         print(m[i], end = ' ')  #This is due to __getitem__()
#
#     print()
#
#     for i in m:                 #This is due to __iter__()
#         print(i, end = ', ')