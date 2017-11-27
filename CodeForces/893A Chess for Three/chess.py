total = [1, 2, 3]
curr = [1, 2]
for _ in range(int(input())):
    winner = int(input())
    if winner not in curr:
        print("NO")
        break
    curr = [winner] + [x for x in total if x not in curr]
else:
    print("YES")