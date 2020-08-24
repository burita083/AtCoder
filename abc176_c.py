N = int(input())

A = list(map(int, input().split()))

prev = 0
ans = 0
for i in range(N):
  if i != 0:
    if prev > A[i]:
      ans += prev-A[i]
      A[i] += prev-A[i]
  prev = A[i]
print(ans)


