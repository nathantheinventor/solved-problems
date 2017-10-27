primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])



def recurse(n, used, remaining, prev):
    if remaining == 0:
        if (prev + 1) in primes:
            print(*ans)
        else:
            return
    for i in range(1, n + 1):
        if not (used & (2 << (i - 1))):
            if (prev + i) in primes:
                ans[n - remaining] = i
                recurse(n, used | (2 << (i - 1)), remaining - 1, i)
    return ans

s = int(input())
i = 0;
while True:
    ans = [0] * s
    ans[0] = 1
    i += 1
    print("Case {}:".format(i))
    #for l in recurse(s, 2, s - 1, 1):
        #if (l[-1] + 1) in primes:
        #print(*([1] + l))
    recurse(s, 2, s - 1, 1)
    try:
        s = int(input())
        print("")
    except:
        exit(0)