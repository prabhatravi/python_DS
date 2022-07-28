def myFun(s):
    return len(s)

l = ['gfg', 'courses', 'python']
# custom sorting based on func
l.sort(key=myFun)
print(l)

# custom sorting based on func and reverse the sorting
l.sort(key=myFun, reverse=True)
print(l)

l1 = ['gfg', 'ide', 'courses']
# alphabetically
l1.sort()
print(l1)

l2 = [5, 10, 15, 1]
l2.sort()
print(l2)

l3 = [1, 5, 3, 10]
l3.sort(reverse=True)
print(l3)