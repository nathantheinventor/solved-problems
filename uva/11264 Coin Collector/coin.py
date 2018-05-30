for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    ans = 1
    sum = l[-1]
    prev = sum
    for i in l[-2::-1]:
        # print(i, sum, ans)
        if i < sum:
            ans += 1
            sum = min(sum, i, sum - i)
        else:
            sum = max(sum, prev - i)
        sum = min(i, sum)
        prev = i
    print(ans)