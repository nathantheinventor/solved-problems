import random

n = 200_000
print(n)
print(*[random.randint(1, 10 ** 9) for _ in range(n)])
print(n)
for _ in range(n):
    print(random.randint(1, 10 ** 9))