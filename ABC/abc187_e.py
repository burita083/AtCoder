from collections import deque
N = int(input())

graph = [[] for _ in range(N)]

l = []
for _ in range(N-1):
  a, b = map(int, input().split())
  l.append((a-1,b-1))
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)
Q = int(input())

ans = [0] * N
for q in range(Q):
  visited = [0] * N
  t, e, x = map(int, input().split())
  if t == 1:
    queue = deque([e-1])
    count = 0
    while queue:
      now = queue.popleft()
      a = -1
      b = -1
      if count == 0:
        a, b = l[e-1]
        now = a
        count += 1
      ans[now] += x
      visited[now] = 1
      for g in graph[now]:
        if g == b: continue
        if visited[g] == 0:
          visited[g] = 1
          queue.append(g)
  else:
    queue = deque([e-1])
    count = 0
    while queue:
      now = queue.popleft()
      a = -1
      b = -1
      if count == 0:
        a, b = l[e-1]
        now = b
        count += 1
      ans[now] += x
      visited[now] = 1
      for g in graph[now]:
        if g == a: continue
        if visited[g] == 0:
          visited[g] = 1
          queue.append(g)
  
for a in ans:
  print(a)