s = input()
t = input()
SL = len(s)
TL = len(t)

dp = [[0]*(TL+1) for i in range(SL+1)]

for i in range(0, SL):
  for j in range(0, TL):
      if s[i] == t[j]:
        dp[i+1][j+1] = dp[i][j] + 1
      else:
        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])


i = SL
j = TL

ans = ""
while i > 0 and j > 0:
  if dp[i][j] == dp[i-1][j-1] + 1:
    ans = s[i-1] + ans
    i -= 1
    j -= 1
  elif dp[i][j] == dp[i-1][j]:
    i -= 1
  elif dp[i][j] == dp[i][j-1]:
    j -= 1
  else:
    i -= 1
    j -= 1


print(ans)