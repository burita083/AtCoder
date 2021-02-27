N = int(input())

A = list(map(int, input().split()))

ans = 0
mx= 0
total = 0
cumsum = 0

for i in range(N):
  cumsum += A[i]
  mx = max(mx, cumsum)
  ans = max(ans, total + mx)
  total += cumsum
print(ans)
