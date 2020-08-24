import collections
t = int(input())

for _ in range(t):
  group = 0
  next = 0
  n = int(input())
  A = list(map(int, input().split()))
  c = collections.Counter(A)
  l = sorted(c.items())
  for i, x in enumerate(l):
    group += (x[1] + next) // x[0]
    if i+1 <= len(l):
      next = (x[1] + next) % x[0]
  print(group)
