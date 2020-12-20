N = int(input())

A = list(map(int, input().split()))

s = 0
A.sort()
ans = 0
for i in range(N):
    ans += i*A[i] - s
    s += A[i]
print(ans)