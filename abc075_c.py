N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]
es = [[] for _ in range(N)]

for a, b in AB:
  a, b = a-1, b-1
  es[a].append(b)
  es[b].append(a)

from collections import deque

count = 0
for i in range(N):
    for now in range(len(es[i])):
        seen = [0] * N
        q = deque([i])
        while q:
            v = q.popleft()
            for to in es[v]:
                if to == es[i][now] and v == i: 
                    continue
                if seen[to] != 0: continue
                seen[to] = 1
                q.append(to)
        if sum(seen) != N:
            count += 1
print(count//2)