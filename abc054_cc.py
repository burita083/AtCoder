from collections import deque
N, M = map(int, input().split())

graph = [[] for i in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

l = []
count = 0
def dfs(start):
    l.append(start)
    print(l)
    if len(l) == N:
        global count
        count += 1

    for n in graph[start]:
        if n in l:
            continue
        dfs(n)
    l.pop()
dfs(0)
print(count)