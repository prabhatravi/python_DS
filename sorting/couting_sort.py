def countingSort(arr, k):
    count = [0]*k
    for x in arr:
        count[x] += 1
    index = 0
    for i in range(k):
        for j in range(count[i]):
            arr[index] = i
            index += 1

arr = [1, 4, 4, 1, 0, 1]
# o/p [0, 1, 1, 1, 4, 4]
countingSort(arr, 6)
print(arr)