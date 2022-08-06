for _ in range(int(input())):
    n, k = map(int, input().split())
    values = []
    for i in range(n):
        a, b = map(int, input().split())
        values.append((i + 1, a, b))
    
    if k == 1:
        best = -1
        score = 0
        for (i, a, b) in values:
            if a > score:
                best = i
                score = a

        print(1)
        print(best)
    
    else:
        values = sorted(values, key=lambda x: x[1], reverse=True)
        keepers = sorted(values[:k], key=lambda x: x[2])
        destroyers = [i for i, a, b in values[k:] if b > 0]
        turns = []
        for i, a, b in keepers[:-1]:
            turns.append(i)
        
        for i in destroyers:
            turns.append(i)
            turns.append(-i)

        turns.append(keepers[-1][0])

        print(len(turns))
        print(*turns)
