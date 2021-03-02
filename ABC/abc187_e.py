from collections import deque
N = int(input())

edge = []
g = [[] for _ in range(N)]

for _ in range(N-1):
  a, b = map(int, input().split())
  edge.append((a-1, b-1))
  g[a-1].append(b-1)
  g[b-1].append(a-1)
Q = int(input())

ans = [0] * N

depth = [-1] * N
depth[0] = 0
q = [0]
while q:
  at = q.pop()
  for i in g[at]:
    if depth[i] == -1:
      depth[i] = depth[at] + 1
      q.append(i)

s = [0] * N
for q in range(Q):
  t, e, x = map(int, input().split())
  A, B = edge[e-1]
  if depth[A] > depth[B]:
    A, B = B, A
    if t == 1:
      t = 2
    else:
      t = 1 
  if t == 1:
    s[0] += x
    s[B] -= x
  else:
    s[B] += x
  
print(s)
q = [0]
while q:
  at = q.pop()
  for to in g[at]:
    if depth[at] < depth[to]: #toのほうが根が深い場合は、足す
      s[to] += s[at]
      q.append(to)

for i in s:
  print(i)