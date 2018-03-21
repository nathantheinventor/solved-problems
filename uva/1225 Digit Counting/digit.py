for _ in range(int(input())):
    tmp = "".join(map(str, range(1,int(input()) + 1)))
    print(*map(tmp.count, "0123456789"))