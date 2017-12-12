for _ in range(int(input())):
    a, b, c, d = input().split()
    a, b, c, d = int(a), int(b), float(c), float(d)
    years = 0
    while a <= b:
        years += 1
        a = int(a * (1 + c / 100))
        b = int(b * (1 + d / 100))
        if years > 100:
            print("Mais de 1 seculo.")
            break
    else:
        print("{} anos.".format(years))