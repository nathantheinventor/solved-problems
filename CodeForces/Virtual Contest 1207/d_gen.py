import random

n = 3 * 10 ** 5
print(n)
for _ in range(n):
    a = random.randint(0, n)
    b = random.randint(0, n)
    print(a, b)
