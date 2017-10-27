for _ in range(int(input())):
    input()
    normal = input()
    encrypted = input()
    freq1 = {c: normal.count(c) for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    freq2 = {c: encrypted.count(c) for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    map = {b: a for a, b in zip(sorted(freq1, key=lambda x: freq1[x]), sorted(freq2, key=lambda x: freq2[x]))}
    ans = [map[x] for x in encrypted]
    if _ != 0:
        print("")
    print("".join(ans))