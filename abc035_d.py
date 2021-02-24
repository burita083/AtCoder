import heapq
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
edge = [list() for _ in range(N)]
reverse = [list() for _ in range(N)]
cost = {}
for e in range(M):
  s, to, cost = map(int, input().split())
  s -= 1
  to -= 1
  edge[s].append((to, cost))
  reverse[to].append((s, cost))

dist = [float('inf')]*N
dist[0] = 0
dist2 = [float('inf')]*N
dist2[0] = 0

ans = [0]*N

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

heap = []
heapq.heappush(heap, (0, 0))
visited = [False] * N
while heap:
    d, current = heapq.heappop(heap)
    visited[current] = True
    if dist2[current] < d:
        continue

    for to, cost in reverse[current]:
        if visited[to] == False and dist2[to] > dist2[current] + cost:
            dist2[to] = dist2[current] + cost
            heapq.heappush(heap, (dist2[to], to))


ans = -1
for v in range(N):
    ans = max((T-dist[v]-dist2[v])*A[v], ans)
print(ans)