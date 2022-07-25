def countMerge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i = j = 0
    k = low
    res = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
            res += (len(left) - i)
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    return res

def countInv(arr, l, r):
    res = 0
    if l < r:
        m = (l + r)//2
        res += countInv(arr, l, m)
        res += countInv(arr, m+1, r)
        res += countMerge(arr, l, m, r)
    return res

arr = [10, 5, 30, 15, 7]

print("res: ",countInv(arr, 0, 4))
print(*arr)
