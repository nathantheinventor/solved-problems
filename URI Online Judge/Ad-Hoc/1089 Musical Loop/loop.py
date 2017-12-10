def peaks(n, l):
    l = [l[-1]] + l + [l[0]]
    ans = 0
    for i in range(1, n + 1):
        # print(l[i] < l[i - 1] and l[i] < l[i + 1], l[i] > l[i - 1] and l[i] > l[i + 1])
        if l[i] < l[i - 1] and l[i] < l[i + 1]:
            ans += 1
        if l[i] > l[i - 1] and l[i] > l[i + 1]:
            ans += 1
    return ans
        

n = int(input())
while n > 0:
    print(peaks(n, [int(x) for x in input().split()]))
    n = int(input())