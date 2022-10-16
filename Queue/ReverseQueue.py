from QueueUsingArray import Queue

def reverse(queue : Queue):
    if queue.size() == 0:
        return 

    frontElement = queue.dequeue()
    reverse(queue)
    queue.enqueue(frontElement)

if __name__ == '__main__':
    queue = Queue()
    n = int(input("Enter the values you want to enter: "))
    for i in range(n):
        queue.enqueue(int(input("Enter a number: ")))

    reverse(queue)
    while queue.isEmpty() is False:
        print(queue.front())
        queue.dequeue()
