def reverseStack(s1: list, s2: list) -> None:
    if len(s1) <= 1:
        return

    topElement = s1.pop()
    reverseStack(s1, s2)

    while len(s1) != 0:
        ele = s1.pop()
        s2.append(ele)

    s1.append(topElement)
    while len(s2) != 0:
        ele = s2.pop()
        s1.append(ele)

if __name__ == '__main__':
    s1 = [int(ele) for ele in input().split()]
    s2 = []
    reverseStack(s1, s2)

    while len(s1) != 0:
        print(s1.pop(), end=' ')