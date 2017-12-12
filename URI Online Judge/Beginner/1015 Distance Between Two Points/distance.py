a, b = map(float, input().split())
c, d = map(float, input().split())
x = a + b * 1j
y = c + d * 1j
print("{:.4f}".format(abs(x - y)))