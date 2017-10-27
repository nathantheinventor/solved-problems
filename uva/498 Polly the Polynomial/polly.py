coeff = [int(x) for x in input().split()][::-1]
xs = [int(x) for x in input().split()]
while True:
    ans = []
    for x in xs:
        tmp = 0
        for i in range(len(coeff)):
            tmp += coeff[i] * x ** i
        ans.append(tmp)
    print(" ".join(map(str, ans)))
    try:
        coeff = [int(x) for x in input().split()][::-1]
        xs = [int(x) for x in input().split()]
    except:
        exit(0)