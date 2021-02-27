N, M, X = map(int, input().split())
CA = [list(map(int,input().split())) for i in range(N)]

ans = float('inf')

for i in range(1<<N):
  a = [0] * (M+1)

  print(i)
  for j in range(N):
    if ((i >> j) & 1):
      for x, k in enumerate(CA[j]):
        a[x] += k

  if all(a >= X for a in a[1:]):
    ans = min(ans, a[0])

print(-1 if ans == float('inf') else ans)


