x = int(input())

y = x // 365
x %= 365
m = x // 30
x %= 30
d = x

print("{} ano(s)".format(y))
print("{} mes(es)".format(m))
print("{} dia(s)".format(d))