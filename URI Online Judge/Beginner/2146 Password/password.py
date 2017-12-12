n = int(input())
while True:
    print(n - 1)
    try:
        n = int(input())
    except:
        exit(0)