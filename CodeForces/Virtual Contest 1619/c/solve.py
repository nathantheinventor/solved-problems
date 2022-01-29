def solve(a, s):
    ans = []
    j = 0
    for i in range(19):
        x = int(a[i])
        y = int(s[j])
        if y >= x:
            ans.append(str(y - x))
            j += 1
        else:
            ans.append(str(10 + y - x))
            assert s[j + 1] == "1"
            j += 2
    return "".join(ans)

for _ in range(int(input())):
    a, s =  input().split()
    try:
        print(int(solve(a[::-1] + "000000000000000000000000000000", s[::-1] + "000000000000000000000000000000")[::-1]))
    except:
        print(-1)