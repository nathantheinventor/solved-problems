#!/bin/python3

import sys

def minimumTime(n, b, m, k):
    dist = []
    last = b.index(1)
    if 1 in b[last + 1:]:
        for i in range(b[last + 1:].index(1) + last + 1, n):
            if b[i] == 1:
                dist.append(i - last)
                last = i
    if m - 1 > len(dist):
        return -1
    ans = 10 ** 20
    s = sum([k * x for x in dist[:m - 1]])
    tmp = sum([(i + 1) * k * x for i, x in enumerate(dist[:m - 1])])
    running = b.index(1)
    ans = tmp + running
    #print(tmp, running)
    for i in range(m - 1, len(dist)):
        tmp -= s
        s -= dist[i - m + 1] * k
        s += dist[i] * k
        tmp += dist[i] * k * (m - 1)
        running += dist[i - m + 1]
        #print(tmp, running)
        ans  = min(ans, tmp + running)
    
    #dist = dist[::-1]
    #s = sum([k * x for x in dist[:m - 1]])
    #tmp = sum([(i + 1) * k * x for i, x in enumerate(dist[:m - 1])])
    #running = n - 1 - b[::-1].index(1)
    #ans = min(ans, tmp + running)
    #print(tmp, running)
    #for i in range(m - 1, len(dist)):
        #tmp -= s
        #s -= dist[i - m + 1] * k
        #s += dist[i] * k
        #tmp += dist[i] * k * (m - 1)
        #running -= dist[i - m + 1]
        #print(tmp, running)
        #ans  = min(ans, tmp + running)
    
    return ans
        

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    b = list(map(int, input().strip().split(' ')))
    result = minimumTime(n, b, m, k)
    print(result)
