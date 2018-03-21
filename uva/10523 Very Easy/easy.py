n,a = map(int, input().split())
while True:
    ans = sum([i * a ** i for i in range(1, n + 1)])
    print(ans)
    
    try:
        n,a = map(int, input().split())
    except:
        exit(0)