class Point:
    def __init_(self, x, y):
        self.x = x
        self.y = y

def myFun(p):
    return p.x

l = [Point(3, 5), Point(10, 5), Point(3, 8)]
l.sort(key=myFun)

for i in l:
    print(i.x, i.y)