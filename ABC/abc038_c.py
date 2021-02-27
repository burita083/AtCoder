N = int(input())

A = list(map(int, input().split()))

ans = 0
r = 1
for l in range(N):
  if l == r:
    r = l + 1
  while r < N and A[r-1] < A[r]:
    r += 1
  ans += r - l
  
print(ans)