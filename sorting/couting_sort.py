def countingSort(arr, k):
    count = [0]*k
    for x in arr:
        count[x] += 1
    index = 0
    for i in range(k):
        for j in range(count[i]):
            arr[index] = i
            index += 1

def genericCountingSort(arr, k):
    output = [0] * len(arr)
    count = [0] * (k)
    for x in arr:
        count[x] += 1

    for i in range(1, k):
        count[i] += count[i-1]
    for x in reversed(arr):
        output[count[x]-1] = x
        count[x] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

arr = [1, 4, 4, 1, 0, 1]
# o/p [0, 1, 1, 1, 4, 4]
countingSort(arr, 6)
print(arr)
arr1 = [1, 4, 4, 2, 0, 1]
genericCountingSort(arr1, 6)
print(arr1)