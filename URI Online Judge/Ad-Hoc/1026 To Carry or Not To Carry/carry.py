def solve(a, b):
    return a ^ b

a, b = map(int, input().split())

while True:
    print(solve(a, b))
    try:
        a, b = map(int, input().split())
    except:
        exit(0)