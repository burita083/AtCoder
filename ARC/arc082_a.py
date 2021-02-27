N, K = map(int, input().split())

A = list(map(int, input().split()))


d = {}

for a in A:
  if a in d:
    d[a] += 1
  else:
    d[a] = 1

  if a+1 in d:
    d[a+1] += 1
  else:
    d[a+1] = 1

  if a-1 < 0:continue
  if a-1 in d:
    d[a-1] += 1
  else:
    d[a-1] = 1
ans = -1
for v in d.values():
  ans = max(v, ans)
print(ans)