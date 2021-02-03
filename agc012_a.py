N = int(input())

A = list(map(int, input().split()))

A.sort()
ans = 0
for i in range(2*N):
  if i % 2 == 0:
    A.pop()
  else:
    ans += A.pop()
print(ans)
