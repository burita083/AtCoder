import heapq
N = int(input())

L = []

dictfeature = {}
for i in range(N):
  A, B = map(int, input().split())
  if A in dictfeature:
    dictfeature[A].append((-1)*B)
  else:
    listfeature = []
    listfeature.append((-1)*B)
    dictfeature[A] = listfeature

ans = 0
heapq.heapify(L)
for i in range(1, N+1):
  if i in dictfeature:
    for x in dictfeature[i]:
      heapq.heappush(L, x)
    
  ans += (-1)* heapq.heappop(L)
  print(ans)

   