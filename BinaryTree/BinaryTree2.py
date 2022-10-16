import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

def removeLeaves(root):
    if root == None:
        return None

    if root.left == None and root.right == None:
        return None

    root.left = removeLeaves(root.left)
    root.right = removeLeaves(root.right)
    return root

def getHeightAndCheckBalanced(root):
    if root == None:
        return 0, True

    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)

    h = 1 + max(lh, rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, False
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False

def isBalanced(root):
    h, isRootBalanced = getHeightAndCheckBalanced(root)
    return isRootBalanced

#Question 1 : Mirror Binary Tree
def mirror(root):
    if root == None:
        return

    root.left = mirror(root.left)
    root.right = mirror(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp
    return root

#Question 2 : Diameter of a Binary Tree
def getHeightAndDiameter(root):
    if root == None:
        return 0, 0

    lh, ld = getHeightAndDiameter(root.left)
    rh, rd = getHeightAndDiameter(root.right)

    h = 1 + max(lh, rh)
    sumHeight = lh + rh
    smallDiameter = max(ld, rd, sumHeight)
    return h, smallDiameter

def diameter(root):
    h, rootDiameter = getHeightAndDiameter(root)
    return rootDiameter

def takeLevelWiseTreeInput():
    q = queue.Queue()
    rootData = int(input("Enter root: "))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)

    while not q.empty():
        current_node = q.get()
        leftChildData = int(input("Enter left child of " + str(current_node.data) + ": "))
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        rightChildData = int(input("Enter right child of " + str(current_node.data) + ": "))
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root

#Question 3 : Print Level Wise Binary Tree
def printLevelWise(root):
    if root == None:
        return

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current_node = q.get()
        print(current_node.data, end = ': ')
        
        if current_node.left != None:
            leftChild = current_node.left
            print("L", leftChild.data, end = ', ')
            q.put(leftChild)
        
        if current_node.right != None:
            rightChild = current_node.right
            print("R", rightChild.data, end = '')
            q.put(rightChild)

        print()

def buildTreeFromPreIn(pre, inorder):
    if len(pre) == 0:
        return None

    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1
    for i in range(len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None

    leftInorder = inorder[0 : rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder + 1 : ]

    lenLeftSubTree = len(leftInorder)

    leftPreorder = pre[1 : lenLeftSubTree + 1]
    rightPreorder = pre[lenLeftSubTree + 1 : ]

    leftChild = buildTreeFromPreIn(leftPreorder, leftInorder)
    rightChild = buildTreeFromPreIn(rightPreorder, rightInorder)

    root.left = leftChild
    root.right = rightChild
    return root

#Question 4 : Construct Tree from Postorder and Inorder
def buildTreeFromPostIn(post, inorder):
    if len(post) == 0:
        return None

    rootData = post[-1]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1
    for i in range(len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None

    leftInorder = inorder[0: rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder + 1:]

    lenLeftSubTree = len(leftInorder)

    leftPostorder = post[0 : lenLeftSubTree]
    rightPostorder =  post[lenLeftSubTree : len(post) - 1]

    leftChild = buildTreeFromPostIn(leftPostorder, leftInorder)
    rightChild = buildTreeFromPostIn(rightPostorder, rightInorder)

    root.left = leftChild
    root.right = rightChild
    return root

#Assignment 1 : Create and Insert Duplicate Node
def duplicate(root):
    if root == None:
        return None

    duplicateNode = BinaryTreeNode(root.data)
    duplicateNode.left = root.left
    root.left = duplicateNode

    duplicate(duplicateNode.left)
    duplicate(root.right)

#Assignment 2 : Min and Max of Binary Tree
def maxmin(root):
    if root == None:
        maximum = -float("inf")
        minimum = float("inf")
        return (maximum, minimum)

    leftMax, leftMin = maxmin(root.left)
    rightMax, rightMin = maxmin(root.right)

    newMax = max(leftMax, rightMax, root.data)
    newMin = min(leftMin, rightMin, root.data)
    return (newMax, newMin)

#Assignment 3 : Level order traversal
def printLevelWiseV2(root):
    if root == None:
        return

    q = queue.Queue()
    q.put(root)
    q.put(None)

    while True:
        current_node = q.get()
        if current_node == None:
            print()
            if q.empty() is True:
                break
            else:
                q.put(None)
        else:
            print(current_node.data, end = ' ')

            if current_node.left != None:
                q.put(current_node.left)

            if current_node.right != None:
                q.put(current_node.right)

#Assignment 4 : Path Sum Root to Leaf
# def printPath(root, k, path = ''):
#     if root == None:
#         return
#     if root.left == None and root.right == None and root.data == k:
#         path = path + ' ' + str(root.data)
#         print(path)
#         return
#
#     #Little Optimization
#     if k - root.data <= 0:
#         return
#
#     if len(path) == 0:
#         path += str(root.data)
#     else:
#         path = path + ' ' + str(root.data)
#
#     printPath(root.left, k - root.data, path)
#     printPath(root.right, k - root.data, path)

def printPath(root, k, path=[]):
    if root.left == None and root.right == None and root.data == k:
        path.append(root.data)
        for i in  path:
            print(i, end = ' ')
        print()
        path.pop()
        return True

    path.append(root.data)

    if root.left is not None and k - root.left.data >= 0:
        printPath(root.left, k - root.data, path)

    if root.right is not None and k - root.right.data >= 0:
        printPath(root.right, k - root.data, path)

    path.pop()
#Assignment 5 : Print nodes at distance k from node
def printDepthK(root, k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left, k -1)
    printDepthK(root.right, k - 1)
'''
def printNodesAtK(root, k, target):
    if root == None:
        return False, -1
    if root.data == target:
        printDepthK(root, k)
        return True, 0

    leftSearch, leftDistance = printNodesAtK(root.left, k, target)
    rightSearch, rightDistance = printNodesAtK(root.right, k, target)

    if leftSearch is True:
        newDistance = 1 + leftDistance
        newk = k - newDistance - 1
        printDepthK(root.right, newk)
        return True, newDistance

    if rightSearch is True:
        newDistance = 1 + rightDistance
        newk = k - newDistance - 1
        printDepthK(root.left, newk)
        return True, newDistance

    return False, -1
'''
#Improved version
def printNodesAtK(root, k, target):
    if root == None:
        return False, -1
    if root.data == target:
        printDepthK(root, k)
        return True, 0

    leftSearch, leftDistance = printNodesAtK(root.left, k, target)
    if leftSearch is True:
        newDistance = 1 + leftDistance
        newk = k - newDistance - 1
        printDepthK(root.right, newk)
        return True, newDistance
    else:
        rightSearch, rightDistance = printNodesAtK(root.right, k, target)
        if rightSearch is True:
            newDistance = 1 + rightDistance
            newk = k - newDistance - 1
            printDepthK(root.left, newk)
            return True, newDistance

    return False, -1

if __name__ == '__main__':
    root = takeLevelWiseTreeInput()
    # Question 3
    printLevelWise(root)

    # root = removeLeaves(root)
    # printTreeDetailed(root)

    # Question 1
    # root = mirror(root)
    # print("Mirrored: ")
    # printTreeDetailed(root)

    # print(isBalanced(root))

    # Question 2
    # print("Diameter = ", diameter(root))

    # preOrder = [1,2,4,5,3,6,7]
    # inOrder = [4,2,5,1,6,3,7]
    # root = buildTreeFromPreIn(preOrder, inOrder)
    # printLevelWise(root)

    #Question 4
    # postOrder = [4,5,2,6,7,3,1]
    # inOrder = [4, 2, 5, 1, 6, 3, 7]
    # root = buildTreeFromPostIn(postOrder, inOrder)
    # printLevelWise(root)

    #Assignment 1
    # duplicate(root)
    # print("Modified :")
    # printTreeDetailed(root)

    # Assignment 2
    # maximum, minimum = maxmin(root)
    # print(minimum, maximum)

    # printLevelWiseV2(root)

    # Assignment 4
    printPath(root, k = int(input("Enter the value of k: ")))

    # Assignment 5
    # print("Nodes are : ")
    # printNodesAtK(root, k = int(input("Enter k: ")), target= int(input("Enter target node : ")))