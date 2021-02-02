N, W = map(int, input().split())

dp = [[float('inf')]*(50) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
  w, v = map(int, input().split())
  for j in range(50):
    if j >= v:
      dp[i+1][j] = min(dp[i][j], dp[i][j-v] + w)
    else:
      dp[i+1][j] = dp[i][j]
    
print(dp[N])

ans = 0
for index, n in enumerate(dp[N]):
  if n != float('inf'):
    if n <= W:
      ans = index

print(ans)