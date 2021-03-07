import math
from collections import Counter
N = int(input())
A = list(map(int, input().split()))  
dp = [0] * (N+1)
for k in A:
  dp[k] += 1

C = Counter(A)
print(C)
C[3] -= 1
if C[0] > 0:
  C[0] -= 1
print(C)
 
sm = 0
for k in dp:
  sm += math.comb(k, 2)

for k in A:
  print(sm - math.comb(dp[k], 2)  + math.comb(dp[k]-1, 2))
