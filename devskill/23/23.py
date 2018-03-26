def powMod(a, b, m):
	if b < 4:
		return (a ** b) % m
	tmp = powMod(a, b // 2, m)
	tmp = tmp ** 2 % m
	if b % 2 == 1:
		tmp *= a
		tmp %= m
	return tmp

for _ in range(int(input())):
	a, b, m = map(int, input().split())
	print("Case {}:".format(_ + 1), powMod(a, b, m))