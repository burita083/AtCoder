N, W = map(int, input().split())

dp = [[0]*(W+1) for i in range(N+1)]
for i in range(N):
  v, w = map(int, input().split())
  for j in range(W+1):
    if j < w:
      dp[i+1][j] = dp[i][j]
    else:
      print(dp[i][j-w], j-w, j)
      dp[i+1][j] = max(dp[i][j-w]+v, dp[i][j])
      print(dp[0])
      print(dp[1])
      print(dp[2])
      print(dp[3])
print(dp[N][W])

