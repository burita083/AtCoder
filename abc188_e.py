N, M = map(int, input().split())

A = list(map(int, input().split()))
l = []
for i in range(len(A)):
  l.append((A[i], i+1))
l.sort()

g = [[] * N for _ in range(N+1)]
for x in range(M):
  X, Y = list(map(int, input().split()))
  g[X].append(Y)


from collections import deque

queue = deque([])
print(queue)
ans = -1
for ll in l:
  queue.append((ll[0], ll[1]))
  v, i = queue.popleft()
  sell = -1
  buy = v
  print(buy, "買う")
  for e in g[i]:
    sell = max(A[e-1], sell) 
    queue.append((e, A[e-1]))
  while queue:
    q = queue.popleft()
    print(q)
  print(sell, "売る")
  ans = max(sell-buy, ans)
  


print(ans)

