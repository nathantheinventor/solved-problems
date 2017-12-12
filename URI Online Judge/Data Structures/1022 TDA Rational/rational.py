from fractions import gcd

for _ in range(int(input())):
    a,_,b,op,c,_,d = input().split()
    a,b,c,d = map(int, (a,b,c,d))
    denom = 1
    num = 1
    if op == "+":
        num = d * a + c * b
        denom = b * d
    elif op == "-":
        num = d * a - c * b
        denom = b * d
    elif op == "*":
        num = a * c
        denom = b * d
    elif op == "/":
        num = a * d
        denom = b * c
    newNum = num // gcd(num, denom)
    newDenom = denom // gcd(num, denom)
    
    print("{}/{} = {}/{}".format(num, denom, newNum, newDenom))