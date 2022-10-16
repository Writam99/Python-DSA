import queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, ":", end = '')
    for child in root.children:
        print(child.data, ', ', end = '')
    print()
    for child in root.children:
        printTreeDetailed(child)

def takeTreeInput(s = "Enter root data: "):
    rootData = int(input(s))
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    childrenCount = int(input("Enter no. of children for " + str(rootData) +  ": "))
    for i in range(childrenCount):
        child = takeTreeInput("Enter children " +str(i + 1) + " of node " + str(rootData) + ": ")
        root.children.append(child)
    return root

def numNodes(root):
    if root == None:
        return 0
    count = 1
    for child in root.children:
        count += numNodes(child)
    return count

#Question 1 : Sum of nodes
def sumNodes(root):
    if root == None:
        return 0

    sum = root.data
    for child in root.children:
        sum += sumNodes(child)
    return sum

#Question 2 : Node With Largest Data
def largestNode(root):
    if root is None:
        print("No nodes")
        return

    maximum = root.data
    for child in root.children:
        maximum = max(maximum, largestNode(child))
    return maximum

#Question 3 : Height of Tree
def height(root):
    if root is None:
        return 0

    childrenHeight = 0
    for child in root.children:
        childrenHeight = max(childrenHeight, height(child))
    return 1 + childrenHeight

def takeInputLevelWise():
    q = queue.Queue()
    rootData = int(input("Enter root data: "))
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    q.put(root)

    while not(q.empty()):
        current_node = q.get()
        print("Enter num of children for ", current_node.data)
        numChildren = int(input())

        for i in range(numChildren):
            print("Enter next child for", current_node.data)
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)

    return root

#Question 4 : Print Tree Levelwise
def printLevelWise(root):
    if root == None:
        return

    q = queue.Queue()
    q.put(root)

    while not (q.empty()):
        current_node = q.get()
        print(current_node.data, end = ":")
        for child in current_node.children:
            print(child.data, end = ', ')
            q.put(child)
        print()

#Assignment 1 : Contains x
def isPresent(root, x):
    #Edge case
    if root == None:
        return False

    if root.data == x:
        return True

    present = False
    for child in root.children:
        present = present or isPresent(child, x)

    return present

#Assignmnet 2 : Count Nodes
def countGreaterNodes(root, x):
    if root == None:
        return "No nodes"

    count = 0
    if root.data > x:
        count += 1

    for child in root.children:
        count += countGreaterNodes(child, x)
    return count

#Assignmnet 3 : Node With Maximum Child Sum
def maxNodeSumHelper(root):
    if root == None:
        return "No nodes"

    maxRootSum, maxRoot = root.data, root.data
    for child in root.children:
        maxRootSum += child.data

    for child in root.children:
        childMaxSum, childMaxRoot = maxNodeSumHelper(child)
        if childMaxSum > maxRootSum:
            maxRootSum = childMaxSum
            maxRoot = childMaxRoot

    return maxRootSum, maxRoot

def maxNodeSum(root):
    maxSum, maxRoot = maxNodeSumHelper(root)
    # print("max sum is =", maxSum)
    return maxRoot

#Assignment 4 : Structurally identical
def isIdentical(root1, root2):
    if root1 == None or root2 == None:
        return False

    if root1.data != root2.data:
        return False

    if len(root1.children) != len(root2.children):
        return False

    for i in range(len(root1.children)):
        isChildIdentical = isIdentical(root1.children[i], root2.children[i])
        if isChildIdentical is False:
            return isChildIdentical

    return True

#Assignment 5 : Next Larger
def nextLarger(root, x, ans = None):
    if root == None:
        return "Empty Tree"

    for child in root.children:
        ans = nextLarger(child, x, ans)

    if root.data > x and (ans == None or root.data < ans):
        ans = root.data

    return ans

#Assignment 6 : Replace With Depth
def replaceNodes(root, d = 0):
    if root == None:
        return "Empty Tree"

    root.data = d
    for child in root.children:
        replaceNodes(child, d + 1)

def printLevelWiseV2(root):
    if root == None:
        return "Empty Tree"

    q = queue.Queue()
    q.put(root)
    q.put(None)

    while True:
        current_node = q.get()
        if current_node == None:
            print()
            if q.empty():
                break
            else:
                q.put(None)

        else:
            print(current_node.data, end = ' ')

            for child in current_node.children:
                q.put(child)


if __name__ == '__main__':
    root = takeInputLevelWise()
    printLevelWise(root)

    # print("Number of nodes =",numNodes(root))

    # Question 1
    # print("Sum = ", sumNodes(root))

    # Question 2
    # print("Largest = ", largestNode(root))

    # Question 3
    # print("Height = ", height(root))

    # Assignment 1
    # result = isPresent(root, x = int(input("Enter the value of x: ")))
    # print(result)

    # Assignmnet 2
    count = countGreaterNodes(root, x = int(input("Enter the value of x: ")))
    print(count)

    # Assignmnet 3
    # result = maxNodeSum(root)
    # print(result)

    # Assignment 4
    # root1 = takeInputLevelWise()
    # root2 = takeInputLevelWise()
    #
    # print("Tree 1:")
    # printLevelWise(root1)
    #
    # print("Tree 2:")
    # printLevelWise(root2)
    #
    # print(isIdentical(root1, root2))

    # Assignment 5
    # print(nextLarger(root, x = int(input("Enter x: "))))

    # Assignment 6
    # replaceNodes(root)
    # printLevelWiseV2(root)