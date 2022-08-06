import math

n, a, b = map(int, input().split())
rounds = int(math.log(n, 2))

a -= 1
b -= 1
a = ("000000000000" + bin(a)[2:])[-8:]
b = ("000000000000" + bin(b)[2:])[-8:]
for i, x, y in zip(range(100), a, b):
    if x != y:
        if (len(a) - i == rounds):
            print("Final!")
        else:
            print(len(a) - i)
        break