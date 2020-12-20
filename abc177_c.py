N = int(input())
A = list(map(int,input().split()))
cums = [0]
for a in A:
  print(cums[-1])
  cums.append(cums[-1] + a)
 
MOD = 10**9+7
ans = 0
print(cums)
for i in range(N-1):
  print(cums[i+1])
  ans += A[i] * (cums[-1] - cums[i+1])
  ans %= MOD
print(ans)

import numpy
ans = 0
 
cA = numpy.cumsum(A)
 
for i in range(1, N):
    ans += i*A[i] * cA[i-1]
    ans %= MOD
print(ans)