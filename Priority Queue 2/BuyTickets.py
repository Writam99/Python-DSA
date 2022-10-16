import queue
from MaxPQ import PriorityQueueNode, PriorityQueue
#Assignment 3 : Buy The Ticket
def findTime(arr, k):
    maxPq = PriorityQueue()
    q = queue.Queue()

    for index, value in enumerate(arr):
        maxPq.insert(value, value)
        q.put(index)

    time = 0
    while True:
        personAtFrontIndex = q.get()
        if arr[personAtFrontIndex] == maxPq.getMax() and personAtFrontIndex == k:
            time += 1
            return time

        elif arr[personAtFrontIndex] == maxPq.getMax():
            time += 1
            maxPq.removeMax()

        else:
            q.put(personAtFrontIndex)


if __name__ == '__main__':
    arr = [int(ele) for ele in input().split()]
    k = int(input("Enter k: "))
    print("Time taken =", findTime(arr, k))
