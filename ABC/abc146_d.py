from collections import deque
N = int(input())
graph = [[] for _ in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  graph[a-1].append((b-1, i))
  graph[b-1].append((a-1, i))

queue = deque([0])
ans = [0] * N
ngs = [-1] * N
K = 0

num_color = 0
while queue:
  v = queue.popleft()
  color = 1
  ng_color = ngs[v]
  for e, i in graph[v]:
    if ans[i] == 0:
      if color == ng_color:
        color += 1
      num_color = max(num_color, color)
      ngs[e] = color
      ans[i] = color
      color += 1
      queue.append(e)
print(num_color)
for i in range(N-1):
  print(ans[i])