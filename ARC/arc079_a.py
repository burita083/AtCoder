N, M = map(int, input().split())
from collections import deque
g = [[] for i in range(N)]
for _ in range(M):
  a, b = map(int, input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)

visited = [0] * N
dist = [0] * N
queue = deque([0])
while queue:
  v = queue.popleft()
  visited[v] = 1
  for e in g[v]:
    if visited[e] == 1:
      continue
    dist[e] += dist[v] + 1
    if e == N-1 and dist[e] == 2:
        print(dist)
        print("POSSIBLE")
        exit()
    queue.append(e)
print(dist)
print("IMPOSSIBLE")
