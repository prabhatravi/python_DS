class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    '''def __lt__(self, other):
        return self.x < other.x'''

    def __lt__(self, other):
    
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

def myFun(p):
    return p.x

l = [Point(3, 5), Point(10, 9), Point(1, 8)]
#l.sort(key=myFun)
l.sort()

for i in l:
    print(i.x, i.y)