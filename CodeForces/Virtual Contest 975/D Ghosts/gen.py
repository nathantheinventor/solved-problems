import random
n = 200000
a = random.randint(1, 10 ** 2)
b = random.randint(-10 ** 2, 10 ** 2)
print(n, a, b)
for _ in range(n):
    x = _
    vx = random.randint(-10 ** 2, 10 ** 2)
    vy = random.randint(-10 ** 2, 10 ** 2)
    print(x, vx, vy)