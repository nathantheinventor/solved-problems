for _ in range(int(input())):
    n, k = map(int, input().split())
    k += 1
    a = sorted([*{int(x) for x in input().split()}])
    ans = 0
    for x, y in zip(a, a[1:]):
        n = 10 ** (y -x) - 1
        if n >= k:
            ans += k * 10 ** x
            k -= n
            break
        ans += n * 10 ** x
        k -= n

    if k > 0:
        ans += k * 10 ** a[-1]

    print(ans)
