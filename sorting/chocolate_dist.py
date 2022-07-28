def minDiff(arr, m):
    if (m == 0 or len(arr) == 0):
        return 0
    if (len(arr) < m):
        return -1
    arr.sort()
    res = arr[m-1] - arr[0]
    for i in range(1, len(arr)-m+1):
        res = min(res, arr[i+m-1] -arr[i])
    return res

arr = [7, 3, 1, 8, 9, 12, 56]
m = 3
print(minDiff(arr, m))