from collections import deque
N, X, Y = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(N-1):
  graph[i].append(i+1)
  graph[i+1].append(i)
graph[X-1].append(Y-1)
graph[Y-1].append(X-1)

ans = [0] * N
for i in range(N):
  dist = [-1] * N
  queue = deque([i])
  dist[i] = 0
  while queue:
    v = queue.popleft()
    for e in graph[v]:
      if dist[e] != -1:
        continue
      dist[e] = dist[v] + 1
      queue.append(e)
  for d in dist:
    ans[d] += 1
    
for i in range(1, N):
  print(ans[i]//2)

