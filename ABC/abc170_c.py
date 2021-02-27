X, N = map(int, input().split())
P = list(map(int, input().split()))

P.sort()
ans = abs(10000000)
for i in range(-101, 102):
  if not i in P:
    ans = min(ans, abs(i-X))

if not X-ans in P:
  print(X-ans)
else:
  print(X+ans)
