l = [(0, 1), (1, 1)]

for _ in range(40):
    a, b = l[-2]
    c, d = l[-1]
    l.append((a + c, b + d + 1))

for _ in range(int(input())):
    n = int(input())
    a, b = l[n]
    print("fib({}) = {} calls = {}".format(n, b - 1, a))