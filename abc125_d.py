N = int(input())

A = list(map(int, input().split()))

total = 0
minus = 0

l = []
for i in range(N):
  total += abs(A[i])
  l.append(abs(A[i]))
  if A[i] < 0:
    minus += 1

ans = total
if minus % 2 == 1:
  ans = total - 2 * min(l)

print(ans)