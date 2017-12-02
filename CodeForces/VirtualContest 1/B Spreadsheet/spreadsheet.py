import re

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def toLetters(x):
    if x == "1":
        return "A"
    lastDigit = 0
    tmp = 0
    last = 0
    while tmp < int(x):
        last = tmp
        lastDigit += 1
        tmp += 26 ** lastDigit
    x = int(x) - last - 1
    ans = ""
    for _ in range(lastDigit):
        ans += alpha[x % 26]
        x //= 26
    return ans[::-1]

def fromLetters(x):
    digits = 1
    tmp = 1
    while digits < len(x):
        tmp += 26 ** digits
        digits += 1
    
    mult = 1
    for c in x[::-1]:
        tmp += alpha.index(c) * mult
        mult *= 26
    return tmp
    

def solve(x):
    #print(x)
    if re.match("^R[0-9][0-9]*C[0-9][0-9]*$", x):
        x = x.split("C")
        row = x[1]
        return toLetters(row) + x[0][1:]
    
    row = "".join([c for c in x if c not in alpha])
    col = "".join([c for c in x if c in alpha])
    return "R" + row + "C" + str(fromLetters(col))

for _ in range(int(input())):
    print(solve(input()))