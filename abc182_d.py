N = int(input())

A = list(map(int, input().split()))

ans = 0
p = 0
m = 0
d = 0

for i in range(N):
  d += A[i]
  m = max(m, d)
  ans = max(ans, p+m)
  p += d
print(ans)
