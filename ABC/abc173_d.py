N = int(input())

A = list(map(int, input().split()))

A.sort()
A.reverse()

ans = 0

count = 0
for i in range(len(A)):
  if i == 0:
    ans += A[i]
    count += 1
  else:
    ans += A[i]
    count += 1
    if count == len(A)-1:
      break
    count += 1
    ans += A[i]
    if count == len(A)-1:
      break

print(ans)