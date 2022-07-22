from collections import Counter
def isPalPer(s):
    cnt=Counter(s) # thea(n)
    odd=0
    for freq in cnt.values():
        if freq%2!=0:
            odd=odd+1
            if odd>1:
                return False
    return True
    
s="geeksgeeks"
print(isPalPer(s))

# cnt = Counter({'g':2, 'e':4, 'k':2, 's':2})
# after loop: odd = 0, return True