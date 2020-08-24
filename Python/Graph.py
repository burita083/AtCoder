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