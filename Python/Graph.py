N, M = map(int, input().split())

H = list(map(int, input().split()))

#AB = [tuple(map(int, input().split())) for i in range(M)]

#丸暗記。隣接リストの初期化
graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

  ans = 0

for n in range(N):
  flag = True
  for to in graph[n]:
    if H[n] <= H[to]:
      flag = False
    
  if flag:
    ans += 1
  
print(ans)

from collections import deque
N, Q = map(int, input().split())

g = [[] for i in range(N)]

for _ in range(N-1):
  a, b = map(int, input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)

cum = [0]*N
a = 0
PQ = [tuple(map(int, input().split())) for i in range(Q)]
for p, q in PQ:
  a += q
  cum[p-1] += q
  
queue = deque([0])
ans = [0] * N
ans[0] = cum[0]

visited = [0] * N

while queue:
  v = queue.popleft()
  visited[v] = 1
  for e in g[v]:
    if visited[e] == 1:
      continue
    cum[e] += cum[v]
    queue.append(e)
print(*cum)
