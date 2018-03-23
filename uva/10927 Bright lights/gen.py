import random
for _ in range(5):
    print(100000)
    for _ in range(100000):
        x, y, z = random.randint(-100000, 100000), random.randint(0, 10000), random.randint(0, 10000)
        print(x, y, z)

print(0)