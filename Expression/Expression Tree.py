class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treeInput(s = "Enter the value of root: "):
    rootData = input(s)
    if rootData == 'done':
        return None

    root = BinaryTreeNode(rootData)
    leftTree = treeInput("Enter the left child of " + rootData + ": ")
    rightTree = treeInput("Enter the right child of " + rootData + ": ")

    root.left = leftTree
    root.right = rightTree
    return root

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

def evaluate(root):
    if root is None:
        return None
    if root.data.isdigit():
        return root.data

    left = evaluate(root.left)
    right = evaluate(root.right)

    return str(eval(left + root.data + right))

if __name__ == '__main__':
    root = treeInput()
    printTreeDetailed(root)
    result = evaluate(root)
    print(result)

