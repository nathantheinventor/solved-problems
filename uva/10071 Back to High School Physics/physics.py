a, b = map(int, input().split())
while True:
    print(b * a * 2)
    try:
        a, b = map(int, input().split())
    except:
        exit(0)