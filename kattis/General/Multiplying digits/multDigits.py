b, n = map(int, input().split())
if n == 1:
    print(1)
    exit(0)
factors = []
while n > 1:
    for i in range(b - 1, 1, -1):
        if n % i == 0:
            factors.append(i)
            n //= i
            break
    else:
        print("impossible")
        exit(0)

tmp = 1
ans = 0
for i in factors:
    ans += i * tmp
    tmp *= b
print(ans)