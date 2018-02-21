n = int(input())

print(len([q for q in range(1, n) if n % q == 0]))