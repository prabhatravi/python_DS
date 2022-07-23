def firstIndex(l,x):
    
    for i in range(len(l)):

        if l[i] == x:
            return i

    return -1

def firstIndexBS(l, x):
    low = 0

    high = len(l) - 1

    while low <= high:

        mid = (low + high) // 2

        if l[mid] > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1

        else:
            if mid == 0 or l[mid - 1] != l[mid]:
                return mid
            else:
                high = mid - 1
    return -1


l = [5, 10, 10, 20, 20]

print(10, firstIndex(l, 10))
print(20, firstIndex(l, 20))
print(50, firstIndex(l, 50))
print("______________________")
print(10, firstIndexBS(l, 10))
print(20, firstIndexBS(l, 20))
print(50, firstIndexBS(l, 50))

