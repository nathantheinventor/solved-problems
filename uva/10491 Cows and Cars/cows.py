a, b, c = map(int, input().split())
while True:
    ans = (b / (a + b)) * ((b - 1) / (a + b - c - 1))
    ans += (a / (a + b)) * ((b) / (a + b - c - 1))
    print("{:.5f}".format(ans))
    try:
        a, b, c = map(int, input().split())
    except:
        exit(0)