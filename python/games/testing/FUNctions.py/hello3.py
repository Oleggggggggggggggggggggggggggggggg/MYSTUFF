def addDown(n):
    total = 0
    for i in range(n):
        total = total + n
    return total

def addDownBetter(n):
    if n == 0:
        return 0
    return n + addDownBetter(n-1)

print(addDownBetter(10))
    
