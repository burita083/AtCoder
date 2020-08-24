N, M, Q = map(int, input().split())

#AB = [tuple(map(int, input().split())) for i in range(M)]
graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

  ans = 0
c = list(map(int, input().split()))
d = {}
for i, x in enumerate(c):
  d[i] = x


for _ in range(Q):
  s = list(map(int, input().split()))
  if s[0] == 1:
    print(d[s[1]-1])
    for to in graph[s[1]-1]:
      d[to] = d[s[1]-1]
  else:
    print(d[s[1]-1])
    d[s[1] - 1] = s[2]
