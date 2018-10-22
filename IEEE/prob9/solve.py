n = int(input())
players = [int(x) for x in input().split()]
q = int(input())
for _ in range(q):
    query = int(input())
    possibles = {p for p in players if (p | query) == query}
    ans = 0
    for p in possibles:
        ans |= p
    print("YES" if query == ans else "NO")
