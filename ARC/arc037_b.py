from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

ans = 0
visited = [False] * N
for i in range(N):
  if visited[i]:
    continue
  queue = deque([(i, -1)])
  f = True
  c = 0
  while queue:
    v, prev = queue.popleft()
    visited[v] = True
    for e in graph[v]:
      if e == prev: continue
      if visited[e]:
        c += 1
        continue
      prev = v
      queue.append((e, prev))
    if c >= 2:
      f = False
  if f:
    ans += 1
print(ans)
