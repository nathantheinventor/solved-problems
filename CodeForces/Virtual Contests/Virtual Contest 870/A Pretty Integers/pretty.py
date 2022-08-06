input()
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]

def isPretty(x):
    if x < 10:
        return x in l1 and x in l2
    x1 = x % 10
    x2 = x // 10
    
    if x1 not in l1 and x2 not in l1:
        return False
    if x1 not in l2 and x2 not in l2:
        return False
    return True

for i in range(99):
    if isPretty(i):
        print(i)
        break
