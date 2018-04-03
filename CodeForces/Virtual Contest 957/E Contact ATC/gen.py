import random

print(10, 5)
for _ in range(10):
    sign = random.choice((-1, 1))
    print(sign * random.choice(range(6, 50)), -sign * random.choice(range(6, 50)))