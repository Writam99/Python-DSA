import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVL:
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

    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        #update height
        root.height = 1 + max(self.__getHeight(root.left), self.__getHeight(root.right))

        #find the balance factor of the parent elemnt whose child is the newly inserted element
        balanceFactor = self.__getBalance(root)
        if balanceFactor < -1:   # This is the balance of the root where the disbalance is observed
            if key > root.right.data:  #RR case of imbalance
                return self.__leftRotate(root)  #returns the updated root
            else:                      #RL case of imbalance
                root.right = self.__rightRotate(root.right) # In first rotation the root where disbalance was observed doesn't get affected
                return self.__leftRotate(root)

        if balanceFactor > 1:    # This is the balance of the root where the disbalance is observed
            if key < root.left.data:   #LL case of imbalance
                return self.__rightRotate(root)
            else:                      #LR case of imbalance
                root.left = self.__leftRotate(root.left)  # In first rotation the root where disbalance was observed doesn't get affected
                return self.__rightRotate(root)
        
        return root               # If balance is -1 or 0 or +1

    def __getMinNodeData(self, root):
        if root is None or root.left is None:
            return root.data
        return self.__getMinNodeData(root.left)

    def delete(self, root, key):
        if root is None:
            print("Key not found")
            return None

        if key < root.data:
            print("Going left of", root.data)
            root.left = self.delete(root.left, key)
        elif key > root.data:
            print("Going right of", root.data)
            root.right = self.delete(root.right, key)

        #found the node to be deleted
        else:
            # root is leaf
            if root.left == None and root.right == None:
                return None

            #root has only right child
            elif root.left is None:
                return root.right

            #root has only left child
            elif root.right is None:
                return root.left

            #root has both child
            # finding the minimum data on right subtree
            replacement = self.__getMinNodeData(root.right)
            root.data = replacement
            root.right = self.delete(root.right, replacement)
            #Note : If the node has both child, update its height and check its balance because it may be unbalanced after deletion. So don't return root from here.

        print("Updating balance and height of", root.data)
        # update height
        root.height = 1 + max(self.__getHeight(root.left), self.__getHeight(root.right))
        balanceFactor = self.__getBalance(root)
        if balanceFactor < -1:
            # Check if RR is possible
            if root.right.right is not None:
                return self.__leftRotate(root)
            # Else do RL
            else:
                root.right = self.__rightRotate(root.right)
                return self.__leftRotate(root)

        if balanceFactor > 1:
            # Check if LL is possible
            if root.left.left is not None:
                return self.__rightRotate(root)
            # Else do LR
            root.left = self.__leftRotate(root.left)
            return self.__rightRotate(root)

        return root  # If balance is -1 or 0 or +1

    # Level wise detailed tree printing
    def display(self, root):
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

if __name__ == '__main__':
    a = AVL()
    root = None
    for ele in [21,26,30,9,4,14,28,18,15,10,2,3,7]:
        root = a.insert(root, ele)
    a.display(root)

    for key in [1,2, 3]:
        print("Deleting", key, ":")
        root = a.delete(root, key)
        a.display(root)