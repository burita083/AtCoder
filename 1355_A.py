t = int(input())

for _ in range(t):
  N, K = map(int, input().split())
  ans = N
  prev = 0
  for i in range(1, K):
    mn = float('inf')
    mx = 0
    for s in str(ans):
      mn = min(int(s), mn)
      mx = max(int(s), mx)
    ans += mn*mx 
    if prev == ans:
      break
    prev = ans

  print(ans)


