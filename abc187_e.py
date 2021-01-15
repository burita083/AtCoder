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
  print("______________")
  if t == 1:
    queue = deque([e-1])
    while queue:
      now = queue.popleft()
      print(now+1)
      b = l[e-1][1]
      ans[now] += x
      visited[now] = 1
      for g in graph[now]:
        if g == b: continue
        if visited[g] == 0:
          visited[g] = 1
          queue.append(g)
    print(ans)
  else:
    queue = deque([e-1])
    while queue:
      now = queue.popleft()
      print(now+1)
      a = l[e-1][0]
      ans[now] += x
      visited[now] = 1
      for g in graph[now]:
        if g == b: continue
        if visited[g] == 0:
          visited[g] = 1
          queue.append(g)
    print(ans)
  
print(ans)