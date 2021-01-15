import collections
N = int(input())

A = list(map(int, input().split()))

L = [i+A[i] for i in range(N)]
R = [i-A[i] for i in range(N)]
countR = collections.Counter(R)
ans = 0
for l in L:
  ans += countR[l]
print(ans)