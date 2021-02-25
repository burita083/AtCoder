N = int(input())

s = []
sm = 0
for i in range(N):
  S = int(input())
  sm += S
  s.append(S)

ans = 0
if sm%10!=0:
  print(sm)
  exit()
for S in s:
  temp = sm-S
  if temp%10 != 0:
    ans = max(ans, temp)
print(ans)

