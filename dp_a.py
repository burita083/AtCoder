N = int(input())

h = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0
for n in range(N):
  if n+1<=N-1:
    dp[n+1] = min(dp[n] + abs(h[n]-h[n+1]), dp[n+1])
  if n+2<=N-1:
    dp[n+2] = min(dp[n] + abs(h[n]-h[n+2]), dp[n+2])
print(dp[-1])
