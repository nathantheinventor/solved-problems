for _ in range(int(input())):
    s = input()
    a = s.count("0")
    b = s.count("1")
    if a == b:
        print(a - 1)
    else:
        print(min(a, b))
