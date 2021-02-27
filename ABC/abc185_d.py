import math
N, M = map(int, input().split())

A = list(map(int, input().split()))
A = [0] + sorted(A) + [N+1]

M += 2

A.sort()
stamp_len = 10 ** 10
between = []

for i in range(1, M):
  res = A[i] - A[i-1] - 1
  if res <= 0:
    continue
  stamp_len = min(stamp_len, res)
  between.append(res)
print(between)

ans = 0
import math
for B in between:
  print(B/stamp_len)
  ans += math.ceil(B/stamp_len)

print(ans)
