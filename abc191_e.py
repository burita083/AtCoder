import heapq
V, E = map(int, input().split())

edge = [list() for _ in range(V)]
cost = {}
for e in range(E):
  s, to, cost = map(int, input().split())
  s, to = s-1, to-1
  edge[s].append((to, cost))


Dist = []
for v in range(V):
  heap = []
  heapq.heappush(heap, (0, v))
  dist = [float('inf')]*V
  dist[v] = 0
  visited = [False] * V
  flag = False
  while heap:
    d, current = heapq.heappop(heap)
    visited[current] = True
    if dist[current] < d:
      continue

    for to, cost in edge[current]:
      if visited[to] == False and dist[to] > dist[current] + cost:
          dist[to] = dist[current] + cost
          heapq.heappush(heap, (dist[to], to))
  Dist.append(dist)

l = []
for i in range(V):
  ans = float('inf')
  for v in range(V):
    for (to, cost) in edge[v]:
      if to == i:
        ans = min(ans, Dist[i][v] + cost)
  l.append(ans)

for ll in l:
  if ll == float('inf'):
    print(-1)
  else:
    print(ll)
