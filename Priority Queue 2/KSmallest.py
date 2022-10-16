import heapq
def kSmallest(arr, k):
    heap = arr[:k]
    heapq._heapify_max(heap)

    for i in range(k, len(arr)):
        if heap[0] > arr[i]:
            heapq._heapreplace_max(heap, arr[i])

    return heap

if __name__ == '__main__':
    arr = [int(ele) for ele in input().split()]
    k = int(input("Enter k: "))
    elements = kSmallest(arr, k)
    for ele in elements:
        print(ele, end = ' ')