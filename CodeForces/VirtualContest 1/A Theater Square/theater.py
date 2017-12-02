n, m, a = map(int, input().split())

m = (((m - 1) // a) + 1)
n = (((n - 1) // a) + 1)
print(n * m)