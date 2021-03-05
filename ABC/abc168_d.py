N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]
es = [[] for _ in range(N)]

for a, b in AB:
  a, b = a-1, b-1
  es[a].append(b)
  es[b].append(a)

from collections import deque
q = deque([0])

INF = float('inf')
dist = [INF] * N
dist[0] = 0
back = [-1] * N

while q:
  v = q.popleft()
  for to in es[v]:
    if dist[to] != INF: continue
    dist[to] = dist[v] + 1
    back[to] = v+1
    q.append(to)

for i in range(1, N):
  if back[i] == -1: 
    print("No")
    exit()

print("Yes")
for i in range(1, N):
  print(back[i])