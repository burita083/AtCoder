import collections
N = int(input())

A = list(map(int, input().split()))

c = collections.Counter(A)

for x in range(1, N+1):
  if x in c.keys():
    print(c[x])
  else:
    print(0)
