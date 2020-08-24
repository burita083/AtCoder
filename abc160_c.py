K, N = map(int, input().split())

A = list(map(int, input().split()))
a = A[-1] - A[0]
ans = 10000000
i = 1
for d in A:
  b = K-A[-i]+A[-i-1]
  ans = min(b, ans)
  i += 1
  if i == len(A):
    break

if a <= ans:
  print(a)
else:
  print(ans)
 