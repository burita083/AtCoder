import heapq

N, M = map(int, input().split())
A = [-int(A) for A in input().split()]
heapq.heapify(A)

for x in range(M):
  most = -heapq.heappop(A)
  most //= 2
  heapq.heappush(A, -most)

print(-sum(A))