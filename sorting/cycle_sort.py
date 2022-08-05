def cycleSortDist(arr):
    for cs in range(len(arr)-1):
        item = arr[cs]
        pos = cs
        for i in range(cs+1, len(arr)):
            if arr[i] < item:
                pos = pos + 1
        if pos == cs:
            continue
        arr[pos], item = item, arr[pos]
        while pos != cs:
            pos = cs
            for i in range(cs+1, len(arr)):
                if arr[i] < item:
                    pos = pos + 1
            if pos == cs:
                continue
            arr[pos], item = item, arr[pos]

arr = [20, 40, 50, 10, 30]
cycleSortDist(arr)
print(arr)