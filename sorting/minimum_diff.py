# naive solution
def minDiff(arr):
    res = float("inf")
    for i in range(1, len(arr)):
        for j in range(i):
            res = min(res, abs(arr[i]-arr[j]))
    return res

# Efficient solution
def findMinDiff(arr):
    res = float("inf")
    arr.sort()
    for i in range(1, len(arr)):
        res = min(res, abs(arr[i]-arr[i-1]))
    return res

arr = [5, 3, 8]
print(minDiff(arr))

arr1 = [10, 8, 1, 4]
print(findMinDiff(arr1))