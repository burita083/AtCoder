N, M = map(int, input().split())

A = list(map(int, input().split()))

g = [[] * N for _ in range(N+1)]
for x in range(M):
  X, Y = list(map(int, input().split()))
  X, Y = X-1, Y-1
  g[X].append(Y)

dp = [float('inf')] * (N+1)
for i in range(N):
  for e in g[i]:
    dp[e] = min(dp[e], dp[i])
    dp[e] = min(dp[e], A[i])
 

ans = -float('inf')
for i in range(N):
  ans = max(ans, A[i] - dp[i]) 
print(ans)
