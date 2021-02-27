import collections
N, M = map(int, input().split())
A = collections.Counter(list(map(int, input().split())))

for _ in range(M):
  B, C = map(int, input().split())
  A[C] += B

A = sorted(A.items(), key=lambda x:x[0], reverse=True)

ans = 0
for key, count in A:
  if N > count:
    ans += key * count
    N -= count
  else:
    ans += key * N
    break

print(ans)
