from math import factorial
f = factorial(13)

MOD = 10 ** 9 + 7

for i in range(100000000):
    if i * f % MOD == 843230316:
        print(i)