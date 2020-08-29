N, M = map(int, input().split())

#AB = [tuple(map(int, input().split())) for i in range(M)]
#丸暗記。隣接リストの初期化
graph = [[i+1] for i in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1].append(b)
  graph[b-1].append(a)

ans = -1
for g in graph:
  ans = max(ans, len(set(g)))
print(graph)
print(ans)
