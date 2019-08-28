import random

n = 5 * 10 ** 5
print(n)
for i in range(n):
    t, a = random.choice([1,2]), random.randint(1, 500000)
    if t == 1:
        b = random.randint(-10000, 10000)
    else:
        b = random.randint(0, a - 1)
    print(t, a, b)