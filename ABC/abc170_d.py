N = int(input())
A = list(map(int, input().split()))
A.sort()
Amax = A[-1]
dp = [1]*(Amax+1)
ans = 0
if len(A) == 1:
  print(1)
  exit()
for i in range(len(A)-1):
  p = A[i]
  if dp[p] == 1: 
    for q in range(0, Amax+1, p):
      dp[q] = 0
    if A[i] != A[i+1]:
      ans += 1

if dp[Amax] == 1:
  if A[0] != A[-1]:
    ans += 1
print(ans)