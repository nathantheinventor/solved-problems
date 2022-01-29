for _ in range(int(input())):
    x = input()
    if len(x) % 2 == 0 and x[:len(x) // 2] * 2 == x:
        print("YES")
    else:
        print("NO")
