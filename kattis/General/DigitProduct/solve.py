n = int(input())
def dp(x):
    p = 1
    for c in str(x):
        if c != "0":
            p *= int(c)
    return p

while n > 9:
    n = dp(n)

print(n)