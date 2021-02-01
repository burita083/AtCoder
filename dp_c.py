N = int(input())

dp = [[0, 1, 2] for i in range(N)]

for i in range(N):
  a, b, c = map(int, input().split())
  if i >= 1:
    dp[i][0] = max(dp[i-1][1]+a, dp[i-1][2]+a)
    dp[i][1] = max(dp[i-1][0]+b, dp[i-1][2]+b)
    dp[i][2] = max(dp[i-1][0]+c, dp[i-1][1]+c)
  else:
    dp[0][0] = a
    dp[0][1] = b
    dp[0][2] = c

print(max(dp[-1][0], dp[-1][1], dp[-1][2]))
