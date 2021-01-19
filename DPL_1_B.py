N, W = map(int, input().split())

dp = [[0] * W for i in range(N)]
for i in range(N):
  v, w = map(int, input().split())
  for i in range(N):
    if W >= w:
      dp[i][w] = max(dp[i][w], dp[i][W-w]+v)
print(dp)
print(max(dp[N-1]))

