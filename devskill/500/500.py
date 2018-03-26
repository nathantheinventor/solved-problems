for _ in range(int(input())):
    a, b = map(int, input().split())
    if b > 0 and a % b == 0:
        print(":wink:")
    else:
        print(":kick:")