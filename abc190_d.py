N = int(input())


N, K = map(int, input().split())

A = []
for i in range(20):
  A.append(i)

ans = 0
r = 0
s = 0
l = []
ans = []
while (r < N)
  s += A[r]
  l.append(A[r])
  r += 1
  if s == N:
    ans.append(l)
    l = []
    s -= A[l]

print(ans)
