n, k, x = map(int, input().split())
l = [int(x) for x in input().split()]
print(sum(l[:-k]) + k * x)