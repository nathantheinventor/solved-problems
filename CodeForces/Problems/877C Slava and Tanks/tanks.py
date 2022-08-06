n = int(input())
if n == 2:
    print(3)
    print(2, 1, 2)
    exit(0)

ans = [i for i in range(2, n + 1, 2)]
ans += [i for i in range(1, n + 1, 2)]
ans += [i for i in range(2, n + 1, 2)]
print(len(ans))
print(*ans)