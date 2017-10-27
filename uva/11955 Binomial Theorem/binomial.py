coeffs = [[1]]
for i in range(50):
    last = coeffs[-1]
    new = []
    tmp = 0
    for j in last:
        new.append(tmp + j)
        tmp = j
    new.append(1)
    coeffs.append(new)


for index in range(1, int(input()) + 1):
    s = input()
    first = s.split(")")[0][1:]
    name1 = first.split("+")[0]
    name2 = first.split("+")[1]
    exp = int(s.split("^")[1])
    
    ans = []
    coeff = coeffs[exp]
    for i in range(exp + 1):
        exp2 = i
        exp1 = exp - i
        parts = []
        if coeff[i] != 1:
            parts.append(str(coeff[i]))
        if exp1 != 0:
            if exp1 == 1:
                parts.append(name1)
            else:
                parts.append("{}^{}".format(name1, exp1))
        if exp2 != 0:
            if exp2 == 1:
                parts.append(name2)
            else:
                parts.append("{}^{}".format(name2, exp2))
        ans.append("*".join(parts))
    print("Case {}: {}".format(index, "+".join(ans)))
    