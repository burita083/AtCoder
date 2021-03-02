N = int(input())
A = list(map(int, input().split()))

ans = 0
r = 1
for l in range(N):
  while r < N and A[r-1] < A[r]:
    r += 1
  if r == l:
    r += 1
  else:
    ans += r - l
print(ans)