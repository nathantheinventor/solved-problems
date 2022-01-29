def transform(ratings, start):
    ans = []
    for p, i in sorted(ratings):
        ans.append((i, start))
        start += 1
    return sorted(ans)

for _ in range(int(input())):
    input()
    ps = [int(x) for x in input().split()]
    r = [int(x) for x in input()]
    liked_ratings = [(p, i) for i, p in enumerate(ps) if r[i]]
    disliked_ratings = [(p, i) for i, p in enumerate(ps) if not r[i]]
    liked_ratings2 = transform(liked_ratings, len(disliked_ratings) + 1)
    disliked_ratings2 = transform(disliked_ratings, 1)
    p1 = 0
    p2 = 0
    ans = []
    for x in r:
        if x:
            ans.append(liked_ratings2[p1][1])
            p1 += 1
        else:
            ans.append(disliked_ratings2[p2][1])
            p2 += 1
    print(*ans)
