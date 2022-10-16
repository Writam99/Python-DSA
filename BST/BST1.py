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

def printLevelWise(root):
    if root == None:
        return

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current_node = q.get()
        print(current_node.data, end=': ')

        if current_node.left != None:
            leftChild = current_node.left
            print("L", leftChild.data, end=', ')
            q.put(leftChild)

        if current_node.right != None:
            rightChild = current_node.right
            print("R", rightChild.data, end='')
            q.put(rightChild)

        print()

def search(root, x):
    if root == None:
        return False
    if root.data == x:
        return True
    elif root.data > x:
        return search(root.left, x)
    else:
        return search(root.right, x)

def printBetweenK1K2(root, k1, k2):
    if root == None:
        return

    if root.data > k2:
        printBetweenK1K2(root.left, k1, k2)

    elif root.data < k1:
        printBetweenK1K2(root.right, k1, k2)

    else:
        print(root.data)
        printBetweenK1K2(root.left, k1, k2)
        printBetweenK1K2(root.right, k1, k2)

#Question 1
def arrayToBST(arr, start, end):
    if start > end:
        return

    middle = (start + end)//2
    rootData = arr[middle]
    root = BinaryTreeNode(rootData)
    root.left = arrayToBST(arr, start, middle - 1)
    root.right = arrayToBST(arr, middle + 1, end)
    return root

def isBST2(root):
    if root == None:
        return float("inf"), -float("inf"), True

    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximum = max((leftMax, rightMax, root.data))

    isTreeBST = True

    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False

    if not(isLeftBST) or not(isRightBST):
        isTreeBST = False

    return minimum, maximum, isTreeBST

def isBST3(root, min_range = -float("inf"), max_range = float("inf")):
    if root == None:
        return True

    if root.data < min_range or root.data > max_range:
        return False

    isLeftWithinConstraints = isBST3(root.left, min_range, root.data-1)
    isRightWithinConstraints = isBST3(root.right, root.data, max_range)

    return isLeftWithinConstraints and isRightWithinConstraints

def nodeToRootPath(root, s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l

    leftOutput = nodeToRootPath(root.left, s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput

    rightOutput = nodeToRootPath(root.right, s)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None

if __name__ == '__main__':
    # root = takeLevelWiseTreeInput()
    # printTreeDetailed(root)

    # print(search(root, x = int(input("Enter the value you want to search: "))))

    # printBetweenK1K2(root, k1 = int(input("Enter k1: ")), k2 = int(input("Enter k2: ")))

    # Question 1
    print("Enter the elements of array with spaces :")
    x = [int(ele) for ele in input().split()]
    root = arrayToBST(x, 0, len(x) - 1)
    printTreeDetailed(root)