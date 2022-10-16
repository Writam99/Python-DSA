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

#Assignment 1
def findNode(head, data):
    count = 0
    while head is not None:
        if head.data == data:
            return count
        else:
            count += 1
            head = head.next
    return -1

#Assignment 2
def appendLastNToFirst(head, n):
    len = length(head)
    if n <= 0 or n >= len:
        return head
    
    indexFromFirst = len - n
    curr = head
    index = 0
    while index < len:
        # 1->2->3->4->5->None; n = 3, len = 5; indexFromFirst = 2 OUTPUT : 3->4->5->1->2->None
        # catching the node after which the next nodes are going to be moved i.e Node 2 or index 1
        if index == indexFromFirst - 1:
            newHead = curr.next     #setting the newHead to the next node i.e setting 3 as newHead
            newTail = curr          #setting the current Node as newTail i.e 2 is the newTail

        #setting the last node point to original head i.e making 5 point to 1
        if index == len - 1:
            curr.next = head
            break
        curr = curr.next
        index += 1

    newTail.next = None  #setting the newTail point to None i.e making 2 point to None
    return newHead

#Assignment 3
def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    prev = head
    curr = head.next
    while curr is not None:
        if prev.data == curr.data:
            prev.next = curr.next
            del(curr)
            curr = prev.next
        else:
            prev = curr
            curr = curr.next

    return head
'''
def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    t1 = head
    t2 = head.next
    while t2 is not None:
        if t1.data == t2.data:
            t2 = t2.next
        else:
            t1.next = t2
            t1 = t2
            t2 = t2.next

    t1.next = t2
    return head
'''

#Assignment 4
def printReversedLL(head):
    if head is None:
        return
    printReversedLL(head.next)
    print(str(head.data), end = ' ')
    return

#Done by me
def reverseLL(head):
    tail = Node(head.data)
    curr = head.next
    while curr is not None:
        newNode = Node(curr.data)
        newNode.next = tail
        tail = newNode
        curr = curr.next
    return tail

#Done by me
def checkPalindrome(head):
    tail = reverseLL(head)
    while head is not None:
        if tail.data != head.data:
            return False
        tail = tail.next
        head = head.next
    return True
if __name__ == '__main__':

    head = takeInput()
    printLL(head)
    print(length(head))
    print()

    # Assignment 1
    # print(findNode(head, int(input("Enter the node u want to search: "))))

    # Assignment 2
    # head = appendLastNToFirst(head, int(input("Enter the value of n: ")))
    # printLL(head)

    # Assignment 3
    # head = removeDuplicates(head)
    # printLL(head)

    # Assignment 4
    # printReversedLL(head)

    # head = reverseLL(head)
    # printLL(head)

    print(checkPalindrome(head))