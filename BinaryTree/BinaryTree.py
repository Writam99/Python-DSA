class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, end = ':')
    if root.left != None:
        print("L", root.left.data, end = ',')

    if root.right != None:
        print("R", root.right.data, end = '')

    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput(s = "Enter the value of root: "):
    rootData = int(input(s))
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    leftTree = treeInput("Enter the left child of " + str(rootData) + ": ")
    rightTree = treeInput("Enter the right child of " + str(rootData) + ": ")

    root.left = leftTree
    root.right = rightTree
    return root

def numNodes(root):
    if root == None:
        return 0

    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount

def largestData(root):
    if root == None:
        return -float("inf")

    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)

    largest = max(leftLargest, rightLargest, root.data)
    return largest

def height(root):
    if root == None:
        return 0

    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return 1 + max(leftHeight, rightHeight)

def numLeafNodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1

    numLeafLeft = numLeafNodes(root.left)
    numLeafRight = numLeafNodes(root.right)
    return numLeafLeft + numLeafRight

def printDepthK(root, k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left, k -1)
    printDepthK(root.right, k - 1)

def printDepthKV2(root, k, d = 0):
    if root == None:
        return
    if k == d:
        print(root.data)
        return
    printDepthKV2(root.left, k, d + 1)
    printDepthKV2(root.right, k, d + 1)

#Question 1 : Sum of nodes
def sumNodes(root):
    if root == None:
        return 0
    leftSum = sumNodes(root.left)
    rightSum = sumNodes(root.right)
    return root.data + leftSum + rightSum

#Question 2 : Preorder Binary Tree
def preOrder(root):
    if root == None:
        return
    print(root.data, end = ' ')
    preOrder(root.left)
    preOrder(root.right)

#Question 3 : Postorder Binary Tree
def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=' ')

#Question 4 : Nodes Grater than X
def nodesGreater(root, x):
    if root is None:
        return 0

    leftGreater = nodesGreater(root.left, x)
    rightGreater = nodesGreater(root.right, x)
    if root.data > x:
        return 1 + leftGreater + rightGreater
    return leftGreater + rightGreater

#Question 5 : Replace Nodes With Depth
def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.data, end = ' ')
    inOrder(root.right)

def replaceNodes(root, d = 0):
    if root is None:
        return

    root.data = d
    replaceNodes(root.left, d + 1)
    replaceNodes(root.right, d + 1)

#Assignment 1 : Is Node Present?
def isPresent(root, x):
    if root is None:
        return False

    if root.data == x:
        return True
    smallOuput = isPresent(root.left, x)
    if smallOuput is False:
        return isPresent(root.right, x)
    return smallOuput

#Assignment 2 : Nodes Without Sibling
def noSiblings(root):
    if root == None:
        return
    elif root.left != None and root.right == None:
        print(root.left.data, end = ' ')
        noSiblings(root.left)
    elif root.right != None and root.left == None:
        print(root.right.data, end = ' ')
        noSiblings(root.right)
    else:
        noSiblings(root.left)
        noSiblings(root.right)


if __name__ == '__main__':
    root = treeInput()
    printTreeDetailed(root)
    # print("No. of nodes =", numNodes(root))
    # print("Largest node data = ", largestData(root))
    # print("Height of Tree = ", height(root))
    # print("Number of leaf nodes = ", numLeafNodes(root))
    # printDepthK(root, k = int(input("Enter the depth: ")))
    # printDepthKV2(root, k=int(input("Enter the depth: ")))

    # Question 1
    # print(sumNodes(root))

    # Question 2
    # preOrder(root)

    # Question 3
    # postOrder(root)

    # Question 4
    # print(nodesGreater(root, x = int(input("Enter the value of x: "))))

    #Question 5
    replaceNodes(root)
    inOrder(root)

    # Assignment 1
    # print(isPresent(root, x = int(input("Enter the data: "))))

    #Assignment 2
    # noSiblings(root)