def solve(a, b):
    if a <= 1:
        return 1
    if b <= 0:
        return 1
    if b == 1:
        return a
    if a == 2:
        return 1 + b
    if a == 3:
        return 1 + 2 * b
    if a == 4:
        return 1 + 4 * b
    if a == 5:
        return 1 + 8 * b