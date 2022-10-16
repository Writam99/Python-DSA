#Question 1 : Pair Sum To Zero
def pair(arr):
    count = dict()

    for i in arr:
        if -i in count:
            fre = count[-i]
            for _  in range(fre):
                print(min(-i, i), max(-i, i))

        count[i] = count.get(i, 0) + 1

#Assignment 1 : Extract Unique characters
def removeDuplicate(s):
    count = dict()

    for char in s:
        if char not in count:
            print(char, end = '')
            count[char] = count.get(char, 0) + 1

#Assignment 2 : Longest Consecutive Subsequence
def lCSub(arr):
    count = dict()
    for index, value in enumerate(arr):
        count[value] = [True, index]

    maxLength = 0
    maxStart = None

    for i in arr:
        if count[i][0]:
            currentLength = 0
            currentStart = None

            count[i][0] = False
            currentStart = i
            currentLength += 1
            right = i + 1

            while right in count:
                count[right][0] = False
                currentLength += 1
                right += 1

            left = i - 1
            while left in count:
                count[left][0] = False
                currentLength += 1
                left -= 1
            currentStart = left + 1

            if currentLength > maxLength:
                maxLength = currentLength
                maxStart = currentStart
            elif currentLength == maxLength and count[currentStart][1] < count[maxStart][1]:
                maxLength = currentLength
                maxStart = currentStart

    print(maxStart, maxStart + maxLength - 1)

#Assignment 3 : Pairs with difference k
def pairK(arr, k):
    count = dict()
    pairs = 0
    for i in arr:
        if (i - k) in count:
            fre = count[i - k]
            for _  in range(fre):
                # print(min(i-k, i), max(i-k, i))
                print(i, i - k)
                pairs += 1

        count[i] = count.get(i, 0) + 1

    if k != 0:
        count.clear()

        for i in arr:
            if (i + k) in count:
                fre = count[i + k]
                for _ in range(fre):
                    # print(min(i + k, i), max(i + k, i))
                    print(i, i + k)
                    pairs += 1

            count[i] = count.get(i, 0) + 1

    print("Pairs = ",pairs)

#Assignment 4 : Longest consecutive subsets with sum zero
def sumZero(arr):
    count = dict()
    maxLength = 0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == 0:
            maxLength = i + 1

        elif sum in count:
            currLength = i - count[sum]
            if currLength > maxLength:
                maxLength = currLength

        elif sum not in count:
            count[sum] = i

    print(maxLength)



if __name__ == '__main__':
    #Question 1
    # x = [int(ele) for ele in input().split()]
    # pair(x)

    # Assignment 1
    # s = input("Enter string: ")
    # removeDuplicate(s)

    # Assignment 2
    # x = [int(ele) for ele in input().split()]
    # lCSub(x)

    #Assignment 3
    # x = [int(ele) for ele in input().split()]
    # k = int(input("Enter k: "))
    # pairK(x, k)

    # Assihnment 4
    x = [int(ele) for ele in input().split()]
    sumZero(x)