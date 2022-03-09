n = int(input())
def is_harshad(x):
    n = sum(map(int, str(x)))
    return x % n == 0

for i in range(n, n + 100000):
    if is_harshad(i):
        print(i)
        break