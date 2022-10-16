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

def printANode(node):
    print(node.data)

def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end = '')
        head = head.next

    print("None")
    return
#Reversing LL recursively
def reverseR(head):
    if head is None or head.next is None:
        return head

    smallHead = reverseR(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead

#Reversing LL iteratively
def reverseI(head):
    prev = None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    newHead = prev
    return newHead

#Mid point of LL
def midPoint(head):
    slow = fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

#Merge two Sorted LL
def merge(head1, head2):
    finalHead = finalTail = None
    while head1 != None and head2 != None:
        if head1.data < head2.data:
            if finalHead is None:
                finalHead = finalTail = head1
            else:
                finalTail.next = head1
                finalTail = finalTail.next
            head1 = head1.next
        else:
            if finalHead is None:
                finalHead = finalTail = head2
            else:
                finalTail.next = head2
                finalTail = finalTail.next
            head2 = head2.next

    if head1 is not None:
        finalTail.next = head1

    if head2 is not  None:
        finalTail.next = head2

    return finalHead

#Merge Sort
def mergeSort(head):
    if head.next is None:
        return head

    mid = midPoint(head)
    head2 = mid.next
    mid.next = None
    head1 = mergeSort(head)
    head2 = mergeSort(head2)
    finalHead = merge(head1, head2)
    return finalHead

if __name__ == '__main__':

    head = takeInput()
    printLL(head)
    print()

    # Reversing LL recursively
    # head = reverseR(head)
    # printLL(head)

    # Reversing LL iteratively
    # head = reverseI(head)
    # printLL(head)

    # Mid point of LL

    # node = midPoint(head)
    # printANode(node)

    #Merge two sorted LL
    # head1 = takeInput()
    # head2 = takeInput()
    # head3 = merge(head1, head2)
    # printLL(head3)

    # Merge Sort
    head1 = mergeSort(head)
    printLL(head1)
