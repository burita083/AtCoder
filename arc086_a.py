from collections import Counter
N, K = map(int, input().split())

A = list(map(int, input().split()))
C = Counter(A)



count = 0
if len(C) >= K:
  count = len(C)-K
  l = []
  for v in C.values():
    l.append(v)
  l.sort()
  ans = 0
  for i in range(count):
    ans += l[i]
  print(ans)
else:
  print("0")
  exit()