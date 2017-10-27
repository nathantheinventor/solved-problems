
ans = {}
last = 9
for i in range(70):
    tmp = 1 << i
    ans[tmp] = last
    last = (last * last) % 1000000007

for _ in range(int(input())):
    n = int(input())
    x = n - 1
    ans2 = 8
    for i in ans:
        if i & x:
            ans2 = ans2 * ans[i] % 1000000007
    print(ans2)