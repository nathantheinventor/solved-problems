n = int(input())
print("{}:".format(n))
for i in range(2, n):
    if n % (2 * i - 1) == 0:
        print("{},{}".format(i, i - 1))
    elif (n - i) % (2 * i - 1) == 0:
        print("{},{}".format(i, i - 1))
    if n % i == 0:
        print("{},{}".format(i, i))