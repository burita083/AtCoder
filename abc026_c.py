from collections import deque
N = int(input())
graph = [[] for _ in range(N)]

for i in range(2, N+1):
  B = int(input())
  graph[i-1].append(B-1)
  graph[B-1].append(i-1)

print(graph)
queue = deque([0])
ans = [0] * N
dist = [-1] * N #Visitedとして使う
moneys = [-1] * N

while queue:
  v = queue.popleft()
  print(len(graph[v]), v, "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
  if v != 0 and len(graph[v]) == 1:
    moneys[v] = 1
  for e in graph[v]:
    if dist[e] != -1: #距離が確定確定してたらスルー
      continue
    dist[e] = dist[v] + 1
    queue.append(e)
while moneys[0] == -1:
  queue = deque([0])
  dist = [-1] * N #Visitedとして使う
  while queue:
    v = queue.popleft()
    flag = True
    print(moneys)
    print(graph)
    for i in graph[v]:
      print(i, v, "aaaaaaa")
      if i == 0:continue
      if moneys[i] == -1:
        flag = False
    if moneys[v] == -1 and flag:
      print("aaa", v)
      mn = float('inf')
      mx = -100
      for g in graph[v]:
        if g == 0: continue
        mn = min(moneys[g], mn)
        mx = max(moneys[g], mx)
      moneys[v] = mn + mx + 1

    for e in graph[v]:
      if dist[e] != -1: #距離が確定確定してたらスルー
        continue
      dist[e] = dist[v] + 1
      queue.append(e)


print(moneys, "aaa")
print(moneys[0])