x = int(float(input()) * 100)

curr = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
ans = []

for i in curr:
    ans.append(x // i)
    x %= i

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(ans[0]))
print("{} nota(s) de R$ 50.00".format(ans[1]))
print("{} nota(s) de R$ 20.00".format(ans[2]))
print("{} nota(s) de R$ 10.00".format(ans[3]))
print("{} nota(s) de R$ 5.00".format(ans[4]))
print("{} nota(s) de R$ 2.00".format(ans[5]))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(ans[6]))
print("{} moeda(s) de R$ 0.50".format(ans[7]))
print("{} moeda(s) de R$ 0.25".format(ans[8]))
print("{} moeda(s) de R$ 0.10".format(ans[9]))
print("{} moeda(s) de R$ 0.05".format(ans[10]))
print("{} moeda(s) de R$ 0.01".format(ans[11]))