import random

def is_anti_fib(x):
    for a, b, c in zip(x, x[1:], x[2:]):
        if a + b == c:
            return False
    return True

for _ in range(int(input())):
    i = int(input())
    x = [*range(1, i + 1)]
    answers = set()
    for _ in range(100000):
        random.shuffle(x)
        if is_anti_fib(x):
            answers.add(tuple(x))
            if len(answers) == i:
                break
    for x in answers:
        print(*x)