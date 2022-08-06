for _ in range(int(input())):
    h, w = map(int, input().split())
    ans = w * (w + 1) // 2 + w * h * (h + 1) // 2 - w
    print(ans)
