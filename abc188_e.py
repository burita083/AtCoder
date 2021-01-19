N, M = map(int, input().split())

A = list(map(int, input().split()))
l = []
for i in range(len(A)):
  l.append((A[i], i))
l.sort()

g = [[] * N for _ in range(N+1)]
for x in range(M):
  X, Y = list(map(int, input().split()))
  X, Y = X-1, Y-1
  g[X].append(Y)

from collections import deque

queue = deque()
ans = -float('inf')
d = {}
visited = [0] * N
for ll in l:
  history = []
  queue.append(ll[1])
  sellMax = -float('inf')
  while queue:
    current = queue.popleft()
    for e in g[current]:
      if visited[e] == 1: 
        sellMax = max(sellMax, d[e])
        continue
      visited[e] = 1
      history.append(e)
      sellMax = max(sellMax, A[e])
      queue.append((e))
      for h in history:
        d[h] = sellMax
  ans = max(sellMax - ll[0], ans)
  
print(ans)

