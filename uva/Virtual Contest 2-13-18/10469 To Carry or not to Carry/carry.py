a, b = map(int, input().split())
while True:
    print(a ^ b)
    try:
        a, b = map(int, input().split())
    except:
        exit(0)