from collections import deque
N, K = map(int, input().split())
if K > N:
  print(-1)
  exit()
graph = [[] for _ in range(N)]

for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

queue = deque([0])
ans = [0] * N
dist = [-1] * N #Visitedとして使う


if K == 1:
  print(0)
  exit()
K -= 1
count = 0
while queue:
  v = queue.popleft()
  for e in graph[v]:
    if dist[e] != -1: #距離が確定確定してたらスルー
      continue
    dist[e] = dist[v] + 1
    K -= 1
    count += 1
    if K == 0:
      print(count)
      exit()
    queue.append(e)
print(-1)
