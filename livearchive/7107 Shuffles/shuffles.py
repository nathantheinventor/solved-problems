import math

while True:
    try:
        n = int(input())
        l = {int(x): i for i, x in enumerate(input().split())}
        ans = 1
        for i in range(2, n + 1):
            if l[i] < l[i - 1]:
                ans += 1
        
        print(math.ceil(math.log(ans) / math.log(2)))
    except:
        #print(e)
        exit(0)