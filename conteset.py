N = int(input())
P = list(map(int, input().split()))

dp = [[0]*10001 for _ in range(N+1)]

dp[0][0] = 1
for i in range(1, N+1):
  for j in range(10001):
    if dp[i-1][j] == 1:
      dp[i][j] = 1
      dp[i][j+P[i-1]] = 1

print(sum(dp[N]))