def solve(n, m):
    pos = 0
    l = [i for i in range(1, n + 1)]
    for _ in range(n - 1):
        del l[pos]
        pos = (pos + m - 1) % len(l)
    return l[0]

n = int(input())
while n > 0:
    for m in range(1, 1000):
        if solve(n, m) == 13:
            print(m)
            break
    else:
        print("no solution to", n)
    n = int(input())