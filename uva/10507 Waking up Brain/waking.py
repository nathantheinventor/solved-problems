n = int(input())
while True:
    m = int(input())
    areas = {c: [0, False] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    for c in input():
        areas[c][1] = True
        
    adj = {c: {} for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    for i in range(m):
        a,b = list(input())
        adj[a][b] = 1
        adj[b][a] = 1
    
    years = 0
    while years < 50 and len([i for i in areas if areas[i][1]]) < n:
        years += 1
        woken = []
        for c in  "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            awake = 0
            for d in adj[c]:
                if areas[d][1]:
                    awake += 1
            if awake >= 3:
                woken.append(c)
        for c in woken:
            areas[c][1] = True
        if len(woken) == 0:
            break
    if len([i for i in areas if areas[i][1]]) < n:
        print("THIS BRAIN NEVER WAKES UP")
    else:
        print("WAKE UP IN, {}, YEARS".format(years))
    
    try:
        input()
        n = int(input())
    except:
        exit(0)