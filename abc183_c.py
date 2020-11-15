import math
N, K = map(int, input().split())
n = math.factorial(N)

"1 2 3 4 5を配列に"
d = [[0 for j in range(N+1)] for i in range(N+1)]
for i in range(N):
  A = list(map(int, input().split()))
  for (index, a) in enumerate(A):
    d[i+1][index+1] = a

import itertools

l = []
for i in range(2, N+1):
  l.append(i)

ans = 0
for v in itertools.permutations(l, N-1):
  count = 0
  count += d[1][v[0]]
  for k in range(N-2):
    count += d[v[k]][v[k+1]]
  count += d[v[N-2]][1]
  if count == K:
    ans += 1

print(ans)

