N = int(input())

from collections import Counter
A = list(map(int, input().split()))
C = Counter(A)

if A[0] != 0:
  print(0)
  exit()

if C[0] > 1:
  print(0)
  exit()

ans = 1
MOD = 10**9+7
for i in range(len(C)-1):
  ans *= pow(C[i], C[i+1], MOD)
  ans %= MOD
print(ans)

