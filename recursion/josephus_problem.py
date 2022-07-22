def jos(n, k):
    if n == 1:
        return 0
    else:
        return (jos(n - 1, k) + k) % n

def josBeginWithOne(n, k):
    return jos(n, k) + 1


print(jos(5, 3))
