class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.__root = None
        self.__numNodes = 0

    def __printTreeHelper(self, root):
        if root == None:
            return

        print(root.data, end=':')
        if root.left != None:
            print("L", root.left.data, end=',')

        if root.right != None:
            print("R", root.right.data, end='')

        print()
        self.__printTreeHelper(root.left)
        self.__printTreeHelper(root.right)

    def printTree(self):
        self.__printTreeHelper(self.__root)

    def __isPresentHelper(self, root, data):
        if root == None:
            return False

        if root.data == data:
            return True

        if root.data > data:
            return self.__isPresentHelper(root.left, data)
        else:
            return self.__isPresentHelper(root.right, data)

    def isPresent(self, data):
        return self.__isPresentHelper(self.__root, data)

    def __insertHelper(self, root, data):
        if root == None:
            node = BinaryTreeNode(data)
            return node

        if root.data > data:
            root.left = self.__insertHelper(root.left, data)
        else:
            root.right = self.__insertHelper(root.right, data)

        return root

    def insert(self, data):
        self.__numNodes += 1
        self.__root = self.__insertHelper(self.__root, data)

    def __min(self, root):
        if root == None:
            return float("inf")

        if root.left == None:
            return root.data

        return self.__min(root.left)

    def __deleteDataHelper(self, root, data):
        if root == None:
            return False, None
        
        if root.data < data:
            deleted, newRightNode = self.__deleteDataHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        
        if root.data > data:
            deleted, newLeftNode = self.__deleteDataHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root

        #root is leaf
        if root.left == None and root.right == None:
            return True, None

        #root has one child
        if root.left == None:
            return True, root.right

        if root.right == None:
            return True, root.left

        #root has two children
        replacement = self.__min(root.right)
        root.data = replacement
        deleted, newRightNode = self.__deleteDataHelper(root.right, replacement)
        root.right = newRightNode
        return True, root

    def deleteData(self, data):
        deleted, newRoot = self.__deleteDataHelper(self.__root, data)
        if deleted:
            self.__numNodes -= 1

        self.__root = newRoot
        return deleted

    def count(self):
        return self.__numNodes

if __name__ == '__main__':
    b = BST()
    b.insert(10)
    b.insert(5)
    b.insert(7)
    b.insert(6)
    b.insert(8)
    b.insert(12)
    b.insert(11)
    b.insert(15)
    b.printTree()

    print(b.count())

    #delete leaf
    # print("After deleting: ")
    # b.deleteData(8)
    # b.printTree()

    #root has one child
    # print("After deleting: ")
    # b.deleteData(5)
    # b.printTree()

    #root has two children
    print("After deleting: ")
    b.deleteData(10)
    b.printTree()
