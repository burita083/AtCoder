N = int(input())
A = list(map(int,input().split()))
cums = [0]
sm = 0
for a in A:
  sm += a
 
MOD = 10**9+7
ans = 0
for i in range(N-1):
  sm -= A[i]
  ans += A[i] * sm
  ans %= MOD
print(ans)
