import math

def solve(a, b):
    return math.factorial(a) + math.factorial(b)

n, k = map(int, input().split())
while True:
    print(solve(n, k))
    try:
        n, k = map(int, input().split())
    except:
        break