t = int(input())
for _ in range(t):
  N, A, B, C, D  = map(int, input().split())
  dp = {}
  dp[0] = 0
  dp[1] = D

  next = 1
  for i in range(1, 100):
    next += 1
    dp[next] = dp[next-1] + D

  next2 = 1
  next3 = 1
  next5 = 1
  def solve(n):
    next = i
    next2 = i*2
    next3 = i*3
    next5 = i*5

    if next2 > 1000000000000:
      break
    dp[next2] = min(solve([next]+A), dp[next2])
    dp[next2-1] = min(dp[next2]+D, dp[next2-1])
    dp[next2+1] = min(dp[next2]+D, dp[next2+1])

    if next3 > 1000000000000:
      break
    dp[next3] = min(dp[next]+B, dp[next3])
    dp[next3-1] = min(dp[next3]+D, dp[next3-1])
    dp[next3+1] = min(dp[next3]+D, dp[next3+1])

    if next5 > 1000000000000:
      break
    dp[next5] = min(dp[next]+C, dp[next5])
    dp[next5-1] = min(dp[next5]+D, dp[next5-1])
    dp[next5+1] = min(dp[next5]+D, dp[next5+1])

    dp[next] = min(dp[next-1]+D, dp[next])

  print(dp[N])