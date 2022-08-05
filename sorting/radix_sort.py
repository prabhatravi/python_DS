def radixSort(arr):
    mx = max(arr)
    exp = 1
    while mx/exp > 1:
        countingSort(arr, exp)
        exp *= 10

def countingSort(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(0, n):
        index = (arr[i]//exp)
        count[index%10] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n-1
    while i>=0:
        index = (arr[i]//exp)
        output[count[index%10]-1] = arr[i]
        count[index%10] -= 1
        i -=1
    for i in range(0, n):
        arr[i] = output[i]

arr = [319, 212, 6, 8, 100, 50]
radixSort(arr)
print(arr)