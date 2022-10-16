def countingSort(arr, place):
    n = len(arr)
    count = [0] * 10
    result = [0] * n

    #calculate the count of each elemnt
    for i in range(n):
        index = arr[i] // place
        count[index % 10] += 1

    #calculate  cumulative sum
    for i in range(1,10):
        count[i] += count[i-1]

    #place the elemnts in sorted order
    i = n - 1
    while i >= 0:
        index = arr[i] // place
        result[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = result[i]

def radixSort(arr):
    #find maximum element
    max_element = max(arr)

    #apply counting sort to sort elements based on place value
    place = 1
    while max_element // place > 0:
        countingSort(arr, place)
        place *= 10

if __name__ == '__main__':
    arr = [120,178,269,48,56,1,25,2,98,100,120,269]
    radixSort(arr)
    print(arr)