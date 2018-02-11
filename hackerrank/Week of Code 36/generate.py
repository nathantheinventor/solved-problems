n = 100000
print(n)
print(n)
x = []
y = []
for i in range(n - 1):
    x.append(n - i)
    y.append(-i)
print(" ".join(map(str, x)))
print(" ".join(map(str, y)))