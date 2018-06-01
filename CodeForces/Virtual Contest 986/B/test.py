import random

n = 1000000
l = list(range(1, n + 1))
for _ in range(3 * n):
    i, j = random.randint(0, n -1 ), random.randint(0, n - 1)
    while i == j:
        i, j = random.randint(0, n -1 ), random.randint(0, n - 1)
    l[i], l[j] = l[j], l[i]
print(n)
print(*l)