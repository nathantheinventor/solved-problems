while True:
    try:
        n, b, h, w = map(int, input().split())
    except:
        exit(0)
    ans = b + 1
    for _ in range(h):
        p = int(input())
        weeks = [int(x) for x in input().split()]
        if max(weeks) >= n:
            ans = min(ans, n * p)
    if ans <= b:
        print(ans)
    else:
        print("stay home")

