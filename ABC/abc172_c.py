N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cuma = [0]

for a in A:
  cuma.append(cuma[-1]+a)

cumb = [0]
for b in B:
  cumb.append(cumb[-1]+b)

ans = 0
from bisect import bisect
for i, ca in enumerate(cuma):
  if ca > K: break
  t = K - ca
  j = bisect(cumb, t)
  ans = max(ans, i+j-1)

print(ans)