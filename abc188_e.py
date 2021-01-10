N, M = map(int, input().split())

A = list(map(int, input().split()))

g = [[] * N for _ in range(M)]
for x in range(M):
  X, Y = list(map(int, input().split()))
  g[X].append(Y)

print(g)