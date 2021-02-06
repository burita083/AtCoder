from collections import deque
N, M = map(int, input().split())

AB = [tuple(map(int, input().split())) for i in range(M)]

graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

  ans = 0

N, Q = map(int, input().split())

g = [[] for i in range(N)]

queue = deque([0])
ans = [0] * N

visited = [0] * N
dist = [0] * N

while queue:
  v = queue.popleft()
  visited[v] = 1
  for e in g[v]:
    if visited[e] == 1:
      continue
    dist[e] = dist[v] + 1
    queue.append(e)
