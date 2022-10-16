from StackUsingArray import Stack

def minReverse(s : str) -> int:
    if len(s) % 2 == 1:
        return -1

    stack = Stack()

    for i in s:
        if i == '{':
            stack.push(i)

        else:
            if stack.size() == 0:
                stack.push(i)

            elif stack.top() == '{':
                stack.pop()

            else:
                stack.push(i)

    count = 0
    while stack.size() != 0:
        c1 = stack.pop()
        c2 = stack.pop()

        if c1 == c2:
            count += 1
        else:
            count += 2

    return count

if __name__ == '__main__':
    s = input("Enter a expression: ")
    print(minReverse(s))