from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

queue = deque([0])
ans = [0] * N
dist = [-1] * N #Visitedとして使う

while queue:
  v = queue.popleft()
  for e in graph[v]:
    if dist[e] != -1: #距離が確定確定してたらスルー
      continue
    dist[e] = dist[v] + 1
    queue.append(e)
