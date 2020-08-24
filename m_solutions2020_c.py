N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
prev = 1
ans = 1
for i in range(0, K):
  prev *= A[i]

for i in range(K, N):
  ans = prev
  ans //= A[count]
  ans *= A[i]
  if ans > prev:
    print("Yes")
  else:
    print("No")
  prev = ans
  count += 1

