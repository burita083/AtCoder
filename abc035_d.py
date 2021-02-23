import heapq
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
edge = [list() for _ in range(N)]
cost = {}
for e in range(M):
  s, to, cost = map(int, input().split())
  s -= 1
  edge[s].append((to, cost))

dist = [float('inf')]*N
dist[0] = 0

heap = []
heapq.heappush(heap, (0, 0))
visited = [False] * N
while heap:
  d, current = heapq.heappop(heap)
  visited[current] = True
  if dist[current] < d:
    continue

  for to, cost in edge[current]:
    if visited[to] == False and dist[to] > dist[current] + cost:
      dist[to] = dist[current] + cost
      heapq.heappush(heap, (dist[to], to))

ans = [0]*N

ans[0] = A[0] * T