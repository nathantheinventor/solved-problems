
m, n = map(int, input().split())
while True:
  ans = [{} for i in range(n)]
  for i in range(m):
      s1 = [int(x) for x in input().split()]
      s2 = input()
      if s1[0] != 0:
          s2 = [int(x) for x in s2.split()]
          for j, k in zip(s1[1:], s2):
              ans[j - 1][i] = k
  
  print(n, m)
  for line in ans:
      ans1 = sorted([i+1 for i in line])
      ans2 = [line[x-1] for x in ans1]
      ans1 = [len(line)] + ans1
      print(" ".join(map(str, ans1)))
      print(" ".join(map(str, ans2)))
  try:
      m, n = map(int, input().split())
  except:
      exit(0)