import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVL:
    def __init__(self):
        self.__root = None
        self.__numNodes = 0

    def __getHeight(self, root):
        if root is None:
            return -1
        return root.height

    def __getBalance(self, root):
        return self.__getHeight(root.left) - self.__getHeight(root.right)

    def __leftRotate(self, parent):
        # parent -> parent of the node which is to be rotated
        # rotate -> node which is to be rotated
        # temp -> left of node to be rotated
        rotate = parent.right
        temp = rotate.left
        rotate.left = parent
        parent.right = temp
        parent.height = 1 + max(self.__getHeight(parent.left), self.__getHeight(parent.right))
        rotate.height = 1 + max(self.__getHeight(rotate.left), self.__getHeight(rotate.right))
        return rotate  #returns the updated root

    def __rightRotate(self, parent):
        # parent -> parent of the node which is to be rotated
        # rotate -> node which is to be rotated
        # temp -> right of node to be rotated
        rotate = parent.left
        temp = rotate.right
        rotate.right = parent
        parent.left = temp
        parent.height = 1 + max(self.__getHeight(parent.left), self.__getHeight(parent.right))
        rotate.height = 1 + max(self.__getHeight(rotate.left), self.__getHeight(rotate.right))
        return rotate

    def __insertHelper(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.data:
            root.left = self.__insertHelper(root.left, key)
        else:
            root.right = self.__insertHelper(root.right, key)

        # update height
        root.height = 1 + max(self.__getHeight(root.left), self.__getHeight(root.right))

        # find the balance factor of the parent elemnt whose child is the newly inserted element
        balanceFactor = self.__getBalance(root)
        if balanceFactor < -1:  # This is the balance of the root where the disbalance is observed
            if key > root.right.data:  # RR case of imbalance
                return self.__leftRotate(root)  # returns the updated root
            else:  # RL case of imbalance
                root.right = self.__rightRotate(root.right)  # In first rotation the root where disbalance was observed doesn't get affected
                return self.__leftRotate(root)

        if balanceFactor > 1:  # This is the balance of the root where the disbalance is observed
            if key < root.left.data:  # LL case of imbalance
                return self.__rightRotate(root)
            else:  # LR case of imbalance
                root.left = self.__leftRotate(root.left)  # In first rotation the root where disbalance was observed doesn't get affected
                return self.__rightRotate(root)

        return root  # If balance is -1 or 0 or +1

    def insert(self, key):
        self.__numNodes += 1
        self.__root = self.__insertHelper(self.__root, key)

    def __isPresentHelper(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True
        if root.data > data:
            return self.__isPresentHelper(root.left, data)
        else:
            return self.__isPresentHelper(root.right, data)

    def isPresent(self, key):
        return self.__isPresentHelper(self.__root, key)

    def __getMinNodeData(self, root):
        if root is None or root.left is None:
            return root.data
        return self.__getMinNodeData(root.left)

    def __deleteHelper(self, root, key):
        if root is None:
            return False, None

        if key < root.data:
            deleted, root.left = self.__deleteHelper(root.left, key)
        elif key > root.data:
            deleted, root.right = self.__deleteHelper(root.right, key)

        #found the node to be deleted
        else:
            # root is leaf
            if root.left == None and root.right == None:
                return True, None

            #root has only right child
            elif root.left is None:
                return True, root.right

            #root has only left child
            elif root.right is None:
                return True, root.left

            #root has both child
            # finding the minimum data on right subtree
            replacement = self.__getMinNodeData(root.right)
            root.data = replacement
            deleted, root.right = self.__deleteHelper(root.right, replacement)
            #Note : If the node has both child, update its height and check its balance because it may be unbalanced after deletion. So don't return root from here.

        if deleted:
            #if deleted node then only update height and balance
            # update height
            root.height = 1 + max(self.__getHeight(root.left), self.__getHeight(root.right))
            #update balance
            balanceFactor = self.__getBalance(root)
            if balanceFactor < -1:
                # Check if RR is possible
                if root.right.right is not None:
                    return True, self.__leftRotate(root)
                # Else do RL
                else:
                    root.right = self.__rightRotate(root.right)
                    return True, self.__leftRotate(root)

            if balanceFactor > 1:
                # Check if LL is possible
                if root.left.left is not None:
                    return True, self.__rightRotate(root)
                # Else do LR
                root.left = self.__leftRotate(root.left)
                return True, self.__rightRotate(root)

            return True, root  # If balance is -1 or 0 or +1

        else:
            return False, root

    def delete(self, key):
        deleted, newRoot = self.__deleteHelper(self.__root, key)

        if deleted:
            self.__numNodes -= 1
            self.__root = newRoot
            return deleted
        else:
            print("Key not found")

    def length(self):
        return self.__numNodes

    # Level wise detailed tree printing
    def display(self):
        if self.__root == None:
            return

        q = queue.Queue()
        q.put(self.__root)

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

if __name__ == '__main__':
    a = AVL()

    for ele in [21,26,30,9,4,14,28,18,15,10,2,3,7]:
        a.insert(ele)
    a.display()
    print("No.of nodes", a.length())

    print(a.isPresent(14))
    print(a.isPresent(99))
    print()

    for key in [2,3,10,18,4,9,14,7,15,99]:
        print("Deleting", key, ":")
        a.delete(key)
        a.display()
        print("No.of nodes:", a.length())
        print()

    print(a.isPresent(14))
    