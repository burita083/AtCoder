import collections
N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)
Q = int(input())
ans = sum(A)
for q in range(Q):
  B, C = map(int, input().split())
  count = c[B]
  c[B] -= count
  c[C] += count
  ans += (C-B)*count
  print(ans)

