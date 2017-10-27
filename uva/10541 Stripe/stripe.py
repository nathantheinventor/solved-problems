from math import factorial as f

for _ in range(int(input())):
    l = [int(x) for x in input().split()]
    num = l[0] - sum(l[1:]) + 1
    bins = l[1]
    if num < 0:
        print(0)
    else:
        ans = f(bins + num)
        ans //= f(bins)
        ans //= f(num)
        print(ans)