n = int(input())
h = n // 3600
n %= 3600
m = n // 60
n %= 60
s = n

print("{}:{}:{}".format(h, m, s))