class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def insertAtIR(head, i, data):
    if i < 0:
        return head

    if i==0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    if head is None:
        return None

    smallHead = insertAtIR(head.next, i - 1, data)
    head.next = smallHead
    return head

def insertAtI(head, i, data):
    if i < 0 or i > length(head):
        return head

    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode

    newNode.next = curr
    return head

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for currData in inputList:
        if currData == -1:
            break

        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def printNode(head, i):
    count = 0
    while count < i and head != None:
        count += 1
        head = head.next

    if head is None or i < 0:
        print("Node not found")
    else:
        print(head.data)

def deleteNodeIR(head, i):
    if i < 0:
        print("Node not found. Index out of bounds")
        return head

    if head is None:
        print("Node not found. Could not delete node")
        return None

    if i == 0:
        newHead = head.next
        del(head)
        return newHead

    smallHead = deleteNodeIR(head.next, i - 1)
    head.next = smallHead
    return head


def deleteNodeI(head, i):
    if i < 0 or i >= length(head):
        print("Node not found. Could not delete node")
        return head

    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    if prev is not None:
        prev.next = curr.next
    else:
        head = curr.next

    del(curr)
    return head

def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end = '')
        head = head.next

    print("None")
    return

if __name__ == '__main__':

    head = takeInput()
    printLL(head)
    print(length(head))
    print()

    # head = insertAtI(head, 4, int(input("Enter the value you want to insert: ")))
    # printLL(head)
    # print(length(head))
    # print()
    #
    # head = insertAtIR(head, 0, int(input("Enter the value you want to insert: ")))
    # printLL(head)
    # print(length(head))
    # print()
    #
    # printNode(head, int(input("Enter the node you want to print: ")))

    head = deleteNodeIR(head, 3)
    printLL(head)
    print(length(head))



