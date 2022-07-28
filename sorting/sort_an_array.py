# naive solution
def sortArr(arr):
    temp = []
    for x in arr:
        if x == 0:
            temp.append(x)

    for x in arr:
        if x == 1:
            temp.append(x)
    
    for x in arr:
        if x == 2:
            temp.append(x)
    
    for i in range(len(arr)):
        arr[i] = temp[i]

# Efficient Solution (Dutch National Flag Algorithm)
def sortArray(arr):
    lo, mid, hi = 0, 0, (len(arr)-1)

    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[hi], arr[mid] = arr[mid], arr[hi]
            hi -= 1


arr = [0, 1, 1, 2, 0, 1]
sortArr(arr)
print(arr)

arr1 = [0, 1, 2, 1, 1, 2]
sortArray(arr1)
print(arr1)