for _ in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    
    total = 0
    if h > c:
        total = min(b // 2, p) * h
        b = max(0, b - p * 2)
        total += min(b // 2, f) * c
    else:
        total = min(b // 2, f) * c
        b = max(0, b - f * 2)
        total += min(b // 2, p) * h
    print(total)