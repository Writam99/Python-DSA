from StackUsingArray import Stack

def stockSpan(arr: list) -> list:
    stack = Stack()
    span = []
    span.append(1)
    stack.push(0)

    for index in range(1, len(arr)):
        if arr[index] <= arr[stack.top()]:
            span.append(1)
            stack.push(index)
        else:
            while stack.size() != 0 and arr[index] > arr[stack.top()]:
                stack.pop()

            if stack.size() == 0:
                span.append(index + 1)
                stack.push(index)

            else:
                span.append(index - stack.top())
                stack.push(index)

    return span


if __name__ == '__main__':
    x = [int(ele) for ele in input().split()]
    print(x)
    print(stockSpan(x))
