l = [int(x) for x in input().split()[:-1]]
while True:
    ans = -1000000000000000000000000000000000000
    for i in range(len(l)):
        prod = 1
        for j in range(i, len(l)):
            prod *= l[j]
            ans = max(ans, prod)
    print(ans)
    try:
        l = [int(x) for x in input().split()[:-1]]
    except:
        exit(0)