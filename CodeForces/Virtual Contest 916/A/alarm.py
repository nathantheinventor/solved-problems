x = int(input())

a, b = map(int, input().split())

ans = 0

def isLucky(h, m):
    if "7" in str(h) or "7" in str(m):
        return True
    return False

def sub(h, m, x):
    if m > x:
        return h, m - x
    else:
        m -= x
        while m < 0:
            m += 60
            h -= 1
        return h % 24, m

while not isLucky(a, b):
    a, b = sub(a, b, x)
    ans += 1

print(ans)