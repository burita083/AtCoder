N, W = map(int, input().split())

dp = [[0]*(W+1) for i in range(N+1)]
for i in range(N):
  w, v = map(int, input().split())
  for j in range(W+1):
    if j < w:
      dp[i+1][j] = dp[i][j]
    else:
      dp[i+1][j] = max(dp[i][j-w]+v, dp[i][j])
print(dp[N][W])
