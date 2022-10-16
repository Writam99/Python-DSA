class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    # print('from here', head.data)
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

def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end = '')
        head = head.next

    print("None")
    return
#Assignmnet 1
def findFirstNodeR(head, n):
    if head.next is None:
        if head.data == n:
            return 0
        else:
            return -1

    if head.data == n:
        return 0

    smallOutput = findFirstNodeR(head.next, n)
    if smallOutput != -1:
        return 1 + smallOutput

    return smallOutput

#Assignment 2
def evenAferOdd(head):
    OddH = OddT = EvenH = EvenT = None
    
    while head is not None:
        if head.data % 2 == 1:
            if OddH is None:
                OddH = OddT = head
            else:
                OddT.next = head
                OddT = head
        else:
            if EvenH is None:
                EvenH = EvenT = head
            else:
                EvenT.next = head
                EvenT = head
        head = head.next
        
    if OddH is None:
        return EvenH

    if EvenH is None:
        return OddH

    OddT.next = None
    EvenT.next = None
    OddT.next = EvenH
    return OddH

#Assignment 3
def deleteEveryN(head, M, N):
    if M == 0:
        head = None
        return head
    if N == 0:
        return head

    t1 = head
    while True:
        cM = 1
        while cM != M and t1 != None:
            t1 = t1.next
            cM += 1

        if t1 is None or t1.next is None:
            break

        t2 = t1.next
        cN = 1
        while cN != N and t2 != None:
            next = t2.next
            del(t2)
            t2 = next
            cN += 1

        if t2 is None or t2.next is None:
            t1.next = None
            break

        t1.next = t2.next
        t1 = t2.next
        del(t2)

    return head

#Assignment 4
def swap(head, i, j):
    if i == j:
        return head
    smaller = min(i,j)
    bigger = max(i,j)

    prev = None
    curr = head
    count = 0
    while curr is not None:
        if count == smaller:
            prev1 = prev
            curr1 = curr

        if count == bigger:
            prev2 = prev
            curr2 = curr
            break
        prev = curr
        curr = curr.next
        count += 1

    if prev1 is not None:
        prev1.next = curr2

    prev2.next = curr1
    temp = curr1.next
    curr1.next = curr2.next
    curr2.next = temp

    if smaller == 0:
        head = curr2
    return head

#Assignment 5(both reverseI and kReverse are used in this assignment)
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

def kReverse(head, k):
    if head is None or head.next is None:
        return head

    head1 = tail = head
    count = 1
    while count != k and tail is not None:
        tail = tail.next
        count += 1

    if tail is not None:
        head2 = tail.next
        smallHead = kReverse(head2, k)
        tail.next = None
        newHead = reverseI(head1)
        head.next = smallHead
    else:
        newHead = reverseI(head1)

    return newHead

#Assignment 6
def midPoint(head):
    slow = fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

def palindrome(head):
    mid = midPoint(head)
    head2 = mid.next
    mid.next = None

    head2 = reverseI(head2)

    while head2 is not None:
        if head.data != head2.data:
            return False
        head = head.next
        head2 = head2.next
    return True

#Assignment 7
def bubbleSort(head):
    isSorted = False
    counter = 0
    size = length(head)
    while not isSorted:
        isSorted = True
        curr = head
        for i in range(size - 1 - counter):
            if curr.data > curr.next.data:
                head = swap(head, i, i + 1)
                isSorted = False
            else:
                curr = curr.next
        counter += 1
    return head


if __name__ == '__main__':

    head = takeInput()
    printLL(head)


    #Assignment 1
    # n = int(input("Value to be searched: "))
    # index = findFirstNodeR(head, n)
    # print(index)

    # Assignment 2
    # head = evenAferOdd(head)
    # printLL(head)

    # Assignment 3
    # head = deleteEveryN(head, 2, 3)
    # printLL(head)

    # Assignment 4
    # head = swap(head, int(input("Enter i :")), int(input("Enter j: ")))
    # printLL(head)

    # Assignment 5
    # head = kReverse(head, int(input("Enter the value of k: ")))
    # printLL(head)

    # Assignment 6
    # print(palindrome(head))

    # Assignment 7
    head = bubbleSort(head)
    printLL(head)