for _ in range(int(input())):
    l = [int(x) for x in input().split()[1:]]
    print("Case {}: {}".format(_ + 1, l[len(l) // 2]))