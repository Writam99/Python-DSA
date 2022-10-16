#Iterative Approach
def checkMax(arr):
    size = len(arr)
    for i in range(len(arr)):
        parentIndex = i
        leftChildIndex = 2 * i + 1
        rightChildIndex = 2 * i + 2

        if leftChildIndex < size and arr[parentIndex] < arr[leftChildIndex]:
            return False

        if rightChildIndex < size and arr[parentIndex] < arr[rightChildIndex]:
            return False

    return True

"""
#Recursive Approach
def checkMax(arr, parentIndex = 0, size = None):
    if size == None:
        size = len(arr)
    if parentIndex >= size - 1:
        return True

    leftChildIndex = 2*parentIndex + 1
    rightChildIndex = 2*parentIndex + 2

    if leftChildIndex < size and arr[parentIndex] < arr[leftChildIndex]:
        return False

    if rightChildIndex < size and arr[parentIndex] < arr[rightChildIndex]:
        return False

    isLeftMax = checkMax(arr, leftChildIndex, size)
    isRightMax = checkMax(arr, rightChildIndex, size)

    return isLeftMax and isRightMax
"""

if __name__ == '__main__':
    arr = [int(ele) for ele in input().split()]
    print(checkMax(arr))