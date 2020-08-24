import collections
N, K = map(int, input().split())

l = []
for _ in range(K):
  d = int(input())
  A = list(map(int, input().split()))
  for a in A:
    l.append(a)

c = collections.Counter(l)

print(N-len(c))

