from collections import deque
N, Q = map(int, input().split())

g = [[] for i in range(N)]

for _ in range(N-1):
  a, b = map(int, input().split())
  g[a-1].append(b-1)

queue = deque()
ans = [0] * N
for _ in range(Q):
  p, q = map(int, input().split())
  p -= 1
  queue.append((p, q))
  while queue:
    v, value = queue.popleft()
    ans[v] += value
    if len(g[v]) == 0:
      continue
    for e in g[v]:
      queue.append((e, value))
print(*ans)
