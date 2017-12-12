n = int(input())
denom = [100, 50, 20, 10, 5, 2, 1]
m = n
x = []
for i in denom:
    x.append(m // i)
    m %= i


print(n)
print("{} nota(s) de R$ 100,00".format(x[0]))
print("{} nota(s) de R$ 50,00".format(x[1]))
print("{} nota(s) de R$ 20,00".format(x[2]))
print("{} nota(s) de R$ 10,00".format(x[3]))
print("{} nota(s) de R$ 5,00".format(x[4]))
print("{} nota(s) de R$ 2,00".format(x[5]))
print("{} nota(s) de R$ 1,00".format(x[6]))