n, s, m = map(int, input().split())
l = [int(x) for x in input().split()]
visited = [False for _ in range(n)]

square = s - 1
hops = 0
while True:
    if square >= n:
        print("right")
        print(hops)
        break
    elif square < 0:
        print("left")
        print(hops)
        break
    elif visited[square]:
        print("cycle")
        print(hops)
        break
    elif l[square] == m:
        print("magic")
        print(hops)
        break
    hops += 1
    visited[square] = True
    square += l[square]
