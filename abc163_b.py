N, M = map(int, input().split())
A = list(map(int, input().split()))


for i in A:
  N -= i

if N < 0:
  print(-1)
else:
  print(N)
