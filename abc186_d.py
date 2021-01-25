N = int(input())

A = list(map(int, input().split()))

A.sort()
ans = 0
sm = 0
for i in range(N):
    sm += A[i]
r = sm-A[-1]

n = N+(N+1)//2
for i in range(1, N-1):
    sm -= A[i-1]
    ans += i*sm

for i in range(2, N):
    ans -= i*A[i-2]

print(ans)