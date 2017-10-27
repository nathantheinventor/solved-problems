for _ in range(int(input())):
    s = sorted(input())
    n = int(input())
    permutations = [1]
    l = len(s)
    ans = ""
    for i in range(1, l + 1):
        permutations.append(permutations[-1] * i)
    for i in range(l):
        choice = s[n // permutations[l - i - 1]]
        del s[n // permutations[l - i - 1]]
        n %= permutations[l - i - 1]
        ans += choice
    print(ans)