def down_heapify(arr, i, n):
    parentIndex = i
    leftChildIndex = 2*parentIndex + 1
    rightChildIndex = 2*parentIndex + 2

    while leftChildIndex < n:
        minIdx = parentIndex
        if arr[minIdx] > arr[leftChildIndex]:
            minIdx = leftChildIndex

        if rightChildIndex < n and arr[minIdx] > arr[rightChildIndex]:
            minIdx = rightChildIndex

        if minIdx == parentIndex:
            return

        arr[minIdx], arr[parentIndex] = arr[parentIndex], arr[minIdx]

        parentIndex = minIdx
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

    return

def heapSort(arr):
    #Build the heap
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        down_heapify(arr, i, n)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        down_heapify(arr, 0, i)

    return

if __name__ == '__main__':
    x = [int(ele) for ele in input().split()]
    heapSort(x) #Descending order
    print(x)