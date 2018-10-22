def traverse(tree, depth=0):
    if tree == None:
        return
    root, left, right = tree
    depths[root] = depth
    traverse(left, depth + 1)
    traverse(right, depth + 1)

def parse(infix, prefix):
    if infix == "":
        return None
    root = prefix[0]
    leftIn = infix[:infix.find(root)]
    leftPre = prefix[1:1 + len(leftIn)]
    left = parse(leftIn, leftPre)
    rightIn = infix[infix.find(root) + 1:]
    rightPre = prefix[1 + len(leftIn):]
    right = parse(rightIn, rightPre)
    return (root, left, right)

while True:
    try:
        infix, prefix = input(), input()
    except:
        exit(0)
    depths = {}
    tree = parse(infix, prefix)
    traverse(tree)
    height = max([depths[d] for d in depths]) + 1
    ans = [[" " for _ in range(len(infix))] for _ in range(height)]
    for i, c in enumerate(infix):
        # print(c, depths[c])
        ans[depths[c]][i] = c
    for line in ans:
        print("".join(line))