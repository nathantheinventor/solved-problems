import random
import sys

for _ in range(int(input())):
    n, k = map(int, input().split())

    # Step 1: check if box 1 contains a stone
    isOne = False
    if n < 31:
        for i in range(2, n + 1):
            print(f"? 1 1")
            print(1)
            print(i)
            sys.stdout.flush()
            if input() == "SECOND":
                print("! 1")
                sys.stdout.flush()
                isOne = True
                break
    else:
        tried = set()
        for i in range(30):
            x = random.randint(2, n)
            idx = 0
            while x in tried:
                idx += 1
                if idx > 100:
                    break
                x = random.randint(2, n)
            
            tried.add(x)
            if idx > 100:
                break

            print(f"? 1 1")
            print(1)
            print(x)
            sys.stdout.flush()
            if input() == "SECOND":
                print("! 1")
                sys.stdout.flush()
                isOne = True
                break
    
    if isOne:
        continue

    # Step 2: Box 1 is a stone; find out which segment has the first gift
    ansGroup = 0
    for i in range(10):
        x = 2 ** i
        if 2 ** (i + 1) > n:
            x = n - 2 ** i
        print(f"? {x} {x}")
        print(*range(1, x + 1))
        print(*range(2 ** i + 1, 2 ** i + x + 1))
        sys.stdout.flush()
        if input() == "FIRST":
            ansGroup = i
            break
    
    # Step 3: The answer is somewhere in range [2^i + 1, 2^(i+1)]
    start = 2 ** ansGroup
    for i in range(ansGroup - 1, -1, -1):
        x = min(2 ** i, n - start)
        print(f"? {x} {x}")
        print(*range(1, x + 1))
        print(*range(start + 1, start + x + 1))
        sys.stdout.flush()
        if input() == "EQUAL":
            start += 2 ** i
    
    print(f"! {start + 1}")
