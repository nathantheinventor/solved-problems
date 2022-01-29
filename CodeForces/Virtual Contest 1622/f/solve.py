import math

n = int(input())
f = [1]
for i in range(1, n + 1):
    f.append(f[-1] * i)

def perms(x):
    if x == 0:
        return [[0]]
    ans = []
    for y in perms(x - 1):
        ans.append(y + [0])
        ans.append(y + [1])
    return ans


def isQuad(x):
    n = 1
    for i, y in enumerate(x):
        if y:
            n *= f[i]
    sq = math.isqrt(n)
    # print(x, n, sq, sq * sq == n)
    if sq * sq == n:
        return True
    return False

ans = 1
ans2 = [1]
for x in perms(n):
    if sum(x) > ans and isQuad(x):
        ans = sum(x)
        ans2 = x

print(ans)
print(*[i for i, _ in enumerate(ans2) if _])
