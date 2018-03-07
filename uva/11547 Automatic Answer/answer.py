for _ in range(int(input())):
    n = int(input())
    n *= 567
    n //= 9
    n += 7492
    n *= 235
    n //= 47
    n -= 498
    print(abs(n) // 10 % 10)