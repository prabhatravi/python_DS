from collections import deque

d = deque([10, 20, 30, 40, 50])
d.insert(2, 10)
print(d)
print(d.count(10))
d.remove(10)
print(d)
d.extend([60, 70])
print(d)
d.extendleft([15, 25])
print(d)