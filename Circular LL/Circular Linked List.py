# Singly Circular Linked List
class Node:
    def __init__(self, info, next = None):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
            self.head = newNode

    def insert_at_end(self, ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head

    def delete_node(self, ele):
        if self.head == None:
            print("List is empty")
            return

        # deleting head
        if self.head.info == ele:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        # deleting node in between
        current = self.head
        while current.next != self.head:
            if current.next.info == ele:
                temp = current.next
                current.next = temp.next
                temp = None
                return
            current = current.next

        print("Element not found in the list")

    def reverse(self):
        if self.head == None:
            print("List is empty")
            return

        if self.head.next == None:
            return

        curr = self.head
        prev = None

        while curr.next != self.head:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        curr.next = prev
        self.head.next = curr
        self.head = curr
        return

    def traverse(self):
        current = self.head
        while current.next != self.head:
            print(current.info, end=' ')
            current = current.next
        print(current.info)

if __name__ == '__main__':
    cll = LinkedList()
    cll.insert_at_beginning(10)
    cll.insert_at_beginning(5)
    cll.traverse()
    print('------------------')

    cll.insert_at_end(20)
    cll.insert_at_end(30)
    cll.insert_at_end(40)
    cll.traverse()
    print('------------------')

    cll.delete_node(200)
    cll.traverse()
    print('--------------------')

    cll.reverse()
    cll.traverse()