from itertools import permutations
import random

for p in permutations("abcde"):
    p = "".join(p)
    for a in "abcde":
        for b in "abcde":
            diff = abs(p.find(b) - p.find(a))
            print(diff, end=" ")
    print("")
