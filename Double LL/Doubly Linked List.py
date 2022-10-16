class Node:
    def __init__(self, info, prev = None, next = None):
        self.info = info
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insert_at_end(self, ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
            newNode.prev = current

    def delete_node(self, ele):
        # base case
        if self.head == None:
            print("List is empty")
            return

        # if only one node is present
        if self.head.next == None:
            if self.head.info == ele:
                temp = self.head
                self.head = None
                temp = None
                return
            else:
                print("Element is not found in list")
                return

        # delete head
        self.head = self.head.next
        self.head.prev = None
        return

        # delete node in between
        temp = self.head
        while temp.next != None:
            if temp.info == ele:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp = None
                return
            temp = temp.next

        # delete last node
        if temp.info == ele:
            temp.prev.next = None
            temp = None
            return
        print("Element is not found in the list")

    def reverse(self):
        if self.head == None:
            print("List is empty")
            return

        if self.head.next == None:
            return

        curr = self.head
        while curr != None:
            curr.prev, curr.next = curr.next, curr.prev
            self.head = curr
            curr = curr.prev
        return

    def display(self):
        if self.head == None:
            print("List is empty")
            return

        current = self.head
        while current != None:
            print(current.info)
            current = current.next

if __name__ == '__main__':
    dll = LinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(5)
    dll.display()

    print('-------------------------')
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    dll.display()

    print('------------------------')
    dll.delete_node(5)
    dll.display()

    print('------------------------')
    dll.reverse()
    dll.display()