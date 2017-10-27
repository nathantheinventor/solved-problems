def evaluate(s):
    parts = s.split()
    a, b = int(parts[0]), int(parts[2])
    op = parts[1]
    if op == "*":
        ans = a * b
    elif op == "+":
        ans = a + b
    else:
        ans = a - b
    return str(ans)

def format(answers):
    maxLen = max([len(s) for s in answers])
    numCols = 51 // maxLen
    ans = ""
    for i, s in enumerate(answers):
        spaces = maxLen - len(s)
        if i % numCols == 0 and i > 0:
            ans += "\n"
        else:
            ans += " "
        ans += " " * spaces + s
    return ans

n = int(input())
while n > 0:
    answers = []
    for i in range(n):
        s = input()
        answers.append(evaluate(s))
    print(format(answers))
    n = int(input())
    if n > 0:
        print("")