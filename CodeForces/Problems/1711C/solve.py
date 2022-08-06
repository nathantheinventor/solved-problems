def s(a, n, m):
    ans = 0
    threes = False
    for x in sorted(a, reverse=True):
        if x >= 3 * n:
            threes = True
        if x >= 2 * n:
            ans += (x // n) * n
    return ans >= m * n and (threes or m % 2 == 0)

def solvable():
    n, m, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    if s(a, n, m):
        return True
    return s(a, m, n)

for _ in range(int(input())):
    print("Yes" if solvable() else "No")

    NDNepbzxp!*my$tdDS3L