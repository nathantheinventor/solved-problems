for _ in range(int(input())):
    m, n = map(int, input().split())
    curr = set([0])
    for _ in range(n):
        l = [int(x) for x in input().split()[1:]]
        tmp = []
        for i in l:
            for j in curr:
                tmp.append(i + j)
        curr = set(tmp)
    
    print(max([x for x in curr if x <= m]) if min(curr) <= m else "no solution")