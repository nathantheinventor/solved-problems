a, b, c = input().split()
a2, b2, c2 = input().split()
ans = int(b) * float(c)
ans += int(b2) * float(c2)
print("VALOR A PAGAR: R$ {:.2f}".format(ans))