for _ in range(int(input().strip())):
  input()
  n = int(input().strip())
  l = [int(input().strip()) for i in range(n)]
  s = sorted(l)
  map = {}
  for i, x in enumerate(s):
    map[x] = i
  #print(map)
  ans = 0
  for i in range(n):
    #print(i, l[i], map[l[i]])
    ans += max(i - map[l[i]], 0)
  print(ans)