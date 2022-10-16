def countingSort(arr):
    n = len(arr)
    max_ele = max(arr)
    count = [0]*(max_ele + 1)
    result = [0]* n

    #1. Store the count of each elemnt in count array
    for i in range(n):
        count[arr[i]] += 1

    #2. Store the cumulative sum of count array
    for i in range(1, max_ele + 1):
        count[i] += count[i-1]

    #3. Find the index of each elemnt of the original array in count array
    # and place the elemnts in resultant array

    i = n -1
    while i >= 0:
        result[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(n):
        arr[i] = result[i]

if __name__ == '__main__':
    arr = [120,178,269,48,56,1,25,2,98,100,120,269]
    countingSort(arr)
    print(arr)