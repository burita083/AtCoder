
from collections import deque

N, Q = map(int, input().split())

g = [[] for i in range(N)]

for _ in range(N-1):
  a, b = map(int, input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)

cum = [0]*N
PQ = [tuple(map(int, input().split())) for i in range(Q)]
for p, q in PQ:
  cum[p-1] += q
  
visited = [0] * N

def dfs(thisNode, prev=-1):
  for nextNode in g[thisNode]:
    if nextNode == prev:
      continue
    cum[nextNode] += cum[thisNode]
    dfs(nextNode, thisNode)

dfs(0)
print(*cum)
