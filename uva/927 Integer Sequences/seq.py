for _ in range(int(input())):
    coeffs = [int(x) for x in input().split()[1:]]
    d = int(input())
    k = int(input())
    sum = 0
    n = 0
    for i in range(2000):
        sum += i * d
        if sum >= k:
            n = i
            break
    ans = 0
    mult = 1
    for i in coeffs:
        #print(i * mult)
        ans += i * mult
        mult *= n
    print(ans)