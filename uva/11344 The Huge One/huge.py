for _ in range(int(input())):
    m = int(input())
    l = [int(x) for x in input().split()[1:]]
    wonderful = True
    for i in l:
        if m % i != 0:
            wonderful = False
    if wonderful:
        print("{} - Wonderful.".format(m))
    else:
        print("{} - Simple.".format(m))