# import sys

for _ in range(int(input())):
    n = int(input())
    k = input()
    if n == 1:
        if k[0] == "9":
            target = 11
        else:
            target = 9
    else:
        if k[0] == "9":
            target = 11 * 10 ** (n - 1) + 11
        else:
            target = 10 * 10 ** (n - 1) + 1
    ans = target - int(k)
    assert len(str(ans)) == n, f"{n} {k}"
    print(ans)
    # print(target, file=sys.stderr)
