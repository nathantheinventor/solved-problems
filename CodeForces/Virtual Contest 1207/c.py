for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()
    first_1 = s.find("1")
    last_1 = s.rfind("1")
    cost = n * a + (n + 1) * b
    if first_1 > -1:
        cost += 2 * a
        cost += (last_1 - first_1 + 2) * b
        groups = []
        cur = ""
        for c in s[first_1:last_1+1]:
            if c == "0":
                cur += c
            else:
                groups.append(cur)
                cur = ""
        
        for group in groups:
            if len(group) < 2:
                continue
            new_cost = 2 * a - (len(group) - 1) * b
            if new_cost < 0:
                cost += new_cost

    print(cost)