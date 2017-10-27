from collections import deque

n, m = map(int, input().split())
system = 1
while n > 0:
    adj = [[] for i in range(n + 1)]
    for _ in range(m):
        i, j, l = map(int, input().split())
        adj[i].append((j, l))
        adj[j].append((i, l))
    fallen = [-10000000000000 for i in range(n + 1)]
    clock = 0
    
    toProcess = {0: [1]}
    tmpProcess = {0: [1]}
    
    lastkeys = []
    while len(toProcess) > 0:
        #print(fallen)
        m = min(toProcess)
        clock = m
        lastkeys = set(toProcess[m])
        del[toProcess[m]]
        for key in lastkeys:
            #print(key, fallen[key])
            if fallen[key] == -10000000000000:
                fallen[key] = clock
                for other, time in adj[key]:
                    if fallen[other] == -10000000000000:
                        if (clock + time) not in toProcess:
                            toProcess[clock + time] = []
                        if (clock + time) not in tmpProcess:
                            tmpProcess[clock + time] = []
                        toProcess[clock + time].append(other)
                        tmpProcess[clock + time].append(other)
    clock = max(fallen)
    
    ans = "The last domino falls after {}.0 seconds, at key domino {}.".format(clock, tmpProcess[clock][0])
    for i in range(1, n + 1):
        line = adj[i]
        for other, time in line:
            tmp = (time + fallen[other] - fallen[i]) / 2 + fallen[i]
            if tmp > clock:
                clock = tmp
                ans = "The last domino falls after {0:.1f} seconds, between key dominoes {1} and {2}.".format(clock, min(i, other), max(i, other))
    
    print("System #{}".format(system))
    print(ans)
    print("")
    system += 1
    n, m = map(int, input().split())