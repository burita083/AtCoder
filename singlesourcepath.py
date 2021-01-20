import heapq
V, E, r = map(int, input().split())

edge = [list() for _ in range(V)]
cost = {}
for e in range(E):
  s, to, cost = map(int, input().split())
  edge[s].append((to, cost))

dist = [float('inf')]*V
dist[r] = 0

heap = []
heapq.heappush(heap, (0, r))
visited = [False] * V
while heap:
  d, current = heapq.heappop(heap)
  visited[current] = True
  if dist[current] < d:
    continue

  print(visited, current)
  for to, cost in edge[current]:
    print(to, cost, current, "aa")
    if visited[to] == False and dist[to] > dist[current] + cost:
      dist[to] = dist[current] + cost
      heapq.heappush(heap, (dist[to], to))

for v in range(V):
  if dist[v] < float('inf'):
    print(dist[v])
  else:
    print("INF")
