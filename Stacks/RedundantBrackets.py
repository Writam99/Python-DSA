from StackUsingArray import Stack

def redundant(s: str) -> bool:
    stack = Stack()
    for i in s:
        if i != ')':
            stack.push(i)

        elif i == ')':
            count = 0
            while True:
                if stack.pop() != '(':
                    count += 1
                else:
                    break

            if count == 0:
                return True

    return False

if __name__ == '__main__':
    s = input("Enter a expression: ")
    print(redundant(s))


