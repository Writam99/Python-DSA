from QueueUsingArray import Queue

def reverseK(queue, k, original = None):
    if original is None:
        original = k
    if k == 0 or queue.size() == 0:
        return

    frontElement = queue.dequeue()
    reverseK(queue, k - 1, original)
    queue.enqueue(frontElement)

    if k == original:
        changes = queue.size() - k
        for _ in range(changes):
            ele = queue.dequeue()
            queue.enqueue(ele)

if __name__ == '__main__':
    queue = Queue()

    n = int(input("Enter the values you want to enter: "))
    for i in range(n):
        queue.enqueue(int(input("Enter a number: ")))

    k = int(input("Enter k: "))
    reverseK(queue, k)
    while queue.isEmpty() is False:
        print(queue.front(), end = ' ')
        queue.dequeue()
