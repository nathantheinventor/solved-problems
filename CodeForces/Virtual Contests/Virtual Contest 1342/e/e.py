def solve(x, n):
    rows = [0 for _ in range(n)]
    cols = [0 for _ in range(n)]
    cnt = 0
    for i in range(n ** 2):
        if x & (1 << i):
            cnt += 1
            cols[i % n] += 1
            rows[i // n] += 1
    
    if cnt != n:
        return -1
    
    for i in range(n):
        for j in range(n):
            if rows[i] == 0 and cols[j] == 0:
                return -1
    
    k = 0
    for r in rows:
        k += max(0, r - 1)

    for c in cols:
        k += max(0, c - 1)

    return k

# print(solve(15, 2))

for n in range(1, 6):
    results = {k: 0 for k in range(300)}
    x = 0
    for i in range(2 ** (n ** 2)):
        k = solve(i, n)
        if k != -1:
            results[k] += 1
        x = max(x, k)
    
    for k in range(x + 1):
        print(n, k, results[k])
