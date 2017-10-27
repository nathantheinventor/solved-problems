a, b = map(int, input().split())
while True:
    print(abs(b - a))
    try:
        a, b = map(int, input().split())
    except:
        exit(0)