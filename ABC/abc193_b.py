N = int(input())

mn = float('inf')
for i in range(N):
  A, P, X = map(int, input().split())
  remain = X - A
  if remain >= 1:
    mn = min(P, mn)
if mn == float('inf'):
  print(-1)
  exit()
print(mn)
