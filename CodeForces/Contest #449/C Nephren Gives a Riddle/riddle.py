string = "What are you doing at the end of the world? Are you busy? Will you save us?"
recurse1 = "What are you doing while sending \""
recurse2 = "\"? Are you busy? Will you send \""
recurse3 = "\"?"

last = 75
sizes = []
for _ in range(10 ** 5 + 5):
    sizes.append(last)
    last = min(2 * last + 68, 10 ** 20)

def solve(n, k):
    if k >= sizes[n]:
        return 1, "."
    if n == 0:
        return 1, string[k]
    if k < len(recurse1):
        return 1, recurse1[k]
    k -= len(recurse1)
    if k < sizes[n - 1]:
        return 2, (n - 1, k)
    k -= sizes[n - 1]
    if k < len(recurse2):
        return 1, recurse2[k]
    k -= len(recurse2)
    if k < sizes[n - 1]:
        return 2, (n - 1, k)
    k -= sizes[n - 1]
    return 1, recurse3[k]

ans = ""
for _ in range(int(input())):
    n, k = map(int, input().split())
    state, tmp = solve(n, k - 1)
    while state == 2:
        state, tmp = solve(*tmp)
    ans += tmp

print(ans)