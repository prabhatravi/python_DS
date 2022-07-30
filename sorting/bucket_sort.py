def bucketSort(arr, k):
    res = max(arr) + 1 #Range Size
    bkt = [[] for i in range(k)]
    for x in arr:
        i = (k*x)//res
        bkt[i].append(x)
    for i in range(k):
        bkt[i].sort()

    idx = 0
    for i in range(k):
        for j in range(len(bkt[i])):
            arr[idx] = bkt[i][j]
            idx += 1



arr = [30, 40, 10, 80, 5, 12, 70]
k = 4
bucketSort(arr, k)
print(arr)