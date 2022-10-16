import heapq
def kLargest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)

    for i in range(k, len(arr)):
        if heap[0] < arr[i]:
            heapq.heapreplace(heap, arr[i])

    return heap

if __name__ == '__main__':
    arr = [int(ele) for ele in input().split()]
    k = int(input("Enter k: "))
    elements = kLargest(arr, k)
    for ele in elements:
        print(ele, end = ' ')