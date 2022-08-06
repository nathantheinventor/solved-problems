import random

n, m = 10 ** 5, 20
poss = "abcdefghijklmnopqrstuvwxyz"[:m]
print(n, m)
print("".join(random.choice(poss) for _ in range(n)))
