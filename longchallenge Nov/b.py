for _ in range(int(input())):
	input()
	l = [int(x) for x in input().split()]
	poss = {}
	xs = set(l)
	for i, x in enumerate(l):
		if x not in poss:
			poss[x] = set()
		poss[x].add(i + 1)
	found = False
	for x in poss:
		times = 0
		for y in poss[x]:
			if y in xs:
				times += 1
		if times >= 2:
			found = True
			break
	print("Truly Happy" if found else "Poor Chef")