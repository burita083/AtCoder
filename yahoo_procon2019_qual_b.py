from collections import deque

g = [[] for _ in range(4)]

for _ in range(3):
  a, b = map(int, input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)

for i in range(3):
    queue = deque([i])
    visited = [0] * 4
    dist = [0] * 4
    while queue:
        v = queue.popleft()
        visited[v] = 1
        for e in g[v]:
            if visited[e] == 1: continue
            dist[e] = dist[v] + 1
            if dist[e] == 3:
                print("YES")
                exit()
            queue.append(e)
print("NO")
