for _ in range(int(input())):
    input()
    a = [int(x) for x in input().split()]
    prefix_value = a[0]
    suffix_value = 0
    steps = 0
    for x, y in zip(a, a[1:]):
        if x > y:
            steps += x - y
            prefix_value = y - suffix_value
        elif y > x:
            steps += y - x
            suffix_value += y - x
    print(steps + abs(prefix_value))
