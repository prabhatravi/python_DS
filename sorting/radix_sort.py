def radixSort(arr):
    mx = max(arr)
    exp = 1
    while mx/exp > 1:
        countingSort(arr, exp)
        exp *= 10

def countingSort(arr, exp):
    output = [0]*len(arr)
    count = [0]*10
    for i in range(0, len(arr)):
        index = (arr[i]//exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = len(arr)-1
    while i>=0:
        index = (arr[i]//exp)%10
        output[count[index]-1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]

arr = [319, 212, 6, 8, 100, 50]
radixSort(arr)
print(arr)