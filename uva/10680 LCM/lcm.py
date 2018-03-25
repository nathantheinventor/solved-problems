ans = [0, 1]
cur = 1
factors = [[] for _ in range(1000001)]
for i in range(2, 1000001, 2):
    factors[i].append(2)
for i in range(3, 1000001, 2):
    if len(factors[i]) == 0:
        for k in range(i, 1000001, i):
            factors[k].append(i)

for i in range(2, 1000001):
    if len(factors[i]) == 1:
        for factor in factors[i]:
            cur *= factor
            while cur % 10 == 0:
                cur //= 10
            cur %= 1000
    ans.append(cur)

n = int(input())
while n > 0:
    # print(n)
    print(ans[n] % 10)
    n = int(input())